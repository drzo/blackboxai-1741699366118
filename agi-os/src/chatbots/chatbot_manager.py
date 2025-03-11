from typing import Dict, List, Optional
from .chatbot_core import Chatbot
from .elisp_interpreter import ElispInterpreter
from ..core.logger import AGILogger
from ..core.config import AGIConfig

class ChatbotManager:
    def __init__(self):
        self.logger = AGILogger().get_logger()
        self.config = AGIConfig()
        self.chatbots: Dict[str, Chatbot] = {}
        self.interpreter = ElispInterpreter()
        self.logger.info("Initialized ChatbotManager")

    def create_chatbot(self, name: str) -> bool:
        if name in self.chatbots:
            self.logger.warning(f"Chatbot {name} already exists")
            return False
        
        self.chatbots[name] = Chatbot(name)
        self.logger.info(f"Created new chatbot: {name}")
        return True

    def get_chatbot(self, name: str) -> Optional[Chatbot]:
        return self.chatbots.get(name)

    def process_message(self, chatbot_name: str, message: str) -> Optional[str]:
        chatbot = self.get_chatbot(chatbot_name)
        if chatbot is None:
            self.logger.error(f"Chatbot {chatbot_name} not found")
            return None
        
        # Check if message is an Elisp command
        if message.startswith('(') and message.endswith(')'):
            try:
                result = self.interpreter.evaluate(message)
                return str(result)
            except Exception as e:
                self.logger.error(f"Error processing Elisp command: {str(e)}")
                return f"Error: {str(e)}"
        
        # Process as regular message
        return chatbot.process_message(message)

    def get_chatbot_history(self, chatbot_name: str) -> Optional[List[Dict[str, str]]]:
        chatbot = self.get_chatbot(chatbot_name)
        if chatbot is None:
            self.logger.error(f"Chatbot {chatbot_name} not found")
            return None
        return chatbot.get_history()

    def __repr__(self):
        return f"ChatbotManager(chatbots={len(self.chatbots)})"
