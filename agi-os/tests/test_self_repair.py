import pytest
from ..src.core.self_assembly import SelfAssembly
from ..src.core.repair_manager import RepairManager

def test_self_assembly():
    assembly = SelfAssembly()
    
    # Test component creation
    assert assembly.create_component('chatbot', {'name': 'test_bot'}) == True
    assert assembly.create_component('chatbot', {'name': 'test_bot'}) == False  # Duplicate
    
    # Test component retrieval
    assert assembly.get_component('chatbot') is not None
    assert assembly.get_component('nonexistent') is None

def test_repair_manager():
    manager = RepairManager()
    
    # Test health check registration
    def mock_check():
        return True
    manager.register_health_check('test_component', mock_check)
    assert 'test_component' in manager.health_checks
    
    # Test health check execution
    assert manager.perform_health_check('test_component') == True
    
    # Test component repair
    assert manager.repair_component('chatbot') == True
    assert manager.repair_component('nonexistent') == False
