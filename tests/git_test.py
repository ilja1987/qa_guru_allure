import allure
from selene.support.shared import browser
from selene import by, be


def test_git_without_allure(browser_setup):
    browser.open('https://github.com/')

    browser.element('[name="q"]').click()
    browser.element('[name="q"]').send_keys('ilja1987/qa_guru_python_2').press_enter()

    browser.element('[href="/ilja1987/qa_guru_python_2"]').click()
    browser.element('[id="issues-tab"]').click()

    browser.element(by.partial_text('#1 opened')).should(be.visible)


def test_git_with_as(browser_setup):
    with allure.step('Открываем главную страницу'):
        browser.open('https://github.com/')
    with allure.step('Ищем репозиторий'):
        browser.element('[name="q"]').click()
        browser.element('[name="q"]').send_keys('ilja1987/qa_guru_python_2').press_enter()
    with allure.step('Переходим по ссылке в репозиторий'):
        browser.element('[href="/ilja1987/qa_guru_python_2"]').click()
    with allure.step('Открываем таб Issue'):
        browser.element('[id="issues-tab"]').click()
    with allure.step('Проверяем наличие issue с номером 1'):
        browser.element(by.partial_text('#1 opened')).should(be.visible)


def test_git_with_dec(browser_setup):
    open_main_page()
    search_for_repository('ilja1987/qa_guru_python_2')
    go_to_repository('[href="/ilja1987/qa_guru_python_2"]')
    open_issue_tab()
    should_see_issue_with_number('1')


@allure.step('Открываем главную страницу')
def open_main_page():
    browser.open('https://github.com/')


@allure.step('Ищем репозиторий {repo}')
def search_for_repository(repo):
    browser.element('[name="q"]').click()
    browser.element('[name="q"]').send_keys(repo).press_enter()


@allure .step('Переходим по ссылке в репозиторий {repo}')
def go_to_repository(repo):
    browser.element('[href="/ilja1987/qa_guru_python_2"]').click()


@allure.step('Открываем таб Issue')
def open_issue_tab():
    browser.element('[id="issues-tab"]').click()


@allure.step('Проверяем наличие issue с номером {number}')
def should_see_issue_with_number(number):
    browser.element(by.partial_text('#1 opened')).should(be.visible)