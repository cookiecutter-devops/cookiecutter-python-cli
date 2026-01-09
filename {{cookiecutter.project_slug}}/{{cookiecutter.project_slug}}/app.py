"""
Entrypoint for CLI.
"""
import click
import logging
from pathlib import Path
import rich_click as click
from rich.traceback import install
from {{cookiecutter.project_slug}}.commands import init, show
from . import __version__, log

@click.group(context_settings={"auto_envvar_prefix":  "{{cookiecutter.package_name}}"})
@click.option("-l", "--log-level", type=click.Choice(["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"], case_sensitive=False), default="INFO", help="Log level", show_default=True)
@click.option("--log-file", type=click.Path(dir_okay=False, writable=True, path_type=Path), help="Log file")
@click.version_option(__version__)
def cli(log_level, log_file):
    if log_file:
        file_handler = logging.FileHandler(log_file, mode="w")
        formatter = logging.Formatter('%(asctime)s - %(name)s - "%(pathname)s:%(lineno)d" - %(levelname)s - %(message)s',"%Y-%m-%d %H:%M:%S")
        file_handler.setFormatter(formatter)
        log.addHandler(file_handler)

    log.setLevel(log_level)
    if log_level == "DEBUG":
        install(show_locals=True)

    log.info("Running {{cookiecutter.package_name}}")
    log.debug("Debugging infos")


cli.add_command(init)
cli.add_command(show)
