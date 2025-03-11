from typing import Dict, List, Optional
from ..core.logger import AGILogger
from ..core.config import AGIConfig
from ..atomspace.atom import Atom

class Chatbot:
    def __init__(self, name: str):
        self.logger = AGILogger().get_logger()
        self.config = AGIConfig()
        self.name = name
        self.history: List[Dict[str, str]] = []
        self.logger.info(f"Initialized new Chatbot: {self.name}")

    def process_message(self, message: str) -> str:
        self.logger.debug(f"Processing message: {message}")
        # Add message to history
        self._add_to_history('user', message)
        
        # Generate response
        response = self._generate_response(message)
        
        # Add response to history
        self._add_to_history('bot', response)
        
        return response

    def _add_to_history(self, role: str, content: str):
        if len(self.history) >= self.config.chatbot_config['max_history']:
            self.history.pop(0)
        self.history.append({'role': role, 'content': content})
        self.logger.debug(f"Added to history: {role}: {content}")

    def _generate_response(self, message: str) -> str:
        # Basic echo response for now
        return f"Echo: {message}"

    def get_history(self) -> List[Dict[str, str]]:
        return self.history

    def __repr__(self):
        return f"Chatbot(name={self.name}, history_length={len(self.history)})"
