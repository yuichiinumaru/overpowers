<img src="https://r2cdn.perplexity.ai/pplx-full-logo-primary-dark%402x.png" style="height:64px;margin-right:32px"/>

# Pesquise e responda sistematicamente as perguntas abaixo para

1. antigravity
2. cursor
3. windsurf
4. gemini-cli
5. codex cli (openai)
6. claude code
7. opencode
8. kilo code
9. factory droid cli

a) onde é o local adequado para guardar local/project rules? Por exemplo, no Antigravity, é .agents/rules/  (dentro do projeto). SEM SER AGENTS.md (ou GEMINI.MD ou CLAUDE.md ou qualquer coisa similar). Se não existir, fale "não tem suporte nativo a pasta de regras".

b) onde é a pasta ou arquivo de global rules? qual o limite de tamanho?

c) onde fica a pasta de skills?

d) onde fica a pasta de commands/workflows?

e) onde fica o arquivo de config de mcps (geralmente um mcp.json) global?

Segue uma visão sistemática por ferramenta, com foco em diretórios/arquivos realmente suportados hoje. Onde algo não existe de forma nativa, respondo exatamente “não tem suporte nativo a pasta de regras” como você pediu.

***

## 1. Antigravity

Antigravity distingue bem entre regras globais (GEMINI.md), regras de workspace/projeto e skills; workflows e MCP são configurados via UI, não por pastas óbvias em disco.[^1_1][^1_2][^1_3]


| Item | Resposta |
| :-- | :-- |
| a) Regras locais (pasta) | Workspace/project rules ficam em `.agent/rules/` dentro do projeto (cada arquivo .md é uma regra). Algumas guias mais antigas também aceitam `.antigravity/rules/` ou um arquivo `.antigravity` único na raiz. [^1_4][^1_5] |
| b) Global rules + limite | Global rules vêm de `~/.gemini/GEMINI.md`, que Antigravity lê automaticamente em todas as workspaces. Guias de marketplace falam em limites de ordem de 6–12 k caracteres por arquivo de regra, recomendando dividir regras grandes em vários arquivos; na prática o limite efetivo é o contexto do modelo, não há número “oficial” rígido. [^1_1][^1_6][^1_2] |
| c) Pasta de skills | Skills de projeto: `.agent/skills/<nome>/SKILL.md`. Skills globais: `~/.gemini/antigravity/skills/<nome>/SKILL.md` (ou variação `global_skills/` em algumas versões), seguindo o padrão Agent Skills. [^1_7][^1_8][^1_3] |
| d) Commands / workflows | Workflows são criados pela UI em “Customizations → Workflows” e salvos como prompts internos; a documentação pública não expõe uma pasta tipo `.antigravity/workflows`. Ou seja, **não tem uma pasta de workflows para você versionar diretamente**. [^1_1][^1_4] |
| e) Config MCP global | Antigravity mantém um `mcp_config.json` interno, acessível em “MCP Servers → Manage MCP Servers → View raw config”. O local exato em disco não é documentado (depende da instalação); a recomendação é editar sempre via essa tela em vez de abrir o arquivo manualmente. [^1_9][^1_10] |


***

## 2. Cursor

Cursor hoje usa regras estruturadas em `.cursor/rules` + “User Rules” globais na UI, além de skills em `.cursor/skills`.[^1_11][^1_12]


| Item | Resposta |
| :-- | :-- |
| a) Regras locais (pasta) | Regras de projeto ficam em `.cursor/rules/` (cada arquivo `.mdc` é uma rule; pode haver `.cursor/rules` aninhados em subpastas). `.cursorrules` na raiz ainda funciona, mas é legado. [^1_11] |
| b) Global rules + limite | Regras globais são “User Rules” configuradas em *Cursor Settings → Rules*; o app persiste isso em arquivos de config internos (sem caminho oficial documentado). A doc pública recomenda manter cada rule relativamente curta (centenas de linhas) e dividir regras grandes, mas não publica um limite rígido de tamanho. [^1_11] |
| c) Pasta de skills | Skills globais: `~/.cursor/skills/<nome>/SKILL.md`. Skills de projeto: `.cursor/skills/<nome>/SKILL.md`. Cursor também lê skills de `~/.claude/skills` e `.claude/skills` para compatibilidade. [^1_12] |
| d) Commands / workflows | Não há um formato de “commands/workflows” em disco equivalente a `.opencode/command` ou `.kilocode/workflows`; workflows são expressos como rules, skills ou prompts salvos dentro da própria UI. Na prática, **não tem uma pasta nativa de commands/workflows**. [^1_11] |
| e) Config MCP global | Vários hosts MCP adotam o padrão `~/.cursor/mcp.json` como arquivo global de configuração; isso é citado em guias de MCP JSON compartilhados entre Claude Desktop, Cursor etc. [^1_13] |


***

## 3. Windsurf

Windsurf migrou de um único `.windsurfrules` para um diretório `.windsurf/rules/` com múltiplos arquivos; globalmente usa `global_rules.md` gerenciado via UI.[^1_14][^1_11]


| Item | Resposta |
| :-- | :-- |
| a) Regras locais (pasta) | Workspace rules modernas ficam em `.windsurf/rules/` na raiz do projeto (cada .md é uma regra). O arquivo plano `.windsurfrules` foi explicitamente marcado como deprecado em favor dessa pasta. [^1_14] |
| b) Global rules + limite | Global rules usam um `global_rules.md` configurado nas preferências do Windsurf; a documentação e coleções de rules o tratam como arquivo global, mas sem caminho absoluto documentado (é mantido na área de config do app). Não há limite numérico oficial de tamanho, só recomendações de mantê‑lo enxuto. [^1_11] |
| c) Pasta de skills | Windsurf suporta Agent Skills, mas não define uma pasta própria tipo `.windsurf/skills`; em geral, skills são instaladas nos diretórios padrão do ecossistema Agent Skills (`~/.agents/skills` e `.agents/skills`) via CLIs de skills e então descobertas por vários agentes, incluindo Windsurf. [^1_15] |
| d) Commands / workflows | Workflows são configurados via interface de “Memories/Rules \& Workflows”; não há hoje doc oficial de uma pasta `.windsurf/workflows`. Logo, **não tem suporte nativo a pasta de commands/workflows** que você versiona manualmente. [^1_14] |
| e) Config MCP global | Windsurf expõe configuração de MCP apenas pela UI (sem caminho padrão publicado para um `mcp.json` global). Até onde a documentação externa vai, **não há um arquivo de mcp.json global documentado para o usuário editar diretamente**. [^1_11] |


***

## 4. Gemini CLI

Gemini CLI usa uma hierarquia de `GEMINI.md`/`AGENTS.md` por diretório e integra Agent Skills em `.gemini/skills` / `~/.gemini/skills`.[^1_16][^1_17][^1_18]


| Item | Resposta |
| :-- | :-- |
| a) Regras locais (pasta) | **Não tem suporte nativo a pasta de regras.** As instruções locais são arquivos `GEMINI.md` (ou `AGENTS.md`, se você trocar `contextFileName`) no projeto e subpastas, carregados hierarquicamente. [^1_17][^1_16] |
| b) Global rules + limite | Por padrão o global é `~/.gemini/GEMINI.md`. Você pode configurar `~/.gemini/settings.json` para usar `AGENTS.md` ou uma lista como `["AGENTS.md","GEMINI.md"]`. Não há limite de tamanho documentado; efetivamente você é limitado pelo contexto do modelo, então a própria doc recomenda manter o arquivo curto e focado. [^1_16][^1_17][^1_19] |
| c) Pasta de skills | Skills globais: `~/.gemini/skills/<nome>/SKILL.md`. Skills de projeto: `.gemini/skills/<nome>/SKILL.md`. Tanto a codelab oficial quanto o material da especificação Agent Skills mostram esse layout. [^1_20][^1_18][^1_21] |
| d) Commands / workflows | Gemini CLI tem “custom commands” baseados em TOML/config e também permite override de system prompt com `./.gemini/system.md` via `GEMINI_SYSTEM_MD`, mas **não define uma pasta padrão de commands/workflows** análoga a `.opencode/command` ou `.kilocode/workflows`. [^1_22] |
| e) Config MCP global | A doc pública de Gemini CLI fala em “Policy Engine” com políticas em `/etc/gemini-cli/policies` e afins, mas não em um `mcp.json` global específico para MCP; a integração com MCP normalmente é feita por outros hosts (Antigravity, Claude, etc.). Até onde a documentação vai, **não há um arquivo mcp.json global de Gemini CLI para você editar**. [^1_23] |


***

## 5. Codex CLI (OpenAI)

Codex separa três coisas diferentes: AGENTS.md (instruções), `.codex/rules/*.rules` (execpolicy) e skills (`~/.codex/skills` / `.codex/skills`).[^1_24][^1_25][^1_26]


| Item | Resposta |
| :-- | :-- |
| a) Regras locais (pasta) | Para regras de comportamento do agente, Codex usa `AGENTS.md` na raiz do projeto (e em subpastas), **não uma pasta de regras** — então aqui a resposta é “não tem suporte nativo a pasta de regras” no sentido de um `.agents/rules`. O que existe é uma pasta técnica `.codex/rules/` para exec‑policy de comandos (segurança), não para style guide. [^1_27][^1_26][^1_28] |
| b) Global rules + limite | Global instructions em estilo AGENTS ficam em `~/.codex/AGENTS.MD`, servindo como ledger/global rules que valem para todos os projetos. Não há limite de tamanho publicado; o próprio ecossistema AGENTS.md recomenda manter o arquivo enxuto para não estourar contexto. [^1_25][^1_29] |
| c) Pasta de skills | Skills globais: `~/.codex/skills/<skill>/SKILL.md` (há até uma subpasta `.system` com skills internas). Skills de projeto: `.codex/skills/<skill>/SKILL.md`. Codex descobre qualquer pasta nesse tree que contenha `SKILL.md`. [^1_30][^1_25][^1_24][^1_31] |
| d) Commands / workflows | Codex não tem hoje uma pasta “commands/workflows” ao estilo `.opencode/command` ou `.kilocode/workflows`. Workflows persistentes aparecem como planos (`plans.md`, ExecPlans) ou prompts compartilhados, armazenados fora de uma convenção única de diretório. Portanto, **não tem suporte nativo a pasta de commands/workflows**. [^1_32][^1_33] |
| e) Config MCP global | Codex CLI pode atuar como host MCP, mas a configuração de servidores MCP é feita seguindo guias genéricos de MCP e não expõe (na doc pública) um `mcp.json` global padronizado como em Cursor ou Claude Desktop. Na prática você configura MCP por host (Claude Desktop, Cursor, etc.), não via um mcp.json do próprio Codex. [^1_26][^1_13] |


***

## 6. Claude Code

Claude Code usa CLAUDE.md, uma pasta de rules opcional e Agent Skills via `.claude/skills` / `~/.claude/skills`, além de comandos em `.claude/commands`.[^1_34][^1_35][^1_36]


| Item | Resposta |
| :-- | :-- |
| a) Regras locais (pasta) | Além do `CLAUDE.md` na raiz, Claude Code suporta uma pasta `.claude/rules/*.md` para regras mais granulares por tarefa/pasta; é exatamente o “rules folder” local. [^1_34] |
| b) Global rules + limite | Global rules ficam em `~/.claude/CLAUDE.md`. A própria Anthropic e blogs recomendam mantê‑lo curto e de alto nível, mas não existe um limite oficial de caracteres; o limite real é o contexto do modelo. [^1_34][^1_37][^1_38] |
| c) Pasta de skills | Skills globais: `~/.claude/skills/<nome>/SKILL.md`. Skills de projeto: `.claude/skills/<nome>/SKILL.md`. Claude Code segue a especificação Agent Skills, e esses paths são os canônicos. [^1_36][^1_12] |
| d) Commands / workflows | Slash‑commands personalizados são arquivos markdown em `.claude/commands/<nome>.md` (ou `.mm`), que viram `/nome` no chat. Workflows mais complexos muitas vezes são codificados como combinações de commands + skills; não há uma pasta separada só para “workflows”. [^1_35] |
| e) Config MCP global | Configuração global de MCP servers fica em `~/.claude.json` (campo `mcpServers`), com overrides por projeto em `.mcp.json` na raiz. Há ainda `managed-mcp.json` em diretórios de sistema para configurações gerenciadas por IT. [^1_39][^1_40] |


***

## 7. OpenCode (opencode)

OpenCode adota AGENTS.md/CLAUDE.md para rules, Agent Skills para skills, e tem pastas bem definidas para commands e config MCP.[^1_41][^1_42][^1_43][^1_44][^1_45]


| Item | Resposta |
| :-- | :-- |
| a) Regras locais (pasta) | Para regras de comportamento, OpenCode usa `AGENTS.md` no projeto (ou `CLAUDE.md` como fallback). Não existe hoje uma pasta “.opencode/rules”; instruções extras são referenciadas em `opencode.json`. Então, **não tem suporte nativo a pasta de regras** — o pivot é AGENTS.md mesmo. [^1_43][^1_42] |
| b) Global rules + limite | Global rules: `~/.config/opencode/AGENTS.md`. Se esse arquivo não existir, ele pode cair no fallback `~/.claude/CLAUDE.md`. Não há limite de tamanho formal; a recomendação é manter AGENTS.md pequeno para não consumir muito contexto. [^1_43][^1_42] |
| c) Pasta de skills | Skills de projeto: `.opencode/skills/<nome>/SKILL.md`. Skills globais: `~/.config/opencode/skills/<nome>/SKILL.md`. Além disso, o loader também lê `.agents/skills` e `.claude/skills` (e equivalentes globais) para interoperar com outros agentes. [^1_41][^1_46] |
| d) Commands / workflows | Commands globais: `~/.config/opencode/command/<nome>.md`. Commands de projeto: `.opencode/command/<nome>.md`. (Nota: o nome correto é `command/`, no singular; diretórios `commands/` dão erro.) Esses arquivos definem slash‑commands como `/test`, `/review`, etc. [^1_44][^1_47][^1_48] |
| e) Config MCP global | MCP servers são definidos no config JSON do OpenCode, tipicamente `~/.config/opencode/opencode.json` (ou `config.json`/`opencode.jsonc` conforme a versão). Dentro dele, o campo `mcp` lista os servidores locais/remotos. [^1_45][^1_49][^1_50] |


***

## 8. Kilo Code

Kilo Code hoje concentra “regras” em skills e workflows; a doc pública é bem explícita sobre skills e workflows, mas não publica um padrão de pasta “rules” separado como AGENTS.md.[^1_51][^1_52][^1_53][^1_54][^1_55]


| Item | Resposta |
| :-- | :-- |
| a) Regras locais (pasta) | A documentação atual fala em modos, skills e workflows, mas **não define uma pasta dedicada de regras no estilo `.agents/rules`**; as instruções persistentes costumam ir para skills (`.kilocode/skills`) ou para arquivos de modo/launchConfig. Então aqui a resposta é “não tem suporte nativo a pasta de regras”. [^1_51][^1_56] |
| b) Global rules + limite | Em vez de um `GEMINI.md`/`CLAUDE.md` global, Kilo usa global skills (`~/.kilocode/skills/`) e settings da extensão/CLI. Para skills, o frontmatter `description` é limitado a 1024 caracteres, mas não há limite rígido para o corpo; de novo, o gargalo real é o contexto do modelo. [^1_51][^1_52] |
| c) Pasta de skills | Skills globais: `~/.kilocode/skills/<nome>/SKILL.md` (e variações específicas por modo como `~/.kilocode/skills-code/`). Skills de projeto: `.kilocode/skills/<nome>/SKILL.md` (+ `skills-code/`, `skills-architect/` etc.). [^1_51][^1_52][^1_57] |
| d) Commands / workflows | Workflows globais: `~/.kilocode/workflows/*.md`. Workflows de projeto: `[projeto]/.kilocode/workflows/*.md`. Cada arquivo `.md` é disparado com `/nome-do-arquivo.md` no chat. [^1_58][^1_53][^1_59] |
| e) Config MCP global | Para a extensão VS Code, o config global de MCP fica em um `mcp_settings.json` embaixo do diretório de settings do Kilo (por exemplo `~/.config/Code/User/globalStorage/kilocode.kilo-code/settings/mcp_settings.json`), acessível via UI em “Settings → MCP Servers → Edit Global MCP”. Para o **CLI**, o arquivo recomendado é `~/.config/kilo/kilo.json` (campo `mcp`), com override por projeto em `./kilo.json` ou `./.kilo/kilo.json`. [^1_54][^1_60][^1_55] |


***

## 9. Factory Droid CLI (Factory.ai)

Factory foca em AGENTS.md e “droids” como sub‑agentes; há menos documentação pública sobre Agent Skills/MCP do próprio CLI, então alguns pontos abaixo são necessariamente mais conservadores.[^1_15][^1_61][^1_62]


| Item | Resposta |
| :-- | :-- |
| a) Regras locais (pasta) | Para regras de projeto, Factory usa `AGENTS.md` na raiz do repo; a própria doc do Factory fala em “Teach agents everything… com um único AGENTS.md”. Não há hoje uma pasta `.factory/rules` documentada para regras de texto — portanto, **não tem suporte nativo a pasta de regras** além do próprio `AGENTS.md`. [^1_61] |
| b) Global rules + limite | Global rules: `~/.factory/AGENTS.md` como override pessoal usado pelos “Droids” em múltiplos projetos. A documentação não publica limite de tamanho; recomenda‑se tratá‑lo como um AGENTS.md global enxuto para não consumir o contexto dos modelos usados pelos droids. [^1_61] |
| c) Pasta de skills | Factory aparece como agente suportado no ecossistema Agent Skills; na prática, skills costumam ser instaladas nos diretórios padrão `~/.agents/skills/<skill>/SKILL.md` (global) e `.agents/skills/<skill>/SKILL.md` (projeto), compartilhados entre vários agentes (Claude Code, Cursor, Codex, Gemini CLI, Kilo, Droids, etc.). Não há hoje uma pasta `~/.factory/skills` oficialmente documentada. [^1_15] |
| d) Commands / workflows | O equivalente de “workflows” em Factory são os **Custom Droids**: droids de projeto em `<repo>/.factory/droids/<nome>.md` e droids pessoais em `~/.factory/droids/<nome>.md`. Cada arquivo define um sub‑agente com prompt, ferramentas e modelo próprios que podem ser chamados pelo Task tool. [^1_63][^1_62] |
| e) Config MCP global | A documentação pública foca no uso de Droids como MCP server para outros hosts, e no consumo de MCP servers via hosts como Claude/Antigravity; não há hoje um `mcp.json`/`mcp_config.json` global do **Droid CLI** exposto para o usuário. Quando você usa Droids via Claude/Antigravity, o arquivo MCP relevante é o desses hosts (`~/.claude.json`, `mcp_config.json` do Antigravity, etc.), não algo específico do Factory. [^1_39][^1_10] |


***

Se quiser, posso montar um “cheat sheet” só com os caminhos que interessam para você (por exemplo, só skills e rules cross‑tool: `.agents/skills`, `.agent/rules`, `AGENTS.md`/`GEMINI.md`/`CLAUDE.md`/`AGENTS.MD`) para você padronizar seus repositórios.
<span style="display:none">[^1_100][^1_101][^1_102][^1_103][^1_104][^1_105][^1_106][^1_107][^1_108][^1_109][^1_110][^1_111][^1_112][^1_113][^1_114][^1_115][^1_116][^1_117][^1_118][^1_119][^1_120][^1_121][^1_122][^1_123][^1_124][^1_125][^1_126][^1_127][^1_128][^1_129][^1_130][^1_131][^1_132][^1_133][^1_134][^1_135][^1_136][^1_137][^1_138][^1_139][^1_140][^1_141][^1_142][^1_143][^1_144][^1_145][^1_146][^1_147][^1_148][^1_149][^1_150][^1_151][^1_152][^1_153][^1_154][^1_155][^1_156][^1_157][^1_158][^1_159][^1_160][^1_161][^1_162][^1_163][^1_164][^1_165][^1_166][^1_167][^1_168][^1_169][^1_170][^1_171][^1_172][^1_173][^1_174][^1_175][^1_176][^1_177][^1_178][^1_179][^1_180][^1_181][^1_182][^1_183][^1_184][^1_185][^1_186][^1_187][^1_188][^1_189][^1_190][^1_191][^1_192][^1_193][^1_194][^1_195][^1_196][^1_197][^1_198][^1_199][^1_200][^1_201][^1_202][^1_203][^1_204][^1_205][^1_206][^1_207][^1_208][^1_209][^1_210][^1_211][^1_212][^1_213][^1_214][^1_215][^1_216][^1_217][^1_218][^1_219][^1_220][^1_221][^1_222][^1_223][^1_224][^1_225][^1_226][^1_227][^1_228][^1_229][^1_230][^1_231][^1_232][^1_233][^1_234][^1_235][^1_236][^1_237][^1_238][^1_239][^1_240][^1_241][^1_242][^1_243][^1_244][^1_245][^1_246][^1_247][^1_248][^1_249][^1_250][^1_251][^1_252][^1_253][^1_254][^1_255][^1_256][^1_257][^1_258][^1_259][^1_260][^1_261][^1_262][^1_263][^1_264][^1_265][^1_266][^1_267][^1_268][^1_269][^1_270][^1_271][^1_272][^1_273][^1_274][^1_275][^1_276][^1_277][^1_278][^1_279][^1_280][^1_281][^1_282][^1_283][^1_284][^1_285][^1_286][^1_287][^1_288][^1_289][^1_290][^1_291][^1_292][^1_293][^1_294][^1_295][^1_296][^1_297][^1_298][^1_299][^1_300][^1_301][^1_302][^1_303][^1_304][^1_305][^1_306][^1_307][^1_308][^1_309][^1_310][^1_311][^1_312][^1_313][^1_314][^1_315][^1_316][^1_317][^1_318][^1_319][^1_320][^1_321][^1_322][^1_323][^1_324][^1_325][^1_326][^1_327][^1_328][^1_329][^1_330][^1_331][^1_332][^1_333][^1_334][^1_335][^1_336][^1_337][^1_338][^1_339][^1_340][^1_341][^1_342][^1_343][^1_344][^1_345][^1_346][^1_347][^1_348][^1_349][^1_350][^1_351][^1_352][^1_353][^1_354][^1_355][^1_356][^1_357][^1_358][^1_359][^1_360][^1_361][^1_362][^1_363][^1_364][^1_365][^1_366][^1_367][^1_368][^1_369][^1_370][^1_371][^1_372][^1_373][^1_374][^1_375][^1_376][^1_377][^1_378][^1_379][^1_380][^1_381][^1_382][^1_383][^1_384][^1_385][^1_386][^1_387][^1_388][^1_389][^1_390][^1_391][^1_392][^1_393][^1_394][^1_395][^1_396][^1_397][^1_398][^1_399][^1_400][^1_401][^1_402][^1_403][^1_404][^1_405][^1_406][^1_407][^1_408][^1_409][^1_410][^1_411][^1_412][^1_413][^1_414][^1_415][^1_416][^1_417][^1_418][^1_419][^1_420][^1_421][^1_422][^1_423][^1_424][^1_425][^1_426][^1_427][^1_428][^1_429][^1_430][^1_431][^1_432][^1_433][^1_434][^1_435][^1_436][^1_437][^1_438][^1_439][^1_440][^1_441][^1_442][^1_443][^1_444][^1_445][^1_446][^1_447][^1_448][^1_449][^1_450][^1_451][^1_452][^1_453][^1_454][^1_455][^1_456][^1_457][^1_458][^1_459][^1_460][^1_461][^1_462][^1_463][^1_464][^1_465][^1_466][^1_64][^1_65][^1_66][^1_67][^1_68][^1_69][^1_70][^1_71][^1_72][^1_73][^1_74][^1_75][^1_76][^1_77][^1_78][^1_79][^1_80][^1_81][^1_82][^1_83][^1_84][^1_85][^1_86][^1_87][^1_88][^1_89][^1_90][^1_91][^1_92][^1_93][^1_94][^1_95][^1_96][^1_97][^1_98][^1_99]</span>

<div align="center">⁂</div>

[^1_1]: https://skly.ai/docs/rules/antigravity

[^1_2]: https://antigravityai.directory/antigravity-file-guide

[^1_3]: https://zenn.dev/imohuke/articles/antigravity-guide-skills-rules

[^1_4]: https://antigravityai.directory/google-antigravity-rules

[^1_5]: https://discuss.ai.google.dev/t/conductor-should-be-integrated-into-antigravity-to-ensure-long-term-context-retention/113384

[^1_6]: https://antigravityai.directory/gemini-md-guide

[^1_7]: https://discuss.ai.google.dev/t/feature-request-ui-to-view-global-skills-in-antigravity-ide/121463

[^1_8]: https://discuss.ai.google.dev/t/bug-report-agent-is-unaware-of-global-skills-due-to-missing-path-in-system-prompt/127260

[^1_9]: https://www.youtube.com/watch?v=TwRPGmBKIY0

[^1_10]: https://firebase.google.com/docs/ai-assistance/mcp-server

[^1_11]: https://github.com/hashiiiii/rules-for-ai

[^1_12]: https://agentskills.me/tool/cursor

[^1_13]: https://gofastmcp.com/integrations/mcp-json-configuration

[^1_14]: https://www.reddit.com/r/windsurf/comments/1n4mk39/comment/nbmg6a6/

[^1_15]: https://github.com/tech-leads-club/agent-skills

[^1_16]: https://note.com/yo4shi80/n/ne49df03f6593

[^1_17]: https://fossies.org/linux/gemini-cli/docs/cli/tutorials/memory-management.md

[^1_18]: https://agentskills.me/tool/gemini-cli

[^1_19]: https://developers.google.com/gemini-code-assist/docs/use-agentic-chat-pair-programmer

[^1_20]: https://codelabs.developers.google.com/gemini-cli/how-to-create-agent-skills-for-gemini-cli

[^1_21]: http://sakananote2.blogspot.com/2026/02/gemini-cli-skill.html

[^1_22]: https://geminicli.com/docs/cli/system-prompt/

[^1_23]: https://geminicli.com/docs/core/policy-engine/

[^1_24]: https://dev.to/proflead/codex-skills-101-build-reusable-ai-workflows-with-skillsmd-42fe

[^1_25]: https://libraries.io/npm/codex-skills

[^1_26]: https://developers.openai.com/codex/rules/

[^1_27]: https://developers.openai.com/codex/rules

[^1_28]: https://www.reddit.com/r/OpenAI/comments/1nk0h0r/how_do_you_use_agentsmd_in_codex_cli_or_vs_code/

[^1_29]: https://developertoolkit.ai/en/codex/quick-start/agents-md/

[^1_30]: https://blog.fsck.com/2025/12/19/codex-skills/

[^1_31]: https://proflead.dev/posts/codex-skills-explained-101/

[^1_32]: https://smartscope.blog/en/generative-ai/chatgpt/codex-plan-mode-complete-guide/

[^1_33]: https://qiita.com/masakinihirota/items/62367ca7ab1766cbd012

[^1_34]: https://codewithmukesh.com/blog/claude-md-mastery-dotnet/

[^1_35]: https://claude.com/blog/using-claude-md-files

[^1_36]: https://www.launchvault.dev/blog/ultimate-guide-agent-skills-claude

[^1_37]: https://www.gend.co/en-ca/blog/customise-claude-code-with-claude-md

[^1_38]: https://joseparreogarcia.substack.com/p/claude-code-memory-explained

[^1_39]: https://code.claude.com/docs/en/mcp

[^1_40]: https://code.claude.com/docs/en/settings

[^1_41]: https://opencode.ai/docs/skills

[^1_42]: https://opencode.ai/docs/rules/

[^1_43]: https://open-code.ai/en/docs/rules

[^1_44]: https://opencode.ai/docs/commands/

[^1_45]: https://opencode.ai/docs/mcp-servers/

[^1_46]: https://www.groff.dev/blog/implementing-claude-md-agent-skills

[^1_47]: https://www.opencodecn.com/docs/commands

[^1_48]: https://github.com/sst/opencode/issues/3240

[^1_49]: https://github.com/anomalyco/opencode/issues/3407

[^1_50]: https://composio.dev/blog/mcp-with-opencode

[^1_51]: https://kilo.ai/docs/customize/skills

[^1_52]: https://blog.kilo.ai/p/ai-agent-workflows-with-skills-md

[^1_53]: https://kilo.ai/docs/customize/workflows

[^1_54]: https://kilocode.ai/docs/features/mcp/using-mcp-in-kilo-code

[^1_55]: https://kilo.ai/docs/automate/mcp/using-in-cli

[^1_56]: https://kilocode.ai/docs/features/auto-launch-configuration

[^1_57]: https://www.linkedin.com/posts/kilo-code_overview-agent-skills-activity-7416897413027774467-HWt1

[^1_58]: https://kilocode.ai/docs/features/slash-commands/workflows

[^1_59]: https://kilocode.ai/docs/zh-CN/features/slash-commands/workflows

[^1_60]: https://github.com/Kilo-Org/kilocode/issues/2291

[^1_61]: https://docs.factory.ai/cli/configuration/agents-md

[^1_62]: https://factory.mintlify.app/cli/configuration/custom-droids

[^1_63]: https://docs.factory.ai/cli/configuration/custom-droids

[^1_64]: https://discuss.ai.google.dev/t/new-folder-for-rules/126165

[^1_65]: https://forum.cursor.com/t/project-level-mcp-json-configuration-not-working-in-windows11/62182

[^1_66]: https://github.com/dyoshikawa/rulesync/blob/main/docs/tools/windsurf.md

[^1_67]: https://www.reddit.com/r/google_antigravity/comments/1poybmm/how_are_you_providing_rules_system_instructions/

[^1_68]: https://docs.omni.co/ai/mcp/cursor

[^1_69]: https://fast.io/resources/windsurf-mcp-setup-guide/

[^1_70]: https://discuss.ai.google.dev/t/new-rule-file-not-loaded-even-after-refresh-and-restart-antigravity/123727

[^1_71]: https://snyk.io/articles/how-to-add-a-new-mcp-server-to-cursor/

[^1_72]: https://docs.windsurf.com/windsurf/cascade/mcp

[^1_73]: https://antigravity.codes/blog/user-rules

[^1_74]: https://natoma.ai/blog/how-to-enabling-mcp-in-cursor

[^1_75]: https://natoma.ai/blog/how-to-enabling-mcp-in-windsurf

[^1_76]: https://www.lanxk.com/posts/google-antigravity-rules/

[^1_77]: https://www.youtube.com/watch?v=xiu1D1bwWp0

[^1_78]: https://docs.windsurf.com/plugins/cascade/mcp

[^1_79]: https://www.reddit.com/r/AntiGravityUsers/comments/1p743pc/antigravity_multifolder_workspace_workflow/

[^1_80]: https://www.youtube.com/watch?v=dprcTRFHPHY

[^1_81]: https://deepwiki.com/study8677/antigravity-workspace-template/6.4-configuring-mcp-servers

[^1_82]: https://www.reddit.com/r/google_antigravity/comments/1rf4599/why_is_there_an_inconsistency_between_the_agent/

[^1_83]: https://www.youtube.com/watch?v=zTPEQX0JrsM

[^1_84]: https://antigravityai.directory/blog/mastering-mcp-servers-google-antigravity-advanced-guide-2025

[^1_85]: https://antigravity.codes/pt/blog/workflows

[^1_86]: https://www.youtube.com/watch?v=jZ8c_OlIc_U

[^1_87]: https://composio.dev/blog/howto-mcp-antigravity

[^1_88]: https://codelabs.developers.google.com/getting-started-google-antigravity

[^1_89]: https://antigravity-kit.vercel.app/docs/workflows

[^1_90]: https://www.reddit.com/r/google_antigravity/comments/1qcq8ay/manually_configuring_mcp_for_antigravity_is_a/

[^1_91]: https://antigravity.codes/blog/workflows

[^1_92]: https://github.com/czlonkowski/n8n-mcp/blob/main/docs/ANTIGRAVITY_SETUP.md

[^1_93]: https://macelabs.com/google-antigravity-agent-workflow-documentation/

[^1_94]: https://codelabs.developers.google.com/getting-started-with-antigravity-skills

[^1_95]: https://voltagent.dev/docs/workspaces/skills/

[^1_96]: https://github.com/rmyndharis/antigravity-skills

[^1_97]: https://www.youtube.com/watch?v=gRAndTHbHWo

[^1_98]: https://www.reddit.com/r/google_antigravity/comments/1qo5u47/antigravity_tip_heres_where_to_put_your_global/

[^1_99]: https://www.stephenwthomas.com/azure-integration-thoughts/agent-skills-antigravity-tutorial/

[^1_100]: https://www.reddit.com/r/google_antigravity/comments/1qvrxxx/how_do_you_actually_set_up_antigravity_agent/

[^1_101]: https://developers.openai.com/codex/skills/

[^1_102]: https://www.youtube.com/watch?v=mWpuvze9V0A

[^1_103]: https://www.youtube.com/watch?v=sjsyKABrDaY

[^1_104]: https://fast-agent.ai/agents/skills/

[^1_105]: https://www.youtube.com/watch?v=5BVjeEZOpzo

[^1_106]: https://www.youtube.com/watch?v=JYsR6pNEma4

[^1_107]: https://code.visualstudio.com/docs/copilot/customization/agent-skills

[^1_108]: https://antigravity.google/docs/skills

[^1_109]: https://ai-learningpath.nstech.com.br/pages/cursor/cursor_custom_instructions.html

[^1_110]: https://cursor.com/changelog/2-4

[^1_111]: https://forum.cursor.com/t/guide-a-simpler-more-autonomous-ai-workflow-for-cursor-new-update/70688

[^1_112]: https://forum.cursor.com/t/how-to-use-project-rules-on-existing-file/130650

[^1_113]: https://forum.cursor.com/t/how-to-use-agent-skills-in-cursor-ide/149860

[^1_114]: https://www.reddit.com/r/ChatGPTCoding/comments/1jiyzro/my_cursor_ai_workflow_that_actually_works/

[^1_115]: https://workos.com/blog/what-are-cursor-rules

[^1_116]: https://www.youtube.com/watch?v=hmdRqZ9UdY8

[^1_117]: https://www.youtube.com/watch?v=y0cAnmkTUzc

[^1_118]: https://cursor101.com/cursor/rules

[^1_119]: https://www.youtube.com/watch?v=khekVi1PK3o

[^1_120]: https://www.reddit.com/r/cursor/comments/1jd4s83/my_cursor_ai_workflow_that_actually_works/

[^1_121]: https://forum.cursor.com/t/scan-for-project-rules-in-subdirectories-of-cursor-rules/61534

[^1_122]: https://cursor.com/blog/agent-best-practices

[^1_123]: https://nmn.gl/blog/cursor-guide

[^1_124]: https://forum.cursor.com/t/in-what-file-on-the-filesystem-are-rules-for-ai-stored/26205

[^1_125]: https://www.youtube.com/watch?v=FpJ48a5S5lU

[^1_126]: https://forum.cursor.com/t/where-are-the-global-rules-saved-in-my-filesystem/76645

[^1_127]: https://deepwiki.com/getcursor/docs/4.3-ai-rules-and-configuration

[^1_128]: https://forum.cursor.com/t/does-cursorrules-file-need-to-be-in-strict-json-format/40974

[^1_129]: https://www.reddit.com/r/cursor/comments/1n28d39/help_setting_global_rules_for_cursor_cli/

[^1_130]: https://dev.to/stamigos/setting-up-cursor-rules-the-complete-guide-to-ai-enhanced-development-24cg

[^1_131]: https://forum.cursor.com/t/global-location-for-project-rules/64109

[^1_132]: https://learncursor.dev/features/rules

[^1_133]: https://forum.cursor.com/t/good-examples-of-cursorrules-file/4346

[^1_134]: https://forum.cursor.com/t/global-cursor-rules-directory/50049

[^1_135]: https://forum.cursor.com/t/theres-no-rules-for-ai-in-my-general-cursor-settings/63575

[^1_136]: https://stevekinney.com/writing/cursor-rules-typescript

[^1_137]: https://www.reddit.com/r/cursor/comments/1m8spzt/global_rules_application/

[^1_138]: https://windsurf.com/university/general-education/creating-modifying-rules

[^1_139]: https://github.com/kinopeee/windsurf-antigravity-rules

[^1_140]: https://www.youtube.com/watch?v=aBNJNPpkOBw

[^1_141]: https://www.reddit.com/r/Codeium/comments/1gsl9cv/rules_for_the_ai_in_windsurf_like_the_cursorrules/

[^1_142]: https://windsurf.run

[^1_143]: https://docs.windsurf.com/windsurf/cascade/skills

[^1_144]: https://docs.windsurf.com/windsurf/cascade/memories

[^1_145]: https://windsurf.com/blog/windsurf-wave-8-cascade-customization-features

[^1_146]: https://www.reddit.com/r/Codeium/comments/1jvk88g/my_windsurf_rules/

[^1_147]: https://dev.to/yardenporat/codium-windsurf-ide-rules-file-1hn9

[^1_148]: https://docs.windsurf.com

[^1_149]: https://docs.moderne.io/user-documentation/moderne-cli/how-to-guides/coding-agent-skills/

[^1_150]: https://www.reddit.com/r/Codeium/comments/1hw6hcz/how_to_write_windsurf_rules_files_for_cascade/

[^1_151]: https://www.adspirer.com/docs/ai-clients/windsurf

[^1_152]: https://github.com/kinopeee/windsurfrules

[^1_153]: https://deepwiki.com/balqaasem/awesome-windsurfrules/2.1-global-rules

[^1_154]: https://www.reddit.com/r/Codeium/comments/1jyfpe6/please_help_cant_edit_global_rules_in_windsurf/

[^1_155]: https://www.reddit.com/r/windsurf/comments/1mbz92z/i_created_a_set_of_global_rules_for_windsurf_to/

[^1_156]: https://github.com/danielrosehill/Windsurf-Global-Rules

[^1_157]: https://github.com/Exafunction/codeium/issues/191

[^1_158]: https://github.com/balqaasem/awesome-windsurfrules

[^1_159]: https://blog.michealwayne.cn/2025/01/19/ai/【调研】AI 编程工具WindSurf使用技巧——WindsurfRules配置/

[^1_160]: https://github.com/vallades/awesome-windsurfrules/blob/main/.windsurfrules

[^1_161]: https://github.com/Exafunction/codeium/issues/195

[^1_162]: https://github.com/ichoosetoaccept/awesome-windsurf

[^1_163]: https://www.reddit.com/r/windsurf/comments/1m6hjhs/this_is_my_global_rulesmd_file_feel_free_to_use/

[^1_164]: https://www.youtube.com/watch?v=D3uuCeOLfJA

[^1_165]: https://codeium.mintlify.app/windsurf/cascade/workflows

[^1_166]: https://www.reddit.com/r/windsurf/comments/1mdsifj/windsurf_best_practices/

[^1_167]: https://alternativeto.net/news/2025/5/windsurf-wave-8-s-second-batch-adds-custom-workflows-and-multitasking-to-cascade/

[^1_168]: https://docs.windsurf.com/windsurf/cascade/workflows

[^1_169]: https://windsurf.com/university/general-education/workflows

[^1_170]: https://www.youtube.com/watch?v=dlovRr5dSTU

[^1_171]: https://www.kzsoftworks.com/blog/windsurf-workflows-from-prompt-chaos-to-productive-focus

[^1_172]: https://campus.datacamp.com/courses/software-development-with-windsurf/building-workflows-with-cascade?ex=10

[^1_173]: https://www.paulmduvall.com/using-windsurf-rules-workflows-and-memories/

[^1_174]: https://www.reddit.com/r/windsurf/comments/1oavtaz/can_i_create_folders_for_projects_and_put/

[^1_175]: https://jcomin.tistory.com/entry/더-이상-반복-작업에-시간-낭비하지-마세요-Windsurf-Cascade-Workflows-완전-정복

[^1_176]: https://www.reddit.com/r/windsurf/comments/1khebco/custom_workflows_automating_repetitive_tasks_in/

[^1_177]: https://www.reddit.com/r/windsurf/comments/1kh61e6/customize_your_cascade/

[^1_178]: https://www.reddit.com/r/windsurf/comments/1m7tee3/automate_your_build_process_with_windsurf/

[^1_179]: https://gemini-cli-docs.pages.dev/tools/mcp-server

[^1_180]: https://blog.milvus.io/ai-quick-reference/where-are-the-gemini-cli-config-files-stored

[^1_181]: https://geminicli.com/docs/cli/skills/

[^1_182]: https://developers.googleblog.com/en/gemini-cli-fastmcp-simplifying-mcp-server-development/

[^1_183]: https://gemini-cli-docs.pages.dev/cli/configuration

[^1_184]: https://damimartinez.github.io/agent-skills-gemini-cli/

[^1_185]: https://codelabs.developers.google.com/cloud-gemini-cli-mcp-go

[^1_186]: https://geminicli.com/docs/cli/trusted-folders/

[^1_187]: https://danicat.dev/posts/agent-skills-gemini-cli/

[^1_188]: https://developers.googleblog.com/gemini-cli-fastmcp-simplifying-mcp-server-development/

[^1_189]: https://milvus.io/ai-quick-reference/where-are-the-gemini-cli-config-files-stored

[^1_190]: https://geminicli.com/docs/cli/tutorials/skills-getting-started/

[^1_191]: https://geminicli.com/docs/tools/mcp-server/

[^1_192]: https://google-gemini.github.io/gemini-cli/docs/cli/trusted-folders.html

[^1_193]: https://www.youtube.com/watch?v=EmmOcrwNX74

[^1_194]: https://geminicli.com/docs/cli/gemini-md/

[^1_195]: https://google-gemini.github.io/gemini-cli/docs/get-started/configuration.html

[^1_196]: https://aruru.co.jp/gemini-character-limit/

[^1_197]: https://google-gemini.github.io/gemini-cli/docs/cli/gemini-md.html

[^1_198]: https://geminicli.com/docs/cli/tutorials/memory-management/

[^1_199]: https://www.reddit.com/r/GoogleGeminiAI/comments/1b2rkqh/what_is_the_character_limit_of_gemini/

[^1_200]: https://www.philschmid.de/gemini-cli-cheatsheet

[^1_201]: https://milvus.io/ai-quick-reference/how-do-i-provide-context-files-to-gemini-cli

[^1_202]: https://www.reddit.com/r/GeminiAI/comments/1lez7m1/so_the_custom_instructions_character_limit_for/

[^1_203]: https://www.reddit.com/r/GeminiCLI/comments/1pefslr/does_gemini_cli_ignores_geminimd_on_purporse/

[^1_204]: https://github.com/google-gemini/gemini-cli/issues/4818

[^1_205]: https://www.reddit.com/r/GeminiAI/comments/1f3sdlm/gemini_gems/

[^1_206]: https://www.youtube.com/watch?v=Od5SlOSlMQo

[^1_207]: https://geminicli.com/docs/reference/configuration/

[^1_208]: https://www.reddit.com/r/google_antigravity/comments/1r5kgl6/great_system_prompt_for_ag_geminimd/

[^1_209]: https://geminicli.com/docs/reference/commands/

[^1_210]: https://codelabs.developers.google.com/gemini-cli-hands-on

[^1_211]: https://docs.countersoft.com/workflows/

[^1_212]: https://layer5.io/blog/ai/streamline-your-gemini-cli-workflow-with-trusted-directories

[^1_213]: https://developers.googleblog.com/tailor-gemini-cli-to-your-workflow-with-hooks/

[^1_214]: https://www.reddit.com/r/AISEOInsider/comments/1ox2kbz/google_gemini_workspace_flows_how_i_automated_my/

[^1_215]: https://geminicli.com/docs/get-started/configuration/

[^1_216]: https://www.reddit.com/r/Bard/comments/1meghqn/i_built_10_gemini_cli_commands_to_automate_my/

[^1_217]: https://workspace.google.com/studio/

[^1_218]: https://www.oreateai.com/blog/how-to-change-gemini-cli-directory/33c3d5157bd0608a0cb698f2a5eefb6c

[^1_219]: https://gemini-cli.org

[^1_220]: https://www.youtube.com/watch?v=0hkcVpfbWfA

[^1_221]: https://github.com/google-gemini/gemini-cli/actions/workflows/ci.yml

[^1_222]: https://geminicli.com/docs/get-started/

[^1_223]: https://www.youtube.com/watch?v=MPZNwk2789w

[^1_224]: https://addyo.substack.com/p/gemini-cli-tips-and-tricks

[^1_225]: https://geminicli.com/docs/cli/custom-commands/

[^1_226]: https://google-gemini.github.io/gemini-cli/docs/cli/commands.html

[^1_227]: https://github.com/google-gemini/gemini-cli

[^1_228]: https://www.reddit.com/r/GeminiCLI/comments/1qxh6k2/best_practices_to_use_gemini_cli_in_a_product_team/

[^1_229]: https://geminicli.com/docs/cli/commands/

[^1_230]: https://gemini-cli.xyz/docs/en/cli/commands

[^1_231]: https://github.com/google-gemini/gemini-cli/issues/4834

[^1_232]: https://developers.google.com/gemini-code-assist/docs/gemini-cli?hl=pt-br

[^1_233]: https://gemini-cli-docs.pages.dev/cli/commands

[^1_234]: https://github.com/openai/codex/blob/main/README.md

[^1_235]: https://github.com/ymichael/open-codex

[^1_236]: https://developers.openai.com/codex/cli/

[^1_237]: https://github.com/codingmoh/open-codex

[^1_238]: https://developers.openai.com/codex/skills

[^1_239]: https://www.reddit.com/r/singularity/comments/1k0qc67/openai_releases_codex_cli_an_ai_coding_assistant/

[^1_240]: https://github.com/feiskyer/codex-settings

[^1_241]: https://github.com/openai/skills

[^1_242]: https://developers.openai.com/codex/cli/features/

[^1_243]: https://developers.openai.com/cookbook/examples/codex/autofix-github-actions/

[^1_244]: https://www.youtube.com/watch?v=en0It1zBjpw

[^1_245]: https://github.com/openai/codex

[^1_246]: https://www.reddit.com/r/programming/comments/1k4piuh/github_opencodex_fully_opensource_commandline_ai/

[^1_247]: https://www.reddit.com/r/codex/comments/1r9cjba/do_agent_skills_actually_work_in_codex/

[^1_248]: https://developers.openai.com/codex/guides/agents-md/

[^1_249]: https://github.com/openai/codex/issues/1624

[^1_250]: https://dot-agents.com

[^1_251]: https://developers.openai.com/codex/guides/agents-md

[^1_252]: https://zenn.dev/yorifuji/articles/3d44ca14ad6b3e?locale=en

[^1_253]: https://www.youtube.com/watch?v=W8I4vk1K72Q

[^1_254]: https://github.com/openai/codex/issues/4354

[^1_255]: https://inventivehq.com/knowledge-base/openai/where-configuration-files-are-stored

[^1_256]: https://www.youtube.com/watch?v=A1wct93Haz4

[^1_257]: https://agentsmd.net

[^1_258]: https://developers.openai.com/codex/cli/reference/

[^1_259]: https://www.reddit.com/r/BlackTemplars/comments/1f1r5gm/with_the_new_imperial_agents_rules_i_decided_to/

[^1_260]: https://www.youtube.com/watch?v=NlNuoH5PPl4

[^1_261]: https://github.com/openai/codex/issues/4765

[^1_262]: https://developers.openai.com/codex/cli/slash-commands/

[^1_263]: https://www.ai-code-training.com/ai/cookbook/custom-commands

[^1_264]: https://developers.openai.com/codex/mcp/

[^1_265]: https://codesignal.com/learn/courses/introduction-to-codex-1/lessons/running-terminal-commands-with-codex

[^1_266]: https://developers.openai.com/codex/custom-prompts/

[^1_267]: https://vladimirsiedykh.com/blog/codex-mcp-config-toml-shared-configuration-cli-vscode-setup-2025

[^1_268]: https://amanhimself.dev/blog/first-few-days-with-codex-cli/

[^1_269]: https://www.youtube.com/watch?v=Ioj-2o3nxnI

[^1_270]: https://www.reddit.com/r/ChatGPTCoding/comments/1n3y2vq/setting_up_mcp_in_codex_is_easy_dont_let_the_toml/

[^1_271]: https://www.youtube.com/watch?v=YKODoUcNbK4

[^1_272]: https://github.com/openai/codex/issues/3441

[^1_273]: https://www.anothercodingblog.com/p/working-with-openais-codex-cli-commands

[^1_274]: https://developers.openai.com/codex/config-basic/

[^1_275]: https://antigravity.codes/pt/blog/user-rules

[^1_276]: https://www.reddit.com/r/cursor/comments/1ia1665/whats_the_difference_between_cursorrules_and/

[^1_277]: https://code.claude.com/docs/en/memory

[^1_278]: https://antigravity-ide.org/prompts

[^1_279]: https://github.com/PatrickJS/awesome-cursorrules

[^1_280]: https://www.reddit.com/r/ClaudeCode/comments/1pius01/claude_rules_clauderules_are_here/

[^1_281]: https://zenn.dev/tmasuyama1114/articles/claude_code_dynamic_rules?locale=en

[^1_282]: https://www.reddit.com/r/google_antigravity/comments/1poybmm/how_are_you_providing_rules_system_instructions/nuipy3e/

[^1_283]: https://code.claude.com/docs/en/best-practices

[^1_284]: https://www.youtube.com/watch?v=TVRoodzA1DE

[^1_285]: https://forum.cursor.com/t/make-rules-folder-configurable/49025

[^1_286]: https://www.reddit.com/r/ClaudeAI/comments/1km9hhp/latest_rules_for_claude_code/

[^1_287]: https://www.youtube.com/watch?v=FVwIgc5IiBE

[^1_288]: https://atamel.dev/posts/2025/11-25_customize_antigravity_rules_workflows/

[^1_289]: https://www.aitot.net/blog/tuy-chinh-google-antigravity-voi-rules-va-workflows

[^1_290]: https://github.com/study8677/antigravity-workspace-template

[^1_291]: https://www.reddit.com/r/google_antigravity/comments/1q9jjhi/how_do_you_use_something_like_rulesmd_in/nyvmxfh/

[^1_292]: https://www.youtube.com/watch?v=7tzgiTAxjjI

[^1_293]: https://antigravity.google/docs/rules-workflows

[^1_294]: https://www.reddit.com/r/google_antigravity/comments/1prpevi/antigravity_and_the_power_of_meta_prompting_rules/

[^1_295]: https://antigravity.google/docs/workspaces

[^1_296]: https://www.linkedin.com/posts/crispincourtenay_i-was-having-an-issue-with-google-antigravity-activity-7429418087277391872-i1ct

[^1_297]: https://vertu.com/lifestyle/the-58-skill-power-pack-for-google-antigravity-transforming-ai-into-a-full-stack-team/

[^1_298]: https://github.com/sickn33/antigravity-awesome-skills

[^1_299]: https://codelabs.developers.google.com/getting-started-with-antigravity-skills?hl=en

[^1_300]: https://www.reddit.com/r/google_antigravity/comments/1qcuc8u/i_aggregated_58_skills_for_antigravity_into_one/

[^1_301]: https://www.youtube.com/watch?v=tdzFX2u3dgA

[^1_302]: https://www.linkedin.com/posts/iromin_tutorial-getting-started-with-antigravity-activity-7417162852693721088-vkcD

[^1_303]: https://www.youtube.com/watch?v=4mnP1lRdUm8

[^1_304]: https://vertu.com/lifestyle/mastering-google-antigravity-skills-the-ultimate-guide-to-extending-agentic-ai-in-2026/

[^1_305]: https://www.antigravityskills.org

[^1_306]: https://www.youtube.com/watch?v=xlM1kYfpOnA

[^1_307]: https://www.reddit.com/r/google_antigravity/comments/1qn48a0/antigravity_global_skills_configuration_where_is/

[^1_308]: https://yuv.ai/learn/opencode-cli

[^1_309]: https://kilocode.ai/docs/advanced-usage/custom-rules

[^1_310]: https://open-code.ai/zh/docs/skills

[^1_311]: https://docs.z.ai/devpack/tool/opencode

[^1_312]: https://kilo.ai/docs/code-with-ai/platforms/cli

[^1_313]: https://opencode.ai/docs/skills/

[^1_314]: https://www.youtube.com/watch?v=YLNAp4_AUpo

[^1_315]: https://kilo.ai/docs/zh-CN/cli

[^1_316]: https://opencode.ai/docs/

[^1_317]: https://kilo.ai/docs/customize/custom-rules

[^1_318]: https://open-code.ai/en/docs/skills

[^1_319]: https://www.youtube.com/watch?v=ipY_e9sldFM

[^1_320]: https://kilo.ai/docs

[^1_321]: https://www.reddit.com/r/opencodeCLI/comments/1rbgshz/global_rules_not_applied/

[^1_322]: https://github.com/sst/opencode/issues/1906

[^1_323]: https://www.reddit.com/r/opencodeCLI/comments/1q9urb2/does_opencode_support_claudemd_files/nyy1dmd/

[^1_324]: https://github.com/frap129/opencode-rules

[^1_325]: https://opencode.ai/docs/agents/

[^1_326]: https://suzumiyaaoba.com/en/blog/post/2025-09-16-agents-md/

[^1_327]: https://libraries.io/npm/opencode-rules

[^1_328]: https://www.opencodecn.com/docs/rules

[^1_329]: https://opencode.ai/docs/permissions/

[^1_330]: https://www.reddit.com/r/ClaudeCode/comments/1rdnlkj/agentsmdclaudemd_comparison/

[^1_331]: https://open-code.ai/en/docs/permissions

[^1_332]: https://www.reddit.com/r/opencodeCLI/comments/1qkh19k/commands_skills_and_agents_in_opencode_whats_the/

[^1_333]: https://github.com/javierr33/opencode-workflow

[^1_334]: https://milvus.io/ai-quick-reference/what-commands-are-essential-for-using-opencode

[^1_335]: https://www.youtube.com/watch?v=0pL5kHbXk2M

[^1_336]: https://www.youtube.com/watch?v=K3kN-2j_isc

[^1_337]: https://www.neilpatterson.dev/writing/opencode-ai-development-workflow-guide

[^1_338]: https://www.youtube.com/watch?v=EOIzFMdmox8

[^1_339]: https://opencodeguide.com/en/cli-commands/

[^1_340]: https://www.opencodecn.com/docs/cli

[^1_341]: https://dev.to/kevinl/opencode-tools-commands-agents-y-workflows-i29

[^1_342]: https://www.opencodecn.com/docs/mcp-servers

[^1_343]: https://opencodeguide.com/en/mcp/

[^1_344]: https://opencodeguide.com/en/mcp-configuration/

[^1_345]: https://opencode.ai/docs/tools/

[^1_346]: https://opencodeguide.com/en/cli-mcp

[^1_347]: https://github.com/opencode-ai/opencode

[^1_348]: https://github.com/modelcontextprotocol

[^1_349]: https://opencode.ai/docs/mcp-servers

[^1_350]: https://www.opencode.live/ecosystem/mcp-servers/

[^1_351]: https://opencode-tutorial.com/en/plugins

[^1_352]: https://appwrite.io/docs/tooling/mcp/opencode

[^1_353]: https://github.com/nosolosoft/opencode-mcp

[^1_354]: https://github.com/lightrao/kiloSkillTest

[^1_355]: https://www.reddit.com/r/kilocode/comments/1r5cigr/difference_between_skills_and_agents/

[^1_356]: https://kilo.ai/features/skills

[^1_357]: https://www.youtube.com/watch?v=-_WY6q3QmWU

[^1_358]: https://atbug.com/agent-skills-reusable-ecosystem-for-ai-agents/

[^1_359]: https://github.com/Kilo-Org/kilocode/discussions/4604

[^1_360]: https://libraries.io/npm/skillsmgr

[^1_361]: https://www.linkedin.com/posts/kilo-code_stop-re-explaining-workflows-to-your-ai-agent-activity-7420178830864228352-1DDt

[^1_362]: https://github.com/Kilo-Org/kilocode/issues/5408

[^1_363]: https://www.reddit.com/r/kilocode/comments/1oi3ufm/openskills_cli_use_claude_code_skills_with_any/

[^1_364]: https://www.youtube.com/watch?v=Fh-aBKrG5CI

[^1_365]: https://kilo.ai/docs/automate/tools/execute-command

[^1_366]: https://kilocode.ai/docs/features/tools/execute-command

[^1_367]: https://github.com/Kilo-Org/kilocode/actions

[^1_368]: https://kilo.ai

[^1_369]: https://www.youtube.com/watch?v=CZinsMO9tKI

[^1_370]: https://www.youtube.com/watch?v=AgMNjX9_AFE

[^1_371]: https://www.reddit.com/r/kilocode/comments/1l25hjz/comment/mvxc2rp/

[^1_372]: https://www.youtube.com/watch?v=mbwfduzv0qw

[^1_373]: https://www.reddit.com/r/kilocode/comments/1l25hjz/how_to_have_workflows_globally_vs_code_level/

[^1_374]: https://kilo.ai/cli

[^1_375]: https://kilo.ai/docs/automate/mcp/using-in-kilo-code

[^1_376]: https://kilo.ai/docs/automate/tools/use-mcp-tool

[^1_377]: https://www.youtube.com/watch?v=w67eZrzrsU8

[^1_378]: https://github.com/ashishpatel26/Kubernetes-mcp-in-kilocode

[^1_379]: https://www.youtube.com/watch?v=egXvZ7_hEAI

[^1_380]: https://blog.guillaumea.fr/post/configuring-terraform-mcp-server-kilo-code/

[^1_381]: https://www.youtube.com/watch?v=w67eZrzrsU8\&vl=en

[^1_382]: https://deepwiki.com/Kilo-Org/kilocode/2.6-model-context-protocol-(mcp)-integration

[^1_383]: https://kilo.ai/docs/automate/mcp/overview

[^1_384]: https://www.youtube.com/watch?v=w67eZrzrsU8\&vl=pt-BR

[^1_385]: https://fault-project.com/how-to/agent/mcp-server-configuration/

[^1_386]: https://kiro.dev/docs/mcp/

[^1_387]: https://github.com/SchneiderSam/awesome-windsurfrules/blob/main/.windsurfrules

[^1_388]: https://github.com/grapeot/devin.cursorrules/blob/master/.windsurfrules

[^1_389]: https://agents.md

[^1_390]: https://skillmd.ai/tutorials/run-on/cursor-ai/creating-skills/

[^1_391]: https://advanced.promo/blog/cursor-skills-guide

[^1_392]: https://agentskills.io/home

[^1_393]: https://aicoding.juejin.cn/post/7593771861324054554

[^1_394]: https://www.infoq.com/news/2026/02/agent-trace-cursor/

[^1_395]: https://cursor.zone/faq/cursor-agent-skills-guide.html

[^1_396]: https://www.youtube.com/watch?v=DfLL5_zbWGc

[^1_397]: https://www.reddit.com/r/cursor/comments/1qodj1w/why_my_agents_skills_are_not_working_in_cursor/o48mq19/

[^1_398]: https://libraries.io/npm/@localsummer%2Fcursor-skills

[^1_399]: https://www.reddit.com/r/GeminiCLI/comments/1mr0f86/my_geminicli_setup/

[^1_400]: https://geminicli.com/docs/core/remote-agents/

[^1_401]: https://gist.github.com/intellectronica/b97f4cc482dd2c22d0646b48c4d3abbc

[^1_402]: https://github.com/google-gemini/gemini-skills

[^1_403]: https://www.workspaceskills.com/gemini

[^1_404]: https://ai.google.dev/gemini-api/docs/coding-agents

[^1_405]: https://www.youtube.com/watch?v=AAbSOnAY07o

[^1_406]: https://www.skills.google

[^1_407]: https://design.dev/ai/gemini-skills-generator/

[^1_408]: https://geminicli.com/docs/cli/creating-skills/

[^1_409]: https://github.com/google-gemini/gemini-skills/blob/main/skills/gemini-api-dev/SKILL.md

[^1_410]: https://github.com/google-gemini/gemini-cli/discussions/16084

[^1_411]: https://codelabs.developers.google.com/gemini-cli/how-to-create-agent-skills-for-gemini-cli?hl=th

[^1_412]: https://www.reddit.com/r/GeminiCLI/comments/1qgitn2/experimentalskills_why_use_a_skillmd_when_i_have/

[^1_413]: https://www.reddit.com/r/GeminiAI/comments/1qg7nxi/antigravity_skill_registry/

[^1_414]: https://www.youtube.com/watch?v=72AXWbg1uKo

[^1_415]: https://www.youtube.com/watch?v=T5LHXiTncp0

[^1_416]: https://www.reddit.com/r/google_antigravity/comments/1qkf52l/skills_not_working_on_antigravity/

[^1_417]: https://www.reddit.com/r/google_antigravity/comments/1qn742a/geminimd_claudemd/

[^1_418]: https://www.reddit.com/r/AntiGravityUsers/comments/1pgfwt6/antigravitys_geminimd_file/

[^1_419]: https://aiengineerguide.com/blog/make-antigravity-use-agents-md-automatically/

[^1_420]: https://www.reddit.com/r/GoogleAntigravityIDE/comments/1pgf6dt/antigravitys_geminimd_file/

[^1_421]: https://open-vsx.org/extension/ChronicleCore/antigravity-skills-chronicle

[^1_422]: https://www.reddit.com/r/GoogleAntigravityIDE/comments/1qasji1/gemini_rules_in_antigravity/

[^1_423]: https://x.com/xenit_v0/status/2001677877062840594

[^1_424]: https://firebase.blog/posts/2025/11/firebase-mcp-and-antigravity

[^1_425]: https://www.youtube.com/watch?v=IxiXRyztN9s

[^1_426]: https://www.youtube.com/watch?v=XdgzDQ6cAKs

[^1_427]: https://antigravity.codes/mcp/json-2

[^1_428]: https://www.youtube.com/watch?v=yJBm6xdWt_I

[^1_429]: https://antigravity.google/docs/mcp

[^1_430]: https://www.reddit.com/r/google_antigravity/comments/1ptnd90/anyone_got_tips_tricks_hacks_to_actually_enjoy/

[^1_431]: https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview

[^1_432]: https://www.reddit.com/r/ClaudeAI/comments/1mrr3nm/whats_in_your_global_claudeclaudemd_share_your/

[^1_433]: https://skillsdir.dev

[^1_434]: https://joecotellese.com/posts/claude-code-global-configuration/

[^1_435]: https://www.nathanonn.com/how-to-build-comprehensive-project-rules-with-claude-code/

[^1_436]: https://www.builder.io/blog/claude-md-guide

[^1_437]: https://code.claude.com/docs/en/skills

[^1_438]: https://stevekinney.com/courses/ai-development/claude-dot-md

[^1_439]: https://mcpmarket.com/tools/skills

[^1_440]: https://github.com/zilliztech/claude-context

[^1_441]: https://www.reddit.com/r/ClaudeAI/comments/1lm7fbc/claude_code_where_is_my_mcp_configuration_stored/

[^1_442]: https://github.com/anthropics/claude-code/issues/5037

[^1_443]: https://www.codecademy.com/article/how-to-use-model-context-protocol-mcp-with-claude-step-by-step-guide-with-examples

[^1_444]: https://codestop.com/articles/view/108

[^1_445]: https://institute.sfeir.com/fr/claude-code/claude-code-mcp-model-context-protocol/

[^1_446]: https://www.weavely.ai/blog/claude-mcp

[^1_447]: https://www.reddit.com/r/ClaudeAI/comments/1kx63xd/how_do_i_add_an_mcp_server_to_claude_code/

[^1_448]: https://institute.sfeir.com/fr/claude-code/claude-code-mcp-model-context-protocol/tutorial/

[^1_449]: https://scottspence.com/posts/configuring-mcp-tools-in-claude-code

[^1_450]: https://github.com/anthropics/claude-code/issues/7936

[^1_451]: https://www.youtube.com/watch?v=X7lgIa6guKg

[^1_452]: https://www.youtube.com/watch?v=d3Ydt6LyGeY

[^1_453]: https://github.com/openai/codex/blob/-/AGENTS.md

[^1_454]: https://github.com/skills-directory/skill-codex

[^1_455]: https://www.youtube.com/watch?v=NlNuoH5PPl4\&vl=pt-BR

[^1_456]: https://zenn.dev/kohei_miki_im8/articles/509707dd64a868

[^1_457]: https://www.reddit.com/r/Warhammer40k/comments/1qhjkvy/what_are_codexs_for/

[^1_458]: https://github.com/ComposioHQ/awesome-codex-skills

[^1_459]: https://fossies.org/linux/codex-rust/codex-rs/execpolicy/README.md

[^1_460]: https://github.com/github/spec-kit/issues/417

[^1_461]: https://majesticlabs.dev/blog/202509/codex-cli-developer-guide/

[^1_462]: https://codex.packycode.com/docs

[^1_463]: https://lobehub.com/es/skills/melodic-software-claude-code-plugins-codex-cli-docs?activeTab=resources

[^1_464]: https://www.reddit.com/r/codex/comments/1priv8h/new_codex_plan_feature_just_dropped/

[^1_465]: https://www.nathanonn.com/the-latest-codex-cli-commands-that-will-save-your-sanity-and-your-rate-limits/

[^1_466]: https://fossies.org/linux/codex-rust/docs/execpolicy.md


---

# verifique / recheque pfvr os pontos 8.a b c só, especificamente. parece ter havido uma mistura de global rules com skill principalmente em 8b

Você tem toda razão, peço desculpas pela confusão. Eu acabei misturando as novidades recentes de "Skills" do Kilo Code com o sistema nativo de regras dele, ignorando a estrutura de pastas dedicada que a ferramenta possui.

Aqui está a correção exata e verificada para os pontos **8.a**, **8.b** e **8.c** do **Kilo Code**:

### 8. Kilo Code (Corrigido)

Diferente de ferramentas que usam um único arquivo `AGENTS.md` ou `CLAUDE.md`, o Kilo Code possui um sistema de Custom Rules muito bem estruturado em diretórios, além do sistema de Skills.


| Item | Resposta |
| :-- | :-- |
| **a) Regras locais (pasta)** | **Existe sim uma pasta nativa.** As regras de projeto ficam no diretório `.kilocode/rules/` [^2_1]. Você pode criar vários arquivos `.md` lá dentro (ex: `formatting.md`, `stack.md`). O Kilo Code também suporta regras específicas por "modo" usando pastas com o sufixo do modo, como `.kilocode/rules-code/` ou `.kilocode/rules-architect/` [^2_1]. <br><br>*(Nota: arquivos antigos únicos como `.kilocoderules`, `.clinerules` e `.roorules` são lidos como fallback legado, mas a documentação oficial crava o uso da pasta `rules/`)*. |
| **b) Global rules + limite** | **Existe um diretório global de regras.** Em vez de um único arquivo global, as regras globais ficam na pasta `~/.kilocode/rules/` [^2_1]. Qualquer arquivo markdown colocado lá é carregado globalmente e mesclado com as regras do projeto ativo (sendo que as regras de projeto têm prioridade em caso de conflito) [^2_1]. O Kilo Code não impõe um limite formal de tamanho (bytes/caracteres) para os arquivos de regras, mas a limitação prática continua sendo o limite de janela de contexto do LLM que você configurar nele. |
| **c) Pasta de skills** | O sistema de "Agent Skills" no Kilo Code funciona de forma similar. <br>- **Skills globais:** `~/.kilocode/skills/<nome-da-skill>/SKILL.md`<br>- **Skills de projeto:** `.kilocode/skills/<nome-da-skill>/SKILL.md`<br>Assim como nas regras, o Kilo também suporta pastas específicas de modo para skills, como `~/.kilocode/skills-code/` ou `.kilocode/skills-architect/` para skills que só devem ser ativadas quando o agente estiver operando nesses modos específicos [^2_2]. |

Resumindo: Kilo Code é uma das poucas ferramentas que adota **nativamente** o conceito de ter uma pasta inteira (com múltiplos arquivos) para regras, tanto em nível de repositório quanto em nível global.

Obrigado pelo toque, isso deixa o mapeamento muito mais preciso para os seus repositórios! Se precisar checar mais alguma especificidade, é só avisar.
<span style="display:none">[^2_10][^2_11][^2_12][^2_13][^2_14][^2_15][^2_16][^2_17][^2_18][^2_19][^2_20][^2_3][^2_4][^2_5][^2_6][^2_7][^2_8][^2_9]</span>

<div align="center">⁂</div>

[^2_1]: https://kilo.ai/docs/customize/custom-rules

[^2_2]: https://kilo.ai/docs/customize/skills

[^2_3]: https://github.com/Kilo-Org/kilocode/issues/1404

[^2_4]: https://www.youtube.com/watch?v=Xekmrf0k1a0

[^2_5]: https://www.youtube.com/watch?v=OSlqpKDvAug

[^2_6]: https://www.reddit.com/r/kilocode/comments/1mtyqlh/how_to_make_kilo_code_improve_itself/

[^2_7]: https://www.reddit.com/r/kilocode/comments/1n1or1j/kilo_code_global_rules_is_it_possible_to_apply/

[^2_8]: https://kilo.ai/docs/customize/custom-instructions

[^2_9]: https://kilocode.ai/docs/advanced-usage/custom-rules

[^2_10]: https://www.youtube.com/watch?v=uiyCtXZkJyQ\&vl=pt-BR

[^2_11]: https://www.scribd.com/document/991599853/Custom-Instructions-Kilo-Code-Docs

[^2_12]: https://github.com/OthmanAdi/planning-with-files/blob/master/docs/kilocode.md

[^2_13]: https://www.reddit.com/r/kilocode/comments/1lq3yt6/claude_code_kilo_code_integration_demo_the_gui/

[^2_14]: https://gitlab.com/soapbox-pub/skills-cli

[^2_15]: https://github.com/Kilo-Org/kilocode/issues/4779

[^2_16]: https://www.linkedin.com/posts/gyaansetu-ai_innovation-ai-productivity-activity-7415038816815767552-GK1D

[^2_17]: https://kilo.ai/features/skills

[^2_18]: https://www.youtube.com/watch?v=cS4vQfX528w

[^2_19]: https://www.linkedin.com/posts/kilo-code_overview-agent-skills-activity-7416897413027774467-HWt1

[^2_20]: https://kilo.ai


---

# perfeito, ultimo pedido - cheque o e) de todos os 9 pfvr menos opencode e kilocode q eu sei q ta certo.

Perfeito, fiz uma varredura rigorosa e específica sobre o **item e) (Arquivo de configuração global do MCP)** para as 7 ferramentas solicitadas.

A primeira resposta foi muito genérica/conservadora nesse ponto para algumas delas (assumindo que a configuração só existia via UI), mas ao verificar a fundo as documentações e repositórios recentes (final de 2025/início de 2026), **todas elas possuem arquivos em disco** muito bem definidos para o MCP.

Aqui está a lista corrigida e verificada:


| Ferramenta | Onde fica o arquivo Global de Configuração do MCP |
| :-- | :-- |
| **1. Antigravity** | O arquivo real se chama **`mcp_config.json`**. <br>- No macOS/Linux, fica em `~/.gemini/antigravity/mcp_config.json` (algumas instalações legacy usam `~/.config/antigravity/mcp.json`). <br>- No Windows, fica em `%USERPROFILE%\.gemini\antigravity\mcp_config.json` (ou em `%APPDATA%\Antigravity\User\mcp.json`) [^3_1][^3_2]. |
| **2. Cursor** | É o arquivo **`mcp.json`**. <br>- No macOS/Linux fica na raiz do diretório de config: `~/.cursor/mcp.json`. (Às vezes gerenciado em `~/Library/Application Support/Cursor/User/mcp.json`). <br>- No Windows: `%USERPROFILE%\.cursor\mcp.json` [^3_3][^3_4]. |
| **3. Windsurf** | Diferente do Cursor, o Windsurf guarda dentro da pasta da Codeium em um arquivo chamado **`mcp_config.json`**. <br>- No macOS/Linux: `~/.codeium/windsurf/mcp_config.json`. <br>- No Windows: `%USERPROFILE%\.codeium\windsurf\mcp_config.json` [^3_5][^3_6]. |
| **4. Gemini CLI** | Não usa um `mcp.json` isolado. A configuração dos servidores MCP fica embutida dentro do arquivo principal de settings, na chave `"mcpServers"`. <br>- Global: **`~/.gemini/settings.json`**. <br>- (Também suporta override local em `.gemini/settings.json`) [^3_7][^3_8]. |
| **5. Codex CLI (OpenAI)** | **Importante:** Codex **não usa JSON**, usa TOML. A configuração global dos servidores fica sob a chave `[mcp_servers.<nome>]`. <br>- Global: **`~/.codex/config.toml`**. <br>- (Também suporta override local no projeto em `.codex/config.toml`) [^3_9][^3_10]. |
| **6. Claude Code** | Como mencionado antes, a config global fica direto na raiz do seu user. <br>- Global: **`~/.claude.json`** (dentro do objeto `"mcpServers"`). <br>- (Localmente em projetos, ele usa um arquivo chamado `.mcp.json`) [^3_11]. |
| **9. Factory Droid CLI** | A documentação da Factory confirma que o CLI gerencia seu próprio arquivo, e diferente dos Droids/AGENTS, a pasta `.factory/` existe sim para guardar a config de MCP. <br>- Global: **`~/.factory/mcp.json`**. <br>- (Local/Projeto: `.factory/mcp.json`) [^3_12][^3_13]. |

Resumindo o padrão da indústria de IAs de código hoje:

- **Cursor e Droid** usam `mcp.json`.
- **Windsurf e Antigravity** preferem `mcp_config.json`.
- **Gemini CLI e Claude Code** embutem a configuração em seus arquivos nativos (`settings.json` e `.claude.json`).
- **Codex** é o ponto fora da curva usando `config.toml`.
<span style="display:none">[^3_14][^3_15][^3_16][^3_17][^3_18][^3_19][^3_20][^3_21][^3_22][^3_23][^3_24][^3_25][^3_26][^3_27][^3_28][^3_29][^3_30]</span>

<div align="center">⁂</div>

[^3_1]: https://www.reddit.com/r/google_antigravity/comments/1qcq8ay/manually_configuring_mcp_for_antigravity_is_a/

[^3_2]: https://x.com/John_Capobianco/status/2005643069828509959

[^3_3]: https://www.mixedbread.com/mcp/integrations/cursor

[^3_4]: https://casdoor.github.io/docs/how-to-connect/mcp/connect-cursor

[^3_5]: https://fast.io/resources/windsurf-mcp-setup-guide/

[^3_6]: https://docs.windsurf.com/windsurf/cascade/mcp

[^3_7]: https://github.com/google-gemini/gemini-cli/blob/main/docs/tools/mcp-server.md

[^3_8]: https://www.braingrid.ai/blog/gemini-mcp

[^3_9]: https://vladimirsiedykh.com/blog/codex-mcp-config-toml-shared-configuration-cli-vscode-setup-2025

[^3_10]: https://developers.openai.com/codex/mcp/

[^3_11]: https://github.com/anthropics/claude-code/issues/5037

[^3_12]: https://www.reddit.com/r/FactoryAi/comments/1obv6pd/how_to_configure_mcp_i_tried_and_didnt_work_also/

[^3_13]: https://docs.factory.ai/cli/configuration/mcp

[^3_14]: https://github.com/czlonkowski/n8n-mcp/blob/main/docs/ANTIGRAVITY_SETUP.md

[^3_15]: https://discuss.ai.google.dev/t/support-for-per-workspace-mcp-config-on-antigravity/111952

[^3_16]: https://x.com/juanjovn/status/1991076747106750791

[^3_17]: https://antigravityai.directory/blog/mastering-mcp-servers-google-antigravity-advanced-guide-2025

[^3_18]: https://codelabs.developers.google.com/cloud-gemini-cli-mcp-go

[^3_19]: https://audrey.feldroy.com/articles/2025-07-27-Gemini-CLI-Settings-With-MCP

[^3_20]: https://firebase.google.com/docs/studio/mcp-servers

[^3_21]: https://geminicli.com/docs/tools/mcp-server/

[^3_22]: https://github.com/kky42/codex-as-mcp

[^3_23]: https://www.reddit.com/r/ChatGPTCoding/comments/1n3y2vq/setting_up_mcp_in_codex_is_easy_dont_let_the_toml/

[^3_24]: https://factory.mintlify.app/cli/configuration/mcp

[^3_25]: https://github.com/iannuttall/droid-factory

[^3_26]: https://docs.sentry.io/ai/mcp/

[^3_27]: https://github.com/microsoft/playwright-mcp

[^3_28]: https://www.npmjs.com/package/@upstash/context7-mcp

[^3_29]: https://www.oreateai.com/blog/unlocking-codex-a-deep-dive-into-configtoml-and-mcp-configuration/08e9aeaa5016dbd3116195e2eea2c589

[^3_30]: https://developers.openai.com/codex/config-reference/

