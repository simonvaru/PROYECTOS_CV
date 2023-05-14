from selenium import webdriver
import time

web=webdriver.Chrome()
web.get('http://forms.gle/VmroKJ4BNBvroE3n7')
time.sleep(3)

sname='Carl'
name=web.find_element('xpath','//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
name.send_keys(sname)
time.sleep(3)

mobile='54+351155384696'
phone=web.find_element('xpath','//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
phone.send_keys(mobile)
time.sleep(3)

sel_button=web.find_element('xpath','//*[@id="i17"]/div[2]')
sel_button.click()
time.sleep(3)

col_name='St. Patrick'
cname=web.find_element('xpath','//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div/div[1]/input')
cname.send_keys(col_name)
time.sleep(3)

submit=web.find_element('xpath','//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')
submit.click()
time.sleep(15)