"""
Exports for CLI commands.
"""
from {{cookiecutter.project_slug}}.commands.init import init
from {{cookiecutter.project_slug}}.commands.show import show

from rich.console import Console

# 全局唯一Console实例，整个项目共用
# 参数说明：
# color_system="truecolor": 支持真彩色输出，兼容绝大多数现代终端
# force_terminal=False: 非交互式环境（比如输出重定向到文件）时自动关闭颜色控制符，避免乱码
# width=120: 可选，设置终端输出最大宽度，超过自动换行
console = Console(
    color_system="truecolor",
    force_terminal=False,
    # width=120  # 按需开启
)
