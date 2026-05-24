"""
CLI initialization command.
"""
import click
from rich.prompt import Prompt
from rich.table import Table

from {{cookiecutter.project_slug}} import console
from {{cookiecutter.project_slug}}.constants import WELCOME_MESSAGE


@click.command()
def init():
    """
    CLI Initialization demo.
    """
    # Create a rich table for the welcome message
    table = Table(title="CLI Initialization")
    table.add_column("Status", style="bold green")
    table.add_column("Message", style="cyan")

    table.add_row("✓", "CLI is initializing...")

    console.print(table)

    Prompt.ask("Press enter to continue")

    # Display welcome message in a table
    welcome_table = Table(title="Welcome")
    welcome_table.add_column("Message", style="bold green")
    welcome_table.add_row(WELCOME_MESSAGE)

    console.print(welcome_table)
