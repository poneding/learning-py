# 临时环境运行（未显示安装依赖）
# uv init --script main.py
# uv run main.py

# /// script
# requires-python = ">=3.10"
# dependencies = ["requests"]
# ///

import requests


def main():
    print(requests.__version__)


if __name__ == "__main__":
    main()
