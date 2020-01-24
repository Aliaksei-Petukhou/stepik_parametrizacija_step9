import time

def test_est_li_knopka_tovara(browser):
    
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    
    browser.get(link)
    
    time.sleep(5)
    
    assert browser.find_element_by_css_selector('.btn-add-to-basket'), "А кнопки то нет =("

