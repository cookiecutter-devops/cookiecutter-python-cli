"""
Show command for the CLI.
"""
import click
from rich.table import Table

from git_demo import console


@click.command()
def show():
    """
    Generic sub-command to show a message.
    """
    # Create a rich table to display the message
    table = Table(title="CLI Information")
    table.add_column("Feature", style="bold blue")
    table.add_column("Description", style="cyan")

    table.add_row("Quick Start", "Get started with your CLI in no time!")
    table.add_row("Rich Output", "Beautiful tables and formatting")
    table.add_row("Customization", "Easy to extend and modify")

    console.print(table)
