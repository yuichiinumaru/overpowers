#!/usr/bin/env node
/**
 * NoteX Skills 通用测试脚本
 * 
 * 支持 9 种能力：slide / mindmap / report / flashcards / quiz / infographic / audio / video / ops-chat
 * 
 * 使用方式：
 *   node skills-run.js --skill <技能> --key <CWork Key> --title "标题" --content "内容"
 *   # 内部调试：node skills-run.js --skill <技能> --access-token <token> --user-id <uid> [--person-id <pid>] --title "标题" --content "内容"
 * 
 * 示例：
 *   node skills-run.js --skill mindmap --key YOUR_KEY --title "口腔AI趋势" --content "主要数据..."
 *   # 内部调试：node skills-run.js --skill mindmap --access-token YOUR_TOKEN --user-id u_001 --title "口腔AI趋势" --content "主要数据..."
 *   node skills-run.js --skill slide   --key YOUR_KEY --title "年度汇报"   --content "销售数据..."
 *   node skills-run.js --skill quiz    --key YOUR_KEY --title "护理测验"   --content "护理规范..."
 *   node skills-run.js --skill ops-chat --key YOUR_KEY --content "查询活跃用户排名"
 *
 * 说明：
 *   Notebook/Source 索引树与最小详情检索请使用：
 *   docs/skills/scripts/source-index-sync.js
 *   NoteX 链接带 Token 打开请使用：
 *   docs/skills/scripts/notex-open-link.js
 */

const https = require('https');
const http = require('http');

// ===================== 配置 =====================
const CONFIG = {
    cworkBaseUrl: 'https://cwork-web.mediportal.com.cn',
    cworkAppCode: 'cms_gpt',
    notexBaseUrl: 'https://notex.aishuo.co/noteX',
    authorizationKey: 'BP',              // 固定值，已验证可用
    pollIntervalMs: 60000,   // 每 60 秒轮询一次
    pollMaxTimes: 20,        // 最多 20 次（20 分钟上限）
};

// 各技能的预计生成时间（仅用于输出提示）
const SKILL_INFO = {
    slide: { name: '演示文稿（PPT）', estimatedTime: '3~5 分钟' },
    mindmap: { name: '思维导图', estimatedTime: '1~2 分钟' },
    report: { name: '分析报告', estimatedTime: '1~3 分钟' },
    flashcards: { name: '记忆卡片', estimatedTime: '1~2 分钟' },
    quiz: { name: '测验题目', estimatedTime: '1~2 分钟' },
    infographic: { name: '信息图', estimatedTime: '2~4 分钟' },
    audio: { name: '音频播客', estimatedTime: '3~6 分钟' },
    video: { name: '视频', estimatedTime: '5~10 分钟' },
    'ops-chat': { name: 'OPS 运营智能助理', estimatedTime: '即时 (内含大模型运算, 最长5分钟)' },
};

const ALLOWED_SKILLS = Object.keys(SKILL_INFO);
// ================================================

function ensureProdUrl(rawUrl, expectedHost, label) {
    let parsed;
    try {
        parsed = new URL(rawUrl);
    } catch {
        throw new Error(`${label} 非法: ${rawUrl}`);
    }

    if (parsed.protocol !== 'https:') {
        throw new Error(`${label} 必须使用 https 协议`);
    }
    if (parsed.hostname !== expectedHost) {
        throw new Error(`${label} 必须使用生产域名 ${expectedHost}`);
    }
    return `${parsed.origin}${parsed.pathname.replace(/\/$/, '')}`;
}

function validateConfig() {
    CONFIG.cworkBaseUrl = ensureProdUrl(CONFIG.cworkBaseUrl, 'cwork-web.mediportal.com.cn', 'cworkBaseUrl');
    const notexUrl = ensureProdUrl(CONFIG.notexBaseUrl, 'notex.aishuo.co', 'notexBaseUrl');
    if (!/\/noteX(\/api)?$/i.test(notexUrl)) {
        throw new Error('notexBaseUrl 路径必须是 /noteX 或 /noteX/api');
    }
    CONFIG.notexBaseUrl = notexUrl;
}

function parseArgs() {
    const args = process.argv.slice(2);
    const result = {};
    for (let i = 0; i < args.length; i += 2) {
        result[args[i].replace(/^--/, '')] = args[i + 1];
    }
    return result;
}

function request(url, options = {}) {
    return new Promise((resolve, reject) => {
        const lib = url.startsWith('https') ? https : http;
        const req = lib.request(url, options, (res) => {
            let data = '';
            res.on('data', chunk => data += chunk);
            res.on('end', () => {
                try {
                    resolve({ status: res.statusCode, json: () => JSON.parse(data) });
                } catch (e) {
                    reject(new Error(`JSON 解析失败: ${data.substring(0, 200)}`));
                }
            });
        });
        req.on('error', reject);
        if (options.timeout) {
            req.setTimeout(options.timeout, () => {
                req.destroy();
                reject(new Error(`请求超时，超过 ${options.timeout / 1000}s`));
            });
        }
        if (options.body) req.write(options.body);
        req.end();
    });
}

// Step 1: 用 CWork Key 换取 xgToken
async function getXgToken(cwKey) {
    console.log('\n[Step 1] 用 CWork Key 换取 xgToken...');
    const url = `${CONFIG.cworkBaseUrl}/user/login/appkey?appCode=${CONFIG.cworkAppCode}&appKey=${cwKey}`;
    const res = await request(url, { method: 'GET', headers: { 'Content-Type': 'application/json' } });
    const data = res.json();

    if (data.resultCode !== 1 || !data.data?.xgToken) {
        throw new Error(`获取 xgToken 失败: ${data.resultMsg || JSON.stringify(data)}`);
    }

    console.log(`✅ xgToken 获取成功`);
    console.log(`   userId:   ${data.data.userId}`);
    console.log(`   personId: ${data.data.personId}`);
    return data.data; // { xgToken, userId, personId }
}

/**
 * 统一鉴权预检：
 * 1) 默认使用 CWork Key 自动换取授权
 * 2) 内部调试时可复用传入 token（--access-token + --user-id）
 */
async function resolveAuthContext(args) {
    if (args['access-token'] && args['user-id']) {
        console.log('\n[Auth] 检测到已提供 token，直接复用...');
        return {
            xgToken: args['access-token'],
            userId: args['user-id'],
            personId: args['person-id'] || args['user-id']
        };
    }

    if (args.key) {
        return await getXgToken(args.key);
    }

    throw new Error('缺少鉴权参数：请提供 --key（推荐），或内部调试时同时提供 --access-token 与 --user-id');
}

// Step 2: 提交技能生成任务
async function createTask(userData, skill, title, content, require_text) {
    const info = SKILL_INFO[skill];
    console.log(`\n[Step 2] 提交「${info.name}」生成任务...`);

    const bizId = `skills_${skill}_${Date.now()}`;
    const body = JSON.stringify({
        title,
        bizId,
        bizType: 'TRILATERA_SKILLS',
        skills: [skill],
        require: require_text || `请根据提供的内容生成${info.name}，主题为：${title}`,
        sources: [{ id: 'src_001', title: `${title} - 素材`, content_text: content }]
    });

    const url = `${CONFIG.notexBaseUrl}/api/trilateral/autoTask`;
    const res = await request(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'authorization': CONFIG.authorizationKey,
            'personId': String(userData.personId),
            'x-user-id': userData.userId,
            'access-token': userData.xgToken,
        },
        body
    });
    const data = res.json();

    if (data.resultCode !== 1) {
        throw new Error(`创建任务失败: ${data.resultMsg}`);
    }

    const taskId = data.data.taskId?.[0];
    console.log(`✅ 任务创建成功`);
    console.log(`   taskId:     ${taskId}`);
    console.log(`   notebookId: ${data.data.noteBook_id}`);
    return taskId;
}

// Step 3: 轮询任务状态
async function pollTaskStatus(taskId, xgToken, skillName) {
    const interval = CONFIG.pollIntervalMs;
    const maxTimes = CONFIG.pollMaxTimes;
    console.log(`\n[Step 3] 轮询任务状态（每 ${interval / 1000}s，最多 ${maxTimes} 次 = ${maxTimes} 分钟上限）...`);

    const url = `${CONFIG.notexBaseUrl}/api/trilateral/taskStatus/${taskId}`;

    for (let i = 1; i <= maxTimes; i++) {
        // 第一次等 3 秒，后续等完整间隔
        await new Promise(r => setTimeout(r, i === 1 ? 3000 : interval));

        const res = await request(url, { method: 'GET' });
        const data = res.json();
        const { task_status, url: taskUrl } = data.data || {};

        console.log(`   第 ${i} 次轮询 → task_status: ${task_status}`);

        if (task_status === 'COMPLETED' && taskUrl) {
            const finalUrl = `${taskUrl}&token=${xgToken}`;
            console.log(`\n🎉 ${skillName}生成完成！`);
            console.log(`   查看链接：${finalUrl}`);
            return finalUrl;
        }

        if (task_status === 'FAILED') {
            throw new Error(`${skillName}生成失败，请检查输入内容后重试`);
        }
    }

    throw new Error(`轮询超时（超过 ${maxTimes} 分钟），请稍后通过 taskId 查询状态`);
}

// Step 2.B: 专门处理 ops-chat 新接口
async function callOpsChat(userData, message, timeoutMs = 300000) {
    if (!message) throw new Error('ops-chat 需要提供提问内容 (--content)');
    console.log(`\n[Step 2] 请求 OPS 智能聊天 (自动最长等待 ${timeoutMs / 60000} 分钟)...`);

    // 固定走生产 NoteX 地址
    const baseUrl = CONFIG.notexBaseUrl.replace(/\/$/, '');
    const url = `${baseUrl}/api/ops/ai-chat`;

    const body = JSON.stringify({ message });

    const res = await request(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'x-user-id': userData.userId,
            'access-token': userData.xgToken,
            'authorization': CONFIG.authorizationKey, // 透传权限
        },
        body,
        timeout: timeoutMs
    });

    const data = res.json();
    if (res.status >= 400 || data.error) {
        throw new Error(`请求 OPS 服务器失败 [${res.status}]: ${data.error || JSON.stringify(data)}`);
    }

    console.log(`\n🎉 回答生成完毕：\n`);
    console.log(data.reply);

    if (data.historyCount !== undefined) {
        console.log(`\n(当前记录历史上下文数: ${data.historyCount} 对)`);
    }
}

// 主流程
async function main() {
    validateConfig();
    const args = parseArgs();

    // 参数校验
    if (!args.skill || !ALLOWED_SKILLS.includes(args.skill)) {
        console.error(`❌ 请指定有效的技能 --skill <技能>`);
        console.error(`   支持：${ALLOWED_SKILLS.join(' | ')}`);
        process.exit(1);
    }
    // 鉴权参数校验：必须满足其一
    const hasReusableToken = !!(args['access-token'] && args['user-id']);
    if (!hasReusableToken && !args.key) {
        console.error('❌ 请提供鉴权信息：--key <CWork Key>（推荐），或内部调试参数 (--access-token <token> + --user-id <uid>)');
        process.exit(1);
    }

    // 业务参数校验：ops-chat 与创作类略有差异
    if (args.skill === 'ops-chat') {
        if (!args.content && !args.title) {
            console.error('❌ ops-chat 请提供问题内容：--content "问题"（或使用 --title）');
            process.exit(1);
        }
    } else {
        if (!args.title) {
            console.error('❌ 请提供标题：--title "标题"');
            process.exit(1);
        }
        if (!args.content) {
            console.error('❌ 请提供素材内容：--content "内容"');
            process.exit(1);
        }
    }

    const info = SKILL_INFO[args.skill];
    console.log(`\n🚀 NoteX Skills — ${info.name}`);
    console.log(`   预计生成时间：${info.estimatedTime}`);
    console.log(`   标题：${args.title}`);

    try {
        const userData = await resolveAuthContext(args);

        if (args.skill === 'ops-chat') {
            await callOpsChat(userData, args.content || args.title);
        } else {
            const taskId = await createTask(userData, args.skill, args.title, args.content, args.require);
            await pollTaskStatus(taskId, userData.xgToken, info.name);
        }
    } catch (err) {
        console.error(`\n❌ 错误：${err.message}`);
        process.exit(1);
    }
}

main();
