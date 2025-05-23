# 常规 Python 项目

```bash
mkdir my_project && cd my_project

# 手动创建项目基础文件
touch README.md .gitignore main.py

# 创建虚拟环境
python -m venv .venv
source .venv/bin/activate

# 安装依赖
pip install requests

# 导出到 requirements.txt，每次新安装依赖后都需要重新导出
pip freeze > requirements txt

# 退出并删除环境
deactivate
rm -rf .venv
```
