from setuptools import setup

setup(
    py_modules=["main", "task_manager"], # files
    entry_points={
        "console_scripts": [
            "task-cli=main:main", # yupiyo = main.py:function main();
           # yupiyo = python3 main.py 
        ],
    },
)
