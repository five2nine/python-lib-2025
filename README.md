# install python package from github

structure

```shell
python-lib-2025/          <-- 프로젝트 루트
├── README.md
├── pyproject.toml
└── mylib/                <-- 패키지명 'mylib'
    ├── __init__.py
    └── mytimer.py
```

pyproject.toml

```toml
[build-system]
requires = ["setuptools>=42", "wheel"]
build-backend = "setuptools.build_meta"

[project]
name = "python-lib"
version = "0.1.0"
description = "My sample timer library"
authors = [{ name = "Your Name", email = "you@example.com" }]
requires-python = ">=3.7"
dependencies = []

[tool.setuptools.packages.find]
where = ["."]
include = ["mylib*"]
```

install

```shell
uv add "python-lib @ git+https://github.com/five2nine/python-lib-2025"
```

usage

```python
from mylib.mytimer import elapsed_timer

@elapsed_timer
def main():
    pass

```
