# uv Python 项目

强力推荐 uv！

```bash
# 创建项目
uv init my_project

# 安装依赖
uv add requests

# 运行
uv run main.py

# 从 GitHub 克隆的项目（没有环境），如何初始化？
uv sync

# 安装测试工具，安装完之后直接 pytest 可以使用了
uv tool  install pytest
uv tool uninstall pytest

# 使用临时环境，并在文件中生成依赖信息
uv init --script main.py
# 临时环境运行
uv run main.py
```

uvx 使用临时环境：

```bash
# 在临时环境使用 pytest
uvx pytest
```
