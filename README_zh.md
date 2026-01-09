# cookiecutter-python-cli


## 使用

```sh
# Install cookiecutter.
$ pip install --user cookiecutter

# Generate your project template using cookiecutter.
$ cookiecutter gh:cookiecutter-devops/cookiecutter-python-cli
  [1/11] author_name (Someone): hjl
  [2/11] author_email (someone@somewhere.com): 1@1.com
  [3/11] version (0.1.0):
  [4/11] package_name_long (Python CLI Boilerplate): git_demo
  [5/11] package_name (git_demo):
  [6/11] project_name (Awesome CLI): git-demo
  [7/11] project_slug (git_demo):
  [8/11] cli_command (yooucli-name): git_demo
  [9/11] git (y):
  [10/11] dockerfile (y):
  [11/11] open_source_license (MIT license):

$ cd git-demo
$ make venv
$ source venv/bin/activate
$ make install
```

## 运行

```sh
$  git_demo

 Usage: git_demo [OPTIONS] COMMAND [ARGS]...

╭─ Options ────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ --log-level  -l  [DEBUG|INFO|WARNING|ERROR|CRITICAL]  Log level [default: INFO]                                                                                                  │
│ --log-file       FILE                                 Log file                                                                                                                   │
│ --version                                             Show the version and exit.                                                                                                 │
│ --help                                                Show this message and exit.                                                                                                │
╰──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
╭─ Commands ───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ init                 CLI Initialization demo.                                                                                                                                    │
│ show                 Generic sub-command to show a message.                                                                                                                      │
╰──

$ git_demo --log-level=DEBUG show
2026-01-09 16:45:42 INFO     2026-01-09 16:45:42 - git_demo - "/mnt/d/coder/git_demo/git_demo/app.py:31" - cli - INFO - Running git_demo                                   app.py:31
                    DEBUG    2026-01-09 16:45:42 - git_demo - "/mnt/d/coder/git_demo/git_demo/app.py:32" - cli - DEBUG - Debugging infos                                   app.py:32
                     CLI Information
┏━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Feature       ┃ Description                           ┃
┡━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│ Quick Start   │ Get started with your CLI in no time! │
│ Rich Output   │ Beautiful tables and formatting       │
│ Customization │ Easy to extend and modify             │
└───────────────┴───────────────────────────────────────┘
```
