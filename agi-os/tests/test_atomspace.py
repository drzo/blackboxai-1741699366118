import pytest
from ..src.atomspace.atom import Atom
from ..src.atomspace.atomspace import AtomSpace

def test_atom_creation():
    atom = Atom('test_type', 'test_content')
    assert atom.atom_type == 'test_type'
    assert atom.content == 'test_content'

def test_atomspace_operations():
    atomspace = AtomSpace()
    atom1 = Atom('type1', 'content1')
    atom2 = Atom('type2', 'content2')
    
    # Test adding atoms
    assert atomspace.add_atom(atom1) == True
    assert atomspace.add_atom(atom1) == False  # Duplicate
    
    # Test getting atoms
    assert atomspace.get_atom('type1') == atom1
    assert atomspace.get_atom('nonexistent') is None
    
    # Test linking atoms
    atomspace.add_atom(atom2)
    assert atomspace.link_atoms('type1', 'type2') == True
    assert atomspace.link_atoms('type1', 'nonexistent') == False

def test_atom_properties():
    atom = Atom('test_type', 'test_content')
    atom.set_property('key1', 'value1')
    assert atom.get_property('key1') == 'value1'
    assert atom.get_property('nonexistent') is None
