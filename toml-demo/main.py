# python >= 3.11 标准库自带 tomllib
import tomllib

# 低于3.11 需要安装 uv add toml
# import toml as tomllib
from pprint import pp

# br: binary read
with open("config.toml", "br") as f:
    config = tomllib.load(f)


def main():
    pp(config)


if __name__ == "__main__":
    main()
