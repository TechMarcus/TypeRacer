from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.action_chains import ActionChains
import time

def Racer(IsCookiesUsed=False, cookies=None):
    option = Options()
    option.set_preference("privacy.trackingprotection.enabled", False)

    driver = webdriver.Firefox(options=option)
    driver.maximize_window()
    driver.implicitly_wait(20)
    
    try:
        driver.get('https://play.typeracer.com')
        time.sleep(3)
        if IsCookiesUsed:
            cookie_string = cookies
            
            cookies = []
            for cookie in cookie_string.split("; "):
                name, value = cookie.split("=", 1)
                cookies.append({"name": name, "value": value})

            for cookie in cookies:
                cookie["domain"] = ".typeracer.com" 
                driver.add_cookie(cookie)
            driver.refresh()
            time.sleep(3)

        action = ActionChains(driver)
        action.key_down(Keys.LEFT_CONTROL).key_down(Keys.LEFT_ALT).send_keys("i").key_up(Keys.LEFT_CONTROL).key_up(Keys.LEFT_ALT).perform()
        time.sleep(3)
        text = driver.find_element(By.XPATH, '/html/body/div[2]/div/div[2]/div/div[1]/div[1]/table/tbody/tr[2]/td[2]/div/div[2]/div/table/tbody/tr[2]/td[3]/table/tbody/tr[2]/td/table/tbody/tr[1]/td/table/tbody/tr[1]/td/div/div[1]').text

        try:
            light_sight = driver.find_element(By.XPATH, '/html/body/div[10]/div/table/tbody/tr/td/table/tbody/tr/td[2]/div').text
            while light_sight != 'It\'s the final countdown!':
                time.sleep(1)
                light_sight = driver.find_element(By.XPATH, '/html/body/div[10]/div/table/tbody/tr/td/table/tbody/tr/td[2]/div').text
                if light_sight == '':
                    break
        except Exception:
            pass

        time.sleep(len(text)/12)

        input_text = driver.find_element(By.XPATH, '/html/body/div[2]/div/div[2]/div/div[1]/div[1]/table/tbody/tr[2]/td[2]/div/div[2]/div/table/tbody/tr[2]/td[3]/table/tbody/tr[2]/td/table/tbody/tr[2]/td/input')
        input_text.click()
        for character in text:
            input_text.send_keys(character)
            time.sleep(0.03) 

        time.sleep(3)
        print('success')
    finally:
        driver.quit()