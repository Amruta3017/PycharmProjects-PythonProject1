import pytest
from pytest_metadata.plugin import metadata_key
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome",
                     help="specify the browser: chrome or firefox or edge")


@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")

@pytest.fixture()
def setup(browser):

    if browser == "chrome":
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)

    elif browser == "edge":
            service = EdgeService(EdgeChromiumDriverManager().install())
            driver = webdriver.Edge(service=service)
    elif browser == "firefox":
        service = FirefoxService(GeckoDriverManager().install())
        driver = webdriver.Firefox(service=service)
    else:
        raise ValueError("unsuported browser")

    yield driver
    driver.quit()



#################### for adding persnal data in html report use hook function ###########################
#hook add to environmental info in report

def pytest_configure(config):
    config.stash[metadata_key]['project name'] = "Ecommerce project - nopcommerce"
    config.stash[metadata_key]['test module name'] = "admin"
    config.stash[metadata_key]['tester Name'] = "Amruta"

# hhok for delete or modify environmental info
@pytest.mark.optionalhook
def pytest_metadeta(metadeta):
    metadeta.pop("plugins",None)



