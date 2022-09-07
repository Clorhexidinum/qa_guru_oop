def open_browser(browser_name):
    print_readable_name(open_browser, browser_name)


def go_to_companyname_homepage(page_url):
    print_readable_name(go_to_companyname_homepage, page_url)


def find_registration_button_on_login_page(page_url, button_text):
    print_readable_name(find_registration_button_on_login_page, page_url, button_text)


def print_readable_name(function_name, *args):
    function_name = function_name.__name__.title().replace('_', ' ')
    print(f'\nИмя функции: {function_name}. Аргументы функции: ')

    for arg in args:
        print(arg)


open_browser("Chrome")
go_to_companyname_homepage("https://yandex.ru/")
find_registration_button_on_login_page("https://yandex.ru/", "Submit")