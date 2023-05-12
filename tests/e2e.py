from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

def test_scores_service(url:str):
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.maximize_window()
    driver.implicitly_wait(5)
    driver.get(url)
    score_element=driver.find_element(By.CSS_SELECTOR,'div[id="score"]')
    if 1000 >=int(score_element.text) >=0:
        return True
    return False

def main_function():
    if test_scores_service(url = 'http://localhost:8777/'):
        return 0
    return -1


main_function()