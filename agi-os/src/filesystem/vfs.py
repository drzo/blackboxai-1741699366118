from typing import Dict, List, Optional, Union
from pathlib import Path
from ..core.logger import AGILogger
from ..core.config import AGIConfig
from ..atomspace.atom import Atom

class VirtualFile:
    def __init__(self, path: str, content: Union[str, bytes, Atom]):
        self.logger = AGILogger().get_logger()
        self.path = Path(path)
        self.content = content
        self.logger.debug(f"Created new VirtualFile at {self.path}")

    def read(self) -> Union[str, bytes, Atom]:
        return self.content

    def write(self, content: Union[str, bytes, Atom]):
        self.content = content
        self.logger.debug(f"Updated content of VirtualFile at {self.path}")

    def __repr__(self):
        return f"VirtualFile(path={self.path}, content={type(self.content)})"

class VirtualDirectory:
    def __init__(self, path: str):
        self.logger = AGILogger().get_logger()
        self.path = Path(path)
        self.children: Dict[str, Union[VirtualFile, 'VirtualDirectory']] = {}
        self.logger.debug(f"Created new VirtualDirectory at {self.path}")

    def add_child(self, name: str, child: Union[VirtualFile, 'VirtualDirectory']):
        self.children[name] = child
        self.logger.debug(f"Added child {name} to directory {self.path}")

    def get_child(self, name: str) -> Optional[Union[VirtualFile, 'VirtualDirectory']]:
        return self.children.get(name)

    def list_children(self) -> List[str]:
        return list(self.children.keys())

    def __repr__(self):
        return f"VirtualDirectory(path={self.path}, children={len(self.children)})"

class VirtualFileSystem:
    def __init__(self):
        self.logger = AGILogger().get_logger()
        self.config = AGIConfig()
        self.root = VirtualDirectory(self.config.filesystem_config['root_path'])
        self.logger.info("Initialized new VirtualFileSystem")

    def resolve_path(self, path: str) -> Optional[Union[VirtualFile, VirtualDirectory]]:
        current = self.root
        parts = Path(path).relative_to(self.config.filesystem_config['root_path']).parts
        
        for part in parts:
            if not isinstance(current, VirtualDirectory):
                return None
            current = current.get_child(part)
            if current is None:
                return None
        return current

    def create_file(self, path: str, content: Union[str, bytes, Atom]) -> bool:
        parent_path = Path(path).parent
        filename = Path(path).name
        parent = self.resolve_path(str(parent_path))
        
        if parent is None or not isinstance(parent, VirtualDirectory):
            return False
        
        if parent.get_child(filename) is not None:
            return False
        
        parent.add_child(filename, VirtualFile(path, content))
        self.logger.info(f"Created new file at {path}")
        return True

    def create_directory(self, path: str) -> bool:
        parent_path = Path(path).parent
        dirname = Path(path).name
        parent = self.resolve_path(str(parent_path))
        
        if parent is None or not isinstance(parent, VirtualDirectory):
            return False
        
        if parent.get_child(dirname) is not None:
            return False
        
        parent.add_child(dirname, VirtualDirectory(path))
        self.logger.info(f"Created new directory at {path}")
        return True

    def __repr__(self):
        return f"VirtualFileSystem(root={self.root})"
