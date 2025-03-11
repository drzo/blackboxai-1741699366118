import pytest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from src.core.system_manager import SystemManager

def test_system_manager_initialization():
    manager = SystemManager()
    assert manager is not None
