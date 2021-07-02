import os

def example1():
    """
    Retrieve the current directory

    Returns:
        Current directory
    """
    current_path = os.getcwd()
    return current_path

def test_get_current_directory(monkeypatch):
    """
    GIVEN a monkeypatched version of os.getcwd()
    WHEN example1() is called
    THEN check the current directory returned
    """
    def mock_getcwd():
        return '/data/user/directory123'

    # monkeypatch.setattr(obj, name, value, raising=True)
    monkeypatch.setattr(os, 'getcwd', mock_getcwd)
    assert example1() == '/data/user/directory123'
