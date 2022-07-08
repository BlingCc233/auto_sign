
# 方便延时加载
import time
from selenium import webdriver
import requests
'''from selenium.webdriver.chrome.options import Options

options = Options()
options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
#chrome_driver = "C:\Program Files\Google\Chrome\Application"
browser = webdriver.Chrome(options=options)'''

 
# 模拟浏览器打开网站
browser = webdriver.Chrome()
browser.get('http://yycdjxx.gsjiapei.com/NMobile/page/timenew.html?ts=637928390108311166')
# 将窗口最大化
browser.maximize_window()
 
# 根据路径找到按钮,并模拟进行点击
# 延时2秒，以便网页加载所有元素，避免之后找不到对应的元素

#browser.find_element_by_xpath('/html/body/form/div[0]/p[0]/input').click()
#/html/body/div[1]/div[2]/div[0]/div[1]/div/ul/li[2]
# 格式是PEP8自动转的
# 这里是找到输入框,发送要输入的用户名和密码,模拟登陆
browser.find_element("xpath", "//*[@id='userName']").send_keys("账号")


browser.find_element("xpath","//*[@id='pwd']").send_keys("密码")

# 在输入用户名和密码之后,点击登陆按钮
browser.find_element("xpath","//*[@id='ckbremember']").click()



# 点击登陆后的页面中的签到,跳转到签到页面
browser.find_element("xpath","//*[@id='btnLogin']").click()
time.sleep(2)


browser.find_element("xpath","/html/body/div[3]/div[2]/div[1]/ul/li[3]/a").click()
time.sleep(2)

browser.find_element("xpath","/html/body/div[3]/div[3]/div[2]/div[1]/div[4]/div[1]/a[13]").click()
time.sleep(1)

browser.find_element("xpath","/html/body/div[3]/div[1]/div[1]/div[1]/a[2]").click()

time.sleep(40)
 

 
# 脚本运行成功,退出浏览器
#browser.quit()
