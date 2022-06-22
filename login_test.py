from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

success_msg = 'Success: Login Sucessful.'
error_msg = 'Error: Invalid Credentials. Please try again.' 

driver = webdriver.Chrome('./chromedriver')
driver.get("http://localhost:8000/index")  

def try_login(user, pwd):
    driver.get("http://localhost:8000/index")    
    username = driver.find_element_by_name("username")
    username.send_keys(user)

    password = driver.find_element_by_name("password")
    password.send_keys(pwd)
    username.send_keys(Keys.RETURN)

    message = driver.find_element_by_name("message")
    txt = message.text
    return txt

def try_login_user_pwd_msg(user, pwd):
    driver.get("http://localhost:8000/index")    
    username = driver.find_element_by_name("username")
    username.send_keys(user)

    password = driver.find_element_by_name("password")
    password.send_keys(pwd)

    username.send_keys(Keys.RETURN)

    txt4 = [username.get_attribute("validationMessage"), password.get_attribute("validationMessage")]
    return txt4
    
def test_login_correct_user_and_password():    
    assert try_login("munay", "munay!") == success_msg

def test_login_incorrect_user_and_password():  
    assert try_login("larry", "123412") == error_msg

def test_login_correct_user_incorrect_password():  
    assert try_login("waoty", "smurf") == error_msg

def test_login_empty():  
    assert try_login_user_pwd_msg("", "123")[0] == "Please fill out this field."

def test_password_empty():  
    assert try_login_user_pwd_msg("123", "")[1] == "Please fill out this field."