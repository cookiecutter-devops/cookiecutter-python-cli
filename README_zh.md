# cookiecutter-python-cli


## 使用

```sh
# Install cookiecutter.
$ pip install --user cookiecutter

# Generate your project template using cookiecutter.
$ cookiecutter gh:cookiecutter-devops/cookiecutter-python-cli
  [1/5] project_name (Awesome CLI): git-demo
  [2/5] project_slug (git_demo):
  [3/5] cli_command (yocli): git_demo
  [4/5] author (Yankee Maharjan):
  [5/5] description (This CLI tool does awesome things.):

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
