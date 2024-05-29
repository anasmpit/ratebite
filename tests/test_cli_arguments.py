"""
These tests are designed to check the basic functionality of the RateBite CLI tool. They are not full integration or unit tests, but rather minor tests focusing on the CLI flags and commands.

The tests include:
- Checking if the '--help' flag works properly.
- Verifying if the '--version' flag and its alias '-v' work as expected.
- Testing the behavior when using an invalid flag or argument.
- Ensuring that the CLI can run successfully without any arguments.
- Verifying the handling of invalid start date and only end date.
"""

import sys
from pathlib import Path
import pytest
from cli_test_helpers import shell
from src.ratebite.cli import main

def test_help():
    """Can this package run flag --help?"""
    result = shell('python -m src.ratebite --help')
    assert result.exit_code == 0
    # print(result)

def test_version():
    """Can this package run flag --version?"""
    result = shell('python -m src.ratebite --version')
    assert result.exit_code == 0
    # print(result)

def test_version_alias():
    """Can this package run flag -v?"""
    result = shell('python -m src.ratebite -v')
    assert result.exit_code == 0
    # print(result)

def test_cli_wrong_flag():
    """Can this package run wrong flag?"""
    result = shell('python -m src.ratebite -fflag')
    # Invalid usage of some shell built-in command
    assert result.exit_code == 2
    # print(result)

def test_cli_wrong_arguments():
    """Can this package run wrong argument?"""
    result = shell('python -m src.ratebite argumentfff')
    # Invalid usage of some shell built-in command
    assert result.exit_code == 2
    # print(result)

def test_cli_no_arguments():
    """Can this package run flag -v?"""
    result = shell('python -m src.ratebite')
    # Process initialized successfully
    assert result.exit_code == 0
    # print(result)

def test_cli_invalid_start_date():
    """Can this package run flag -v?"""
    result = shell('python -m src.ratebite -s 2550-20-88')
    # Invalid usage of some shell built-in command
    assert result.exit_code == 2
    # print(result)

def test_cli_only_end_date():
    """Can this package run flag -v?"""
    result = shell('python -m src.ratebite -e 2024-05-28')
    # Invalid usage of some shell built-in command
    assert result.exit_code == 2
    # print(result)

# def test_description():
#     """Can this package be run as a Python module?"""
#     result = shell('python -m src.ratebite --description')
#     assert result.exit_code == 0
    # print(result)