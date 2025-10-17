"""Autograding script"""

import os


def test_01():
    """Test app"""

    assert os.path.exists("app/inventory.db")
    assert os.path.exists("homework/main.py")
    assert os.path.exists("homework/db_setup.py")
