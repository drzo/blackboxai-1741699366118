import pytest
from ..src.chatbots.chatbot_core import Chatbot
from ..src.chatbots.chatbot_manager import ChatbotManager

def test_chatbot_creation():
    chatbot = Chatbot('test_bot')
    assert chatbot.name == 'test_bot'
    assert len(chatbot.get_history()) == 0

def test_chatbot_processing():
    chatbot = Chatbot('test_bot')
    response = chatbot.process_message('test message')
    assert response == 'Echo: test message'
    assert len(chatbot.get_history()) == 2

def test_chatbot_manager():
    manager = ChatbotManager()
    assert manager.create_chatbot('test_bot') == True
    assert manager.create_chatbot('test_bot') == False  # Duplicate
    
    response = manager.process_message('test_bot', 'test message')
    assert response == 'Echo: test message'
    
    history = manager.get_chatbot_history('test_bot')
    assert len(history) == 2
    assert history[0]['role'] == 'user'
    assert history[1]['role'] == 'bot'

def test_elisp_processing():
    manager = ChatbotManager()
    manager.create_chatbot('test_bot')
    
    # Test basic Elisp command
    response = manager.process_message('test_bot', '(print "Hello")')
    assert response == 'Hello'
