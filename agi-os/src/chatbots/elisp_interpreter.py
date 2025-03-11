from typing import Any, Dict, List, Optional
from ..core.logger import AGILogger
from ..core.config import AGIConfig
from ..atomspace.atom import Atom

class ElispInterpreter:
    def __init__(self):
        self.logger = AGILogger().get_logger()
        self.config = AGIConfig()
        self.environment: Dict[str, Any] = self._create_initial_environment()
        self.logger.info("Initialized ElispInterpreter")

    def _create_initial_environment(self) -> Dict[str, Any]:
        return {
            'print': self._builtin_print,
            'atom': self._builtin_atom,
            'link': self._builtin_link,
            'get': self._builtin_get
        }

    def evaluate(self, code: str) -> Any:
        try:
            self.logger.debug(f"Evaluating code: {code}")
            # Basic evaluation for now
            if code.startswith('(print '):
                return self._evaluate_print(code)
            elif code.startswith('(atom '):
                return self._evaluate_atom(code)
            else:
                return f"Unknown command: {code}"
        except Exception as e:
            self.logger.error(f"Error evaluating code: {str(e)}")
            return f"Error: {str(e)}"

    def _evaluate_print(self, code: str) -> str:
        content = code[7:-1]  # Extract content between (print ...)
        return str(content)

    def _evaluate_atom(self, code: str) -> Atom:
        atom_type = code[6:-1]  # Extract content between (atom ...)
        return Atom(atom_type, {})

    def _builtin_print(self, *args):
        return ' '.join(str(arg) for arg in args)

    def _builtin_atom(self, atom_type: str) -> Atom:
        return Atom(atom_type, {})

    def _builtin_link(self, atom1: Atom, atom2: Atom) -> bool:
        atom1.add_link(atom2)
        atom2.add_link(atom1)
        return True

    def _builtin_get(self, atom: Atom, key: str) -> Optional[Any]:
        return atom.get_property(key)

    def __repr__(self):
        return f"ElispInterpreter(environment_size={len(self.environment)})"
