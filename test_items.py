import time


page = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'


def test_button_add_to_basket_exists(browser): 
    browser.get(page)
    #time.sleep(30) #для ручной проверки наличия кнопки
    button = browser.find_elements_by_css_selector('button.btn-add-to-basket')
    assert len(button) > 0, 'Error! Button "Add to basket" not found.'
