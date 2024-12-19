import allure
from selene import browser, by, be


def test_decorator_steps(open_browser):
    open_main_page('/')
    search_for_repository("eroshenkoam/allure-example")
    go_to_repository("eroshenkoam/allure-example")
    open_issue_tab()
    should_see_issue_with_name("Крокодилы ходят лёжа")


@allure.step("Открываем главную страницу {url}")
def open_main_page(url):
    browser.open(url)


@allure.step("Ищем репозиторий {repo}")
def search_for_repository(repo):
    browser.element('.header-search-button').should(be.visible).click()

    browser.element('#query-builder-test').should(be.visible).send_keys(repo)
    browser.element('#query-builder-test').should(be.visible).submit()


@allure.step("Переходим по ссылке репозитория {repo}")
def go_to_repository(repo):
    browser.element(by.link_text(repo)).should(be.visible).click()


@allure.step("Открываем таб Issues")
def open_issue_tab():
    browser.element("#issues-tab").should(be.visible).click()


@allure.step("Проверяем наличие Issue с названием {name}")
def should_see_issue_with_name(name):
    browser.element(by.partial_text(name)).should(be.visible).click()