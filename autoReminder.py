from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service #selenium version 4
from selenium.webdriver.support.wait import WebDriverWait 
from selenium.webdriver.support import expected_conditions as Alert
from webdriver_manager.chrome import ChromeDriverManager
import time
import winsound

options = Options()

options.add_experimental_option('detach', True) #브라우저 닫힘 방지
options.add_experimental_option("excludeSwitches", ["enable-logging"]) # 불필요한 메세지 제거
options.add_argument("--start-maximized") # 최대 크기로 시작
# options.add_experimental_option("excludeSwitches", ["enable-automation"]) #상단의 자동화 메세지 제거
# user_data = "C:\\Users\\kkgm94\\Desktop\\CgvProject\\user_data" #방문기록이나 검색 기록 저장
# options.add_argument(f"user-data-dir={user_data}")
# options.add_argument("--start-fullscreen") # 전체 화면(F11)으로 시작
# options.add_argument("window-size=500,500") # 화면 크기 지정
# options.add_argument("--headless") #화면안나오고 자동실행
# options.add_argument("--disable-gpu") #headless 보강
# options.add_argument("--mute-audio") # 음소거
# options.add_argument("incognito") # 시크릿 모드


service = Service(ChromeDriverManager(path="Drivers").install()) #Drivers라는 폴더에 설치

url = 'https://www.cgv.co.kr/'
user_id = 'kkgm94'
user_password = 'rudALS3922!'
movie_name = '아바타-물의길'
state = '서울' 
city = '영등포'
movie_date = '20221224'

def login():
    driver.get(url)
    time.sleep(0.1) 

    driver.find_element(By.LINK_TEXT, "로그인").click()
    # driver.find_element(By.PARTIAL_LINK_TEXT, "그인").click() #일부분만 일치해도 클릭
    time.sleep(0.1) 

    driver.find_element(By.ID, "txtUserId").send_keys(user_id)
    driver.find_element(By.ID, "txtPassword").send_keys(user_password)

    driver.find_element(By.ID, "submit").click()
    time.sleep(0.1) 

def goReservation():
    driver.find_element(By.LINK_TEXT, "예매").click()
    time.sleep(0.1) 

def cheakSeat():
    ticket_domain = driver.find_element(By.ID, "ticket_iframe").get_attribute('src')
    driver.execute_script(f'window.open("{ticket_domain}");')
    time.sleep(0.1) 
    driver.switch_to.window(driver.window_handles[-1])
    driver.find_element(By.XPATH,'//*[@id="ticket"]/div[1]/span/a[3]').click()
    time.sleep(0.5) 
    driver.find_element(By.CSS_SELECTOR, f"[title='{movie_name}']").click()
    time.sleep(0.5) 
    driver.find_element(By.PARTIAL_LINK_TEXT, f"{state}").click()
    time.sleep(0.5) 
    driver.find_element(By.PARTIAL_LINK_TEXT, f"{city}").click()
    time.sleep(0.5) 
    driver.find_element(By.CSS_SELECTOR, f"[date='{movie_date}']").click()
    time.sleep(0.5) 

def confirmSeat(cnt):
    condition = 0
    try:
        WebDriverWait(driver, 2).until(Alert.alert_is_present())
        alert = driver.switch_to.alert
        print (f"{movie_date}은 아직 예매불가입니다.-{cnt}-")
        # 확인하기
        alert.accept()
        condition = 1
    except:
        print(f"{movie_date}은 예매 가능합니다.")
        # 알림음 재생
        for _ in range(10):
            winsound.Beep(
                frequency=440,  # Hz
                duration=1000  # milliseconds
            )
        condition = 2
    return condition
def close_window():
    driver.close()
    driver.switch_to.window(driver.window_handles[0])
    time.sleep(0.5)
    driver.refresh()

def main(realend):
    repeat = 0
    cnt = 0 
    login()
    goReservation()

    while True:
        cheakSeat()
        repeat = confirmSeat(cnt)
        if repeat == 2:
            realend = 1
            break
        close_window()
        time.sleep(2) #2초에 한번씩 확인
        if cnt == 300: cnt = 0
        cnt += 1
    return realend

if __name__== "__main__":
    while True:
        realend = 0
        try:
            driver = webdriver.Chrome(service=service, options=options)
            realend = main(realend)
        except:
            driver.quit()
            winsound.Beep(
                frequency=440,  # Hz
                duration=1000  # milliseconds
            )
        if (realend == 1):
            break