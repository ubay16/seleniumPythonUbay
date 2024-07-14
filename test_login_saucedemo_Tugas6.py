from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest

@pytest.fixture
def setup():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(10)
    driver.maximize_window()
    driver.get('https://www.saucedemo.com/')
    yield driver
    driver.quit()

@pytest.mark.positive
def test_login_positif(setup):
    '''
    Login dengan menggunakan username dan password yang benar
    '''
    setup.find_element(By.ID,'user-name').send_keys('standard_user') #username
    setup.find_element(By.ID,'password').send_keys('secret_sauce') #password
    setup.find_element(By.ID,'login-button').click()

    title = setup.find_element(By.XPATH,'//*[@id="header_container"]/div[1]/div[2]/div').text
    assert title == 'Swag Labs'

    
input_output = [
    ('sentot','secret_sauce',True, 'Epic sadface: Username and password do not match any user in this service'),
    ('standard_user','passwordsalah',True, 'Epic sadface: Username and password do not match any user in this service'),
    ('sentot','passwordsalah',True, 'Epic sadface: Username and password do not match any user in this service'),
]
@pytest.mark.negative
@pytest.mark.parametrize('username, password, notif, notiftext',input_output)
def test_login_negatif_1(setup, username, password, notif, notiftext):
    '''
    Login dengan menggunakan username yang salah dan password yang benar
    
    username password result

    salah    bener    gak bisa login
    bener    salah    gak bisa login
    salah    salah    gak bisa login

    '''
    setup.find_element(By.ID,'user-name').send_keys('secret_sauce') #username
    setup.find_element(By.ID,'password').send_keys('secret_sauce') #password
    setup.find_element(By.ID,'login-button').click()

    notification_error = setup.find_element(By.XPATH,'//h3[@data-test="error"]').is_displayed()
    assert notification_error == notif
    notification_text = setup.find_element(By.XPATH,'//h3[@data-test="error"]').text
    assert notification_text == notiftext
def test_login_negatif_2(setup, username, password, notif, notiftext):
    
    setup.find_element(By.ID,'user-name').send_keys('standard_user') #username
    setup.find_element(By.ID,'password').send_keys('secret_sauce') #password
    setup.find_element(By.ID,'login-button').click()

    notification_error = setup.find_element(By.XPATH,'//h3[@data-test="error"]').is_displayed()
    assert notification_error == notif
    notification_text = setup.find_element(By.XPATH,'//h3[@data-test="error"]').text
    assert notification_text == notiftext

def test_login_negatif_3(setup, username, password, notif, notiftext):
    
    setup.find_element(By.ID,'user-name').send_keys('user') #username
    setup.find_element(By.ID,'password').send_keys('user') #password
    setup.find_element(By.ID,'login-button').click()

    notification_error = setup.find_element(By.XPATH,'//h3[@data-test="error"]').is_displayed()
    assert notification_error == notif
    notification_text = setup.find_element(By.XPATH,'//h3[@data-test="error"]').text
    assert notification_text == notiftext

