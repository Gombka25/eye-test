import pytest
from browser import get_driver

@pytest.fixture(scope=module)
def driver():
    return get_driver()