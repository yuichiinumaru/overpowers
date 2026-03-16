#!/usr/bin/env python3
"""
飞书文件上传脚本 - 最终版本
支持所有文件类型，自动识别MIME类型
"""

import requests
import json
import os
import sys
import mimetypes

# 配置
APP_ID = os.getenv('FEISHU_APP_ID', 'cli_a9f73f30c4389cd0')
APP_SECRET = os.getenv('FEISHU_APP_SECRET', '60Hd50s39Lt6Q7cmYL36KbWTaTEM1GJn')
RECEIVER = os.getenv('FEISHU_RECEIVER', 'ou_f147879cfc90314f48a26b545dae8ebe')


class FeishuFileUploader:
    def __init__(self, app_id=None, app_secret=None):
        self.app_id = app_id or APP_ID
        self.app_secret = app_secret or APP_SECRET
        self.token = None
        
    def get_token(self):
        """获取访问令牌"""
        resp = requests.post(
            "https://open.feishu.cn/open-apis/auth/v3/tenant_access_token/internal",
            json={"app_id": self.app_id, "app_secret": self.app_secret},
            timeout=10
        )
        result = resp.json()
        
        if result.get('code') != 0:
            raise Exception(f"获取token失败: {result.get('msg')}")
        
        self.token = result.get('tenant_access_token')
        return self.token
    
    def get_mime_type(self, file_path):
        """获取文件MIME类型"""
        mime_type, _ = mimetypes.guess_type(file_path)
        
        # 文件类型映射（飞书支持的类型）
        type_map = {
            'application/pdf': 'pdf',
            'application/msword': 'doc',
            'application/vnd.openxmlformats-officedocument.wordprocessingml.document': 'docx',
            'application/vnd.ms-excel': 'xls',
            'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet': 'xlsx',
            'application/vnd.ms-powerpoint': 'ppt',
            'application/vnd.openxmlformats-officedocument.presentationml.presentation': 'pptx',
            'image/jpeg': 'image',
            'image/png': 'image',
            'image/gif': 'image',
            'image/webp': 'image',
            'audio/mpeg': 'audio',
            'audio/wav': 'audio',
            'audio/aac': 'audio',
            'audio/ogg': 'audio',
            'video/mp4': 'video',
            'video/quicktime': 'video',
            'video/x-msvideo': 'video',
            'application/zip': 'stream',
            'application/x-rar-compressed': 'stream',
            'application/x-7z-compressed': 'stream',
            'text/plain': 'stream',
        }
        
        file_type = type_map.get(mime_type, 'stream')
        
        # 根据扩展名猜测
        if file_type == 'stream':
            ext = os.path.splitext(file_path)[1].lower()
            ext_map = {
                '.pdf': 'pdf',
                '.doc': 'doc',
                '.docx': 'docx',
                '.xls': 'xls',
                '.xlsx': 'xlsx',
                '.ppt': 'ppt',
                '.pptx': 'pptx',
                '.jpg': 'image',
                '.jpeg': 'image',
                '.png': 'image',
                '.gif': 'image',
                '.mp3': 'audio',
                '.wav': 'audio',
                '.aac': 'audio',
                '.ogg': 'audio',
                '.m4a': 'audio',
                '.mp4': 'video',
                '.mov': 'video',
                '.avi': 'video',
                '.mkv': 'video',
                '.zip': 'stream',
                '.rar': 'stream',
                '.7z': 'stream',
                '.tar': 'stream',
                '.gz': 'stream',
                '.txt': 'stream',
                '.md': 'stream',
                '.json': 'stream',
            }
            file_type = ext_map.get(ext, 'stream')
        
        return file_type
    
    def upload_file(self, file_path, file_name=None):
        """上传文件到飞书"""
        if not file_name:
            file_name = os.path.basename(file_path)
        
        if not self.token:
            self.get_token()
        
        file_size = os.path.getsize(file_path)
        file_type = self.get_mime_type(file_path)
        
        print(f"📤 上传文件...")
        print(f"   文件: {file_path}")
        print(f"   文件名: {file_name}")
        print(f"   大小: {file_size:,} bytes")
        print(f"   类型: {file_type}")
        
        headers = {
            "Authorization": f"Bearer {self.token}"
        }
        
        # 准备multipart上传
        files = {
            'file': (file_name, open(file_path, 'rb'), mimetypes.guess_type(file_path)[0] or 'application/octet-stream')
        }
        
        data = {
            'file_name': file_name,
            'file_type': file_type
        }
        
        resp = requests.post(
            "https://open.feishu.cn/open-apis/im/v1/files",
            files=files,
            data=data,
            headers=headers,
            timeout=60
        )
        
        result = resp.json()
        
        if result.get('code') == 0:
            file_key = result.get('data', {}).get('file_key')
            print(f"✅ 上传成功! (file_key: {file_key[:20]}...)")
            return file_key
        else:
            error_msg = result.get('msg', 'Unknown error')
            raise Exception(f"上传失败: {error_msg}")
    
    def send_file_message(self, file_key, file_name, receiver):
        """发送文件消息"""
        if not self.token:
            self.get_token()
        
        headers = {
            "Authorization": f"Bearer {self.token}",
            "Content-Type": "application/json"
        }
        
        # 构建content
        content = {
            "file_key": file_key,
            "file_name": file_name
        }
        
        # 发送消息
        payload = {
            "receive_id": receiver,
            "msg_type": "file",
            "content": json.dumps(content)
        }
        
        print(f"📨 发送消息...")
        print(f"   接收者: {receiver[:20]}...")
        
        resp = requests.post(
            "https://open.feishu.cn/open-apis/im/v1/messages?receive_id_type=open_id",
            headers=headers,
            json=payload,
            timeout=30
        )
        
        result = resp.json()
        
        if result.get('code') == 0:
            message_id = result.get('data', {}).get('message_id')
            print(f"✅ 发送成功! (message_id: {message_id[:20]}...)")
            return message_id
        else:
            error_msg = result.get('msg', 'Unknown error')
            raise Exception(f"发送失败: {error_msg}")


def main():
    if len(sys.argv) < 2:
        print("❌ 用法: python3 feishu_file_upload.py <文件路径> [文件名]")
        print("")
        print("示例:")
        print("  python3 feishu_file_upload.py /path/to/file.pdf")
        print("  python3 feishu_file_upload.py /path/to/file.pdf \"报告.pdf\"")
        sys.exit(1)
    
    file_path = sys.argv[1]
    file_name = sys.argv[2] if len(sys.argv) > 2 else None
    
    if not os.path.exists(file_path):
        print(f"❌ 文件不存在: {file_path}")
        sys.exit(1)
    
    uploader = FeishuFileUploader()
    
    try:
        # 上传文件
        file_key = uploader.upload_file(file_path, file_name)
        
        # 发送消息
        message_id = uploader.send_file_message(
            file_key, 
            file_name or os.path.basename(file_path),
            RECEIVER
        )
        
        print(f"\n✅✅ 全部完成! 消息ID: {message_id}")
        
    except Exception as e:
        print(f"\n❌ 错误: {e}")
        sys.exit(1)


if __name__ == '__main__':
    main()
