import os
import time
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


def submit_data(i1,i2,i3):
    driver = webdriver.Chrome(executable_path="./chromedriver.exe")
    driver.get("https://docs.google.com/forms/d/1THLuqaH5hI43kngVIqkl2lrO-6DFfbC0GZi_NXQFkKo/edit")
    time.sleep(1)
    input_1 = driver.find_element_by_xpath("/html/body/div/div[3]/form/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input")
    time.sleep(1)
    input_1.send_keys(i1)
    input_2 = driver.find_element_by_xpath("/html/body/div/div[3]/form/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input")
    time.sleep(1)
    input_2.send_keys(i2)
    input_3 = driver.find_element_by_xpath("/html/body/div/div[3]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input")
    time.sleep(1)
    input_3.send_keys(i3)
    submit = driver.find_element_by_xpath("/html/body/div/div[3]/form/div[2]/div/div[3]/div[1]/div[1]/div")
    time.sleep(1)
    submit.click()


headers = {
"Accept-Language": "en-GB,en;q=0.5",
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:99.0) Gecko/20100101 Firefox/99.0",
}

response = requests.get("https://www.zillow.com/homes/Detroit,-MI_rb/", headers=headers)
string = response.text
soup = BeautifulSoup(string, features="html.parser")

price_search = soup.select(".list-card-price")
price_list = []
for item in price_search:
    text = item.getText()
    text_rep = text.replace(" ", "/")
    text_split = text_rep.split("/")
    price_list.append(text_split[0])
# print(price_list)
# print(len(price_list))


addr_search = soup.select(".list-card-addr")
addr_list = []
for item in addr_search:
    text = item.getText()
    addr_list.append(text)
# print(addr_list)
# print(len(addr_list))

link_search = soup.select(".list-card-link-top-margin.list-card-img")
link_list = []
for item in link_search:
    text = item.get("href")
    link_list.append(text)
# print(link_list)
# print(len(link_list))

for num in range(0,(len(price_list)-1)):
    submit_data(addr_list[num], price_list[num], link_list[num])

driver = webdriver.Chrome(executable_path="./chromedriver.exe")
driver.get("https://docs.google.com/forms/d/1THLuqaH5hI43kngVIqkl2lrO-6DFfbC0GZi_NXQFkKo/edit")
time.sleep(1)

login = driver.find_element_by_xpath("/html/body/div/div[3]/form/div[2]/div/div[1]/div/div[4]/div/div/a[1]")
login.click()

handles = driver.window_handles
driver.switch_to.window(handles[0])
driver.close()
driver.switch_to.window(handles[1])

google_u = driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div/div[1]/div/div[1]/input")
google_u.send_keys("pythondummy001@gmail.com")
google_u.send_keys(Keys.ENTER)
time.sleep(1)

google_p = driver. find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div[1]/div/div/div/div/div[1]/div/div[1]/input")
google_p.send_keys("fNx92jhu4J7PGQE")
google_p.send_keys(Keys.ENTER)
time.sleep(1)

driver.get("https://docs.google.com/forms/d/1THLuqaH5hI43kngVIqkl2lrO-6DFfbC0GZi_NXQFkKo/edit")

responses = driver.find_element_by_xpath("/html/body/div[2]/div[1]/div[1]/div[2]/div[3]/div[1]/div/div[2]/span")
responses.click()
time.sleep(1)

export = driver.find_element_by_css_selector("#ResponsesView > div > div.pVJUee > div.P2pQDc > div.YaSJkd > div:nth-child(1) > div > div")
export.click()
time.sleep(1)

excel = driver.find_element_by_css_selector("#yDmH0d > div.NBxL9e.iWO5td > div > div.I7OXgf.PMS6Ed.barETd.IOncP.ZEeHrd.Inn9w.iWO5td > span > div > div > span > div:nth-child(1) > div > div > div.aCsJod.oJeWuf > div > div.Xb9hP > input")
excel.clear()
excel.send_keys("SF Property Values")
time.sleep(1)

create = driver.find_element_by_css_selector("#yDmH0d > div.NBxL9e.iWO5td > div > div.I7OXgf.PMS6Ed.barETd.IOncP.ZEeHrd.Inn9w.iWO5td > div.OE6hId.J9fJmf > div.uArJ5e.UQuaGc.kCyAyd.l3F1ye.ARrCac.HvOprf.M9Bg4d > span > span")
create.click()
time.sleep(30)

driver.quit()