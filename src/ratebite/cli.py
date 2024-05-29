try:
    import os  # Module for interacting with the operating system
    import json  # Module for working with JSON data
    import typer  # Module for building CLI applications
    import pandas as pd  # Module for data manipulation and analysis
    from pathlib import Path  # Module for representing file paths
    from typing import Optional  # Module for supporting type hints
    from datetime import datetime, timedelta  # Module for datetime operations
    from subprocess import run, CalledProcessError  # Module for running shell commands

    # Print a success message if modules are imported successfully
    # print('Modules imported successfully.')
except ImportError as import_error:
    print(import_error)

from . import __app_name__, __version__, __description__

# Initialize a Typer application instance
app = typer.Typer()

# Define a time format string
time_format = "%Y-%m-%d"

# Get the parent directory of the current script
__parent_dir__ = Path(__file__).parents[1]

def _version_callback(value: bool) -> None:
    """
    Callback function for displaying the application version.

    Args:
        value (bool): Flag indicating whether to display the version.

    Returns:
        None
    """
    if value:
        typer.echo(f"{__app_name__} v{__version__}")
        raise typer.Exit()


def _description_callback(value: bool) -> None:
    """
    Callback function for displaying the application description.

    Args:
        value (bool): Flag indicating whether to display the description.

    Returns:
        None
    """
    if value:
        intro()
        typer.echo(f"{__description__}")
        raise typer.Exit()


def validate_date(date_str: str) -> datetime:
    """
    Function to validate date strings.

    Args:
        date_str (str): Date string to validate.

    Returns:
        datetime: Validated datetime object.

    Raises:
        typer.BadParameter: If the date string is invalid.
    """
    try:
        return datetime.strptime(date_str, time_format)
    except ValueError:
        raise typer.BadParameter(f"Date {date_str} is not in the format YY-mm-dd.")


def intro():
    """
    Function to display introductory text.

    Returns:
        None
    """
    with open(os.path.join(__parent_dir__, "texts", "intro.txt"), encoding='utf-8') as file:
        intro_text = file.read()
    typer.echo(intro_text)


@app.command()
def main(
        start_date: Optional[str] = typer.Option(
            None,
            "-s",
            "--start-date",
            help="Start date for fetching data in YY-mm-dd format."
        ),
        end_date: Optional[str] = typer.Option(
            None,
            "-e",
            "--end-date",
            help="End date for fetching data in YY-mm-dd format."
        ),
        version: Optional[bool] = typer.Option(
            None,
            "--version",
            "-v",
            help="Show the application's version and exit.",
            callback=_version_callback,
            is_eager=True
        ),
        description: Optional[bool] = typer.Option(
            None,
            "--description",
            "-d",
            help="Show the application's description and exit.",
            callback=_description_callback,
            is_eager=True
        ),
) -> None:
    """
    Command function for the main application logic.

    Args:
        start_date (Optional[str]): Start date for fetching data.
        end_date (Optional[str]): End date for fetching data.
        version (Optional[bool]): Flag to display the application's version.
        description (Optional[bool]): Flag to display the application's description.

    Returns:
        None
    """
    current_date = datetime.now().strftime(time_format)
    typer.echo("\n\n----- RageBite Initialize -----\n\n")
    typer.echo(f"Fetching online exchange rates at: {current_date}.\n\n")

    # Validate and use provided dates
    if start_date and end_date:
        start_date = validate_date(start_date).strftime(time_format)
        end_date = validate_date(end_date).strftime(time_format)
        args = [start_date, end_date]
    elif start_date:
        start_date = validate_date(start_date).strftime(time_format)
        args = [start_date, current_date]
    elif end_date:
        raise typer.BadParameter("If only end_date is provided, start_date must also be provided.\n")
    else:
        typer.echo(f"No date provided, current date {current_date} is imported.\n")
        typer.echo("Note: Keep in mind that some online exchange sources have specific policies"
                   "current dates. There may be a need to modify the request or get the latest"
                   "available exchange rate data.\n")
        args = [current_date]

    try:
        run(["python", os.path.join(__parent_dir__, "main.py")] + args, check=True)
    except CalledProcessError as error:
        typer.echo(f"Error occurred while running: {error}", err=True)
        raise typer.Exit(code=1)


if __name__ == "__main__":
    app()
