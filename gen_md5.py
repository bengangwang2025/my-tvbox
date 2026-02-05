import hashlib
import sys
import os

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
