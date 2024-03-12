import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='en',
                     help="Choose language")


@pytest.fixture(scope="function")
def browser(request):
    language = request.config.getoption("--language")
    if language not in [
        'ar', 'ca', 'cs', 'da', 'de', 'en', 'en-gb', 'el', 'es', 'fi', 'fr',
        'it', 'ko', 'nl', 'pl', 'pt', 'pt-br', 'ro', 'ru', 'sk', 'uk'
    ]:
        raise ValueError(
            "Unsupported language. Choose ar, ca, cs, da, de, 'en', en-gb, el, "
            "es, fi, fr, it, ko, nl, pl, pt, pt-br, ro, ru, sk, uk"
        )

    options = webdriver.ChromeOptions()
    options.add_experimental_option(
        'prefs',
        {'intl.accept_languages': language}
    )

    browser = webdriver.Chrome(options=options)
    browser.implicitly_wait(10)
    yield browser
    browser.quit()
