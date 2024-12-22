from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.action_chains import ActionChains
import time

def Racer():
    cookie_string = "__utmc=163867134; _ga=GA1.1.361923735.1734725799; usprivacy=1---; ad_clicker=false; _sharedid=d9bf8df1-79a4-4c29-a751-cde6743e5793; _sharedid_cst=zix7LPQsHA%3D%3D; _li_dcdm_c=.typeracer.com; _lc2_fpi=2f5ada2fb6ea--01jfjve4qfj5p8201wvh416zzm; _lc2_fpi_meta=%7B%22w%22%3A1734725800687%7D; info=L%7Ctr%3Anlack_bigger%7C1736088790.85%7C4JcKUShFlK6ucSGS2Wa7g8FmuKk%3D; ph_phc_wWvTJTWTbC3Oxk1ebTnyAir93FwPPqxqd91dvrJWE3z_posthog=%7B%22distinct_id%22%3A%220193ee31-d597-7e99-a4de-ddc3ae9cd37a%22%2C%22%24sesid%22%3A%5B1734879401272%2C%220193eeaf-d66f-7f1e-954b-d32d9be7026f%22%2C1734876321391%5D%2C%22%24initial_person_info%22%3A%7B%22r%22%3A%22https%3A%2F%2Fwww.google.com%2F%22%2C%22u%22%3A%22https%3A%2F%2Fplay.typeracer.com%2F%22%7D%7D; __utma=163867134.890847797.1734725799.1734876321.1734890975.9; __utmz=163867134.1734890975.9.7.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided); __utmt=1; prefs=%7B%22dateOfLastVisit%22%3A%201734892436082.0%2C%20%22dateOfPriorVisit%22%3A%201734890975207.5%2C%20%22domain%22%3A%20%22.typeracer.com%22%2C%20%22pupDate%22%3A%201734879191008.5%7D; FCNEC=%5B%5B%22AKsRol-P8h_4W0GNjOu5PEWr5ATvXWrMqQcHtuwCdONmYPtJ1wONrJBbhAPW_VUMBYpXLGcoosnRg-P15rmmN5fjTc2-lhdhpCgr2v_tXcQ7hQt9ygUf4-LDyPoho9xjSs-fKGnrJELWZnLZmaJNNMBAEnwVNgmsrw%3D%3D%22%5D%5D; __utmb=163867134.19.1.1734892437346; _ga_MH93WM11JZ=GS1.1.1734890975.9.1.1734892437.0.0.0"
    
    cookies = []
    for cookie in cookie_string.split("; "):
        name, value = cookie.split("=", 1)
        cookies.append({"name": name, "value": value})

    option = Options()
    option.set_preference("privacy.trackingprotection.enabled", False)

    driver = webdriver.Firefox(options=option)
    driver.maximize_window()
    driver.implicitly_wait(20)
    
    try:
        driver.get('https://play.typeracer.com')
        time.sleep(2)

        for cookie in cookies:
            cookie["domain"] = ".typeracer.com" 
            driver.add_cookie(cookie)
        driver.refresh()
        time.sleep(2)

        action = ActionChains(driver)
        action.key_down(Keys.LEFT_CONTROL).key_down(Keys.LEFT_ALT).send_keys("i").key_up(Keys.LEFT_CONTROL).key_up(Keys.LEFT_ALT).perform()
        time.sleep(2)

        light_sight = driver.find_element(By.XPATH, '/html/body/div[10]/div/table/tbody/tr/td/table/tbody/tr/td[2]/div').text
        text = driver.find_element(By.XPATH, '/html/body/div[2]/div/div[2]/div/div[1]/div[1]/table/tbody/tr[2]/td[2]/div/div[2]/div/table/tbody/tr[2]/td[3]/table/tbody/tr[2]/td/table/tbody/tr[1]/td/table/tbody/tr[1]/td/div/div[1]').text
        while light_sight != 'It\'s the final countdown!':
            time.sleep(1)
            light_sight = driver.find_element(By.XPATH, '/html/body/div[10]/div/table/tbody/tr/td/table/tbody/tr/td[2]/div').text
            if light_sight == '':
                break

        time.sleep(len(text)/12)

        input_text = driver.find_element(By.XPATH, '/html/body/div[2]/div/div[2]/div/div[1]/div[1]/table/tbody/tr[2]/td[2]/div/div[2]/div/table/tbody/tr[2]/td[3]/table/tbody/tr[2]/td/table/tbody/tr[2]/td/input')
        input_text.click()
        for character in text:
            input_text.send_keys(character)
            time.sleep(0.03) 

        time.sleep(3)
    finally:
        driver.quit()