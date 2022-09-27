import pytest

"""Configuration for pytest runner."""
pytest_plugins = 'pytester'


@pytest.fixture
def teardown_fixture(request):
    request.driver.close_driver()
    """
        The yield block makes to run the code blocks once the test execution is finished.
        If yield block is deleted here, the code blocks run before the test execution starts.
    """
    yield
    print("If this fixture is added to any test, this comment line will be printed at the end of the test's execution")
