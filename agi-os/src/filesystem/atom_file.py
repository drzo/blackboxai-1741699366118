from typing import Union
from pathlib import Path
from ..atomspace.atom import Atom
from .vfs import VirtualFile
from ..core.logger import AGILogger

class AtomFile(VirtualFile):
    def __init__(self, path: str, atom: Atom):
        super().__init__(path, atom)
        self.logger = AGILogger().get_logger()
        self.logger.debug(f"Created new AtomFile at {path} for atom {atom.atom_type}")

    def read_atom(self) -> Atom:
        if not isinstance(self.content, Atom):
            raise TypeError("File content is not an Atom")
        return self.content

    def write_atom(self, atom: Atom):
        if not isinstance(atom, Atom):
            raise TypeError("Can only write Atom objects to AtomFile")
        self.content = atom
        self.logger.debug(f"Updated AtomFile at {self.path} with new atom {atom.atom_type}")

    def __repr__(self):
        return f"AtomFile(path={self.path}, atom={self.content})"
