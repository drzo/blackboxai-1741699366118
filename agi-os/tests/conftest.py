import pytest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from src.core.system_manager import SystemManager
from src.core.config import AGIConfig
from src.core.logger import AGILogger

@pytest.fixture
def config():
    return AGIConfig()
