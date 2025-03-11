from typing import Dict, List, Optional
from ..core.logger import AGILogger
from ..core.config import AGIConfig
from ..atomspace.atom import Atom

class SelfAssembly:
    def __init__(self):
        self.logger = AGILogger().get_logger()
        self.config = AGIConfig()
        self.components: Dict[str, Any] = {}
        self.logger.info("Initialized SelfAssembly system")

    def create_component(self, component_type: str, config: Dict[str, Any]) -> bool:
        if component_type in self.components:
            self.logger.warning(f"Component {component_type} already exists")
            return False
        
        try:
            # Create new component based on type
            if component_type == 'chatbot':
                from ..chatbots.chatbot_core import Chatbot
                self.components[component_type] = Chatbot(config.get('name', 'default'))
            elif component_type == 'atomspace':
                from ..atomspace.atomspace import AtomSpace
                self.components[component_type] = AtomSpace()
            else:
                self.logger.error(f"Unknown component type: {component_type}")
                return False
            
            self.logger.info(f"Created new component: {component_type}")
            return True
        except Exception as e:
            self.logger.error(f"Failed to create component {component_type}: {str(e)}")
            return False

    def get_component(self, component_type: str) -> Optional[Any]:
        return self.components.get(component_type)

    def __repr__(self):
        return f"SelfAssembly(components={len(self.components)})"
