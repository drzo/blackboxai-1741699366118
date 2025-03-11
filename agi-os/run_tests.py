import pytest
import sys

if __name__ == '__main__':
    # Run all tests in the tests directory
    result = pytest.main(['agi-os/tests/', '-v'])
    sys.exit(result)
