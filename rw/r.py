from pathlib import Path

path = Path("test.txt")
content = path.read_text()
print(content)


try:
    path = Path("test_not_exist.txt")
    content = path.read_text()
    print(content)
except FileNotFoundError:
    print("未找到 'test.txt' 文件")
