import allure
import pytest

from framework.logger import Logger
from project.models import Bear
from project.steps import CommonSteps
from project.utilities.api_utilities import BearApiUtils


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call) -> None:
    """
    Hook to log test result run status
    """
    outcome = yield
    rep = outcome.get_result()

    if rep.outcome == "skipped":
        Logger.info(f"Test '{item.nodeid}' skipped")
    else:
        if rep.when == "setup":
            Logger.info(f"Test '{item.nodeid}' started")
        elif rep.when == "call":
            Logger.info(f"Test [{item.name}] finished with result '{rep.outcome}'")

        if call.excinfo:
            Logger.error("".join([str(element) for element in call.excinfo.traceback]))


@allure.title("Clear bear objects list")
@pytest.fixture(scope="function", autouse=True)
def clear_bear_objects() -> None:
    """
    Clear all bear objects
    """
    BearApiUtils.delete_bears()


@allure.title("Crete default bear object")
@pytest.fixture(scope="function")
def default_bear() -> Bear:
    """
    Create default bear object
    :return: Bear object with default data
    :rtype: Bear
    """
    yield CommonSteps.create_default_bear()
