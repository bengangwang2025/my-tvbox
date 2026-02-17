import hashlib
import sys
import os
import json
import re

def generate_md5(file_path):
    """
    计算文件的 MD5 值并将其保存到 .md5 文件中
    例如: spider.js -> spider.js.md5
    """
    if not os.path.exists(file_path):
        print(f"Error: File '{file_path}' not found.")
        return

    try:
        # 读取文件内容
        with open(file_path, 'rb') as f:
            content = f.read()
        
        # 计算 MD5
        md5_hash = hashlib.md5(content).hexdigest()
        
        # 输出 MD5 文件
        md5_file_path = file_path + ".md5"
        with open(md5_file_path, 'w') as f:
            f.write(md5_hash)
            
        print(f"Success! Generated MD5 for '{file_path}':")
        print(f"  MD5: {md5_hash}")
        print(f"  Saved to: {md5_file_path}")
        
        # 尝试更新 tvbox_config.json
        config_path = "tvbox_config.json"
        if os.path.exists(config_path):
            try:
                with open(config_path, 'r', encoding='utf-8') as f:
                    config_str = f.read()
                
                # 使用正则替换 spider 字段中的 MD5
                # 匹配模式: "spider": "./index.js;md5;[a-f0-9]{32}" 或类似
                # 这里假设文件名可能不同，但格式固定
                
                filename = os.path.basename(file_path)
                # Remove quotes to match inside the string value (handling ./ prefix)
                pattern = f'{filename};md5;([a-fA-F0-9]+)'
                replacement = f'{filename};md5;{md5_hash}'
                
                if re.search(pattern, config_str):
                    new_config_str = re.sub(pattern, replacement, config_str)
                    with open(config_path, 'w', encoding='utf-8') as f:
                        f.write(new_config_str)
                    print(f"  Updated {config_path} with new MD5.")
                else:
                    print(f"  Warning: Pattern for {filename} not found in {config_path}")
            except Exception as e:
                print(f"  Failed to update config: {e}")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        # Default to index.js if no argument provided
        target_file = "index.js"
    else:
        target_file = sys.argv[1]
        
    print(f"Processing {target_file}...")
    generate_md5(target_file)
