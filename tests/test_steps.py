import allure
from selene import browser, by, be
from selene.support.shared.jquery_style import s  # s == browser.element()


def test_dynamic_steps(open_browser):
    with allure.step("Открываем главную страницу"):
        browser.open("/")

    with allure.step("Ищем репозиторий"):
        s('.header-search-button').click()

        s("#query-builder-test").send_keys("eroshenkoam/allure-example")
        s("#query-builder-test").submit()

    with allure.step("Переходим по ссылке репозитория"):
        s(by.link_text("eroshenkoam/allure-example")).click()

    with allure.step("Открываем таб Issues"):
        s("#issues-tab").click()

    with allure.step("Проверяем наличие Issue с наименованием 'One piece'"):
        s(by.partial_text("One piece")).should(be.visible)
