from setuptools import setup

setup(
    py_modules=["main", "functions"], # files
    entry_points={
        "console_scripts": [
            "task-cli=main:main", # yupiyo = main.py:function main();
           # yupiyo = python3 main.py 
        ],
    },
)
