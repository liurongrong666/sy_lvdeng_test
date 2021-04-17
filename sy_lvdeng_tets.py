import time
import requests
from selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Chrome()  # 打开谷歌浏览器
driver.get("https://sy-dev.joysfintech.com/joys/login/pc_index.html?from=https%3A%2F%2Fsy-dev.joysfintech.com%2Fjoys%2Fpc_index.html%23%2F#/")  # 输入网址
driver.implicitly_wait(10)
driver.maximize_window()  # 最大窗口化展示
driver.find_element_by_xpath("/html/body/div/div/div[1]/div[2]/div[1]/div/input").send_keys("0139")  # 输入用户名
driver.find_element_by_xpath("/html/body/div/div/div[1]/div[2]/div[2]/div/input").send_keys("kjjr588")  # 输入密码
driver.find_element_by_xpath("/html/body/div/div/div[1]/div[3]/button").click()  # 点击登录按钮

xuanting = driver.find_element_by_xpath("/html/body/div/section/section/header/div/div[1]/div[1]/span")  # 鼠标悬停在导航按钮
ActionChains(driver).move_to_element(xuanting).perform()
lcpt = driver.find_element_by_xpath('//*[text()="流程平台"]')  # 点击“流程平台”节点
ActionChains(driver).move_to_element(lcpt).perform()
rwzx = driver.find_element_by_xpath('/html/body/div[1]/section/section/div/div[2]/div/div')  # 点击任务中心
rwzx.click()
k = driver.find_element_by_xpath("/html/body/div[1]/section/section/header/div/div[3]/div[2]/span/img")  # 点击按钮后，为使页面全部展示，将鼠标悬停在头像处。
ActionChains(driver).move_to_element(k).perform()
a = driver.find_element_by_xpath('/html/body/div[1]/section/section/main/div/div[1]/div[1]/div/div[2]')  # 点击任务中心按钮
a.click()
k = driver.find_element_by_xpath("/html/body/div[1]/section/section/header/div/div[3]/div[2]/span/img")  # 点击按钮后，为使页面全部展示，将鼠标悬停在头像处。
ActionChains(driver).move_to_element(k).perform()
renwu = driver.find_element_by_xpath("/html/body/div[1]/section/section/main/div/div[2]/div[2]/iframe")  # 获取页面的句柄
driver.switch_to.frame(renwu)
time.sleep(5)
driver.find_element_by_xpath("/html/body/div/div[2]/div/div[3]/div[4]/div/div/div[1]/div[1]/div/div/button[1]").click()   #点击刷新按钮
currentPageUrl = driver.current_url
print("当前页面的url是：", currentPageUrl)     # 获取当前URL地址
code = requests.get(currentPageUrl).status_code
print("任务中心状态码校验:{}".format(code))   # 获取当前URL的状态码
driver.refresh()   #刷新整个页面
xuanting1 = driver.find_element_by_class_name("menuImg_box")  # 鼠标悬停在导航按钮
ActionChains(driver).move_to_element(xuanting1).perform()
xxgl = driver.find_element_by_xpath('//*[text()="系统管理"]')  # 点击“系统管理”节点
ActionChains(driver).move_to_element(xxgl).perform()
xtxx = driver.find_element_by_xpath('/html/body/div[1]/section/section/div/div[2]/div/div')  # 点击“系统消息”按钮
xtxx.click()
k = driver.find_element_by_xpath("/html/body/div[1]/section/section/header/div/div[3]/div[2]/span/img")  # 点击按钮后，为使页面全部展示，将鼠标悬停在头像处
ActionChains(driver).move_to_element(k).perform()
xt = driver.find_element_by_xpath("/html/body/div[1]/section/section/main/div/div[2]/div[2]/iframe")  # 获取页面的句柄
driver.switch_to.frame(xt)
time.sleep(2)
driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div[3]/div[7]/div[1]/div[1]/div[1]/button[1]").click()   #点击刷新按钮
currentPageUrl = driver.current_url
print("当前页面的url是：", currentPageUrl)     # 获取当前URL地址
code = requests.get(currentPageUrl).status_code
print("系统消息状态码校验:{}".format(code))   # 获取当前URL的状态码
driver.refresh()   #刷新整个页面
xuanting1 = driver.find_element_by_class_name("menuImg_box")  # 鼠标悬停在导航按钮
ActionChains(driver).move_to_element(xuanting1).perform()
xxgl = driver.find_element_by_xpath('//*[text()="系统管理"]')  # 点击“系统管理”节点
ActionChains(driver).move_to_element(xxgl).perform()
xtxx = driver.find_element_by_xpath('/html/body/div[1]/section/section/div/div[2]/div/div')  # 点击“系统消息”按钮
xtxx.click()
k = driver.find_element_by_xpath("/html/body/div[1]/section/section/header/div/div[3]/div[2]/span/img")  # 点击按钮后，为使页面全部展示，将鼠标悬停在头像处
ActionChains(driver).move_to_element(k).perform()
xt = driver.find_element_by_xpath("/html/body/div[1]/section/section/main/div/div[2]/div[2]/iframe")  # 获取页面的句柄
driver.switch_to.frame(xt)
time.sleep(2)
driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div[3]/div[7]/div[1]/div[1]/div[1]/button[1]").click()   #点击刷新按钮
currentPageUrl = driver.current_url
print("当前页面的url是：", currentPageUrl)     # 获取当前URL地址
code = requests.get(currentPageUrl).status_code
print("系统消息状态码校验:{}".format(code))   # 获取当前URL的状态码
driver.refresh()   #刷新整个页面
xuanting2 = driver.find_element_by_class_name("menuImg_box")  # 鼠标悬停在导航按钮
ActionChains(driver).move_to_element(xuanting2).perform()
khgl = driver.find_element_by_xpath('//*[text()="客户管理"]')  # 点击“客户管理”节点
ActionChains(driver).move_to_element(khgl).perform()
khgl01 = driver.find_element_by_xpath('/html/body/div[1]/section/section/div/div[2]/div[1]/div')  # 点击“客户信息维护”按钮
khgl01.click()
k = driver.find_element_by_xpath("/html/body/div[1]/section/section/header/div/div[3]/div[2]/span/img")  # 点击按钮后，为使页面全部展示，将鼠标悬停在头像处
ActionChains(driver).move_to_element(k).perform()
khgl011 = driver.find_element_by_xpath("/html/body/div[1]/section/section/main/div/div[2]/div[2]/iframe")  # 获取页面的句柄
driver.switch_to.frame(khgl011)
time.sleep(2)
driver.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/div[1]/div[1]/div/button[1]").click()   #点击刷新按钮
currentPageUrl = driver.current_url
print("当前页面的url是：", currentPageUrl)     # 获取当前URL地址
code = requests.get(currentPageUrl).status_code
print("客户信息维护状态码校验:{}".format(code))   # 获取当前URL的状态码
driver.refresh()   #刷新整个页面
xuanting2 = driver.find_element_by_class_name("menuImg_box")  # 鼠标悬停在导航按钮
ActionChains(driver).move_to_element(xuanting2).perform()
khgl = driver.find_element_by_xpath('//*[text()="客户管理"]')  # 点击“客户管理”节点
ActionChains(driver).move_to_element(khgl).perform()
khgl02 = driver.find_element_by_xpath('/html/body/div[1]/section/section/div/div[2]/div[2]/div')  # 点击“客户移交”按钮
khgl02.click()
k = driver.find_element_by_xpath("/html/body/div[1]/section/section/header/div/div[3]/div[2]/span/img")  # 点击按钮后，为使页面全部展示，将鼠标悬停在头像处
ActionChains(driver).move_to_element(k).perform()
khgl021 = driver.find_element_by_xpath("/html/body/div[1]/section/section/main/div/div[2]/div[2]/iframe")  # 获取页面的句柄
driver.switch_to.frame(khgl021)
driver.find_element_by_xpath("/html/body/div/div[2]/div/div/div[3]/div[3]/div[1]/div[1]/div/div/button[1]").click()   #点击刷新按钮
time.sleep(2)
currentPageUrl = driver.current_url
print("当前页面的url是：", currentPageUrl)     # 获取当前URL地址
code = requests.get(currentPageUrl).status_code
print("客户移交状态码校验:{}".format(code))   # 获取当前URL的状态码
driver.refresh()   #刷新整个页面
xuanting2 = driver.find_element_by_class_name("menuImg_box")  # 鼠标悬停在导航按钮
ActionChains(driver).move_to_element(xuanting2).perform()
khgl = driver.find_element_by_xpath('//*[text()="客户管理"]')  # 点击“客户管理”节点
ActionChains(driver).move_to_element(khgl).perform()
khgl02 = driver.find_element_by_xpath('/html/body/div[1]/section/section/div/div[2]/div[3]/div')  # 点击“企业客户信息维护”按钮
khgl02.click()
k = driver.find_element_by_xpath("/html/body/div[1]/section/section/header/div/div[3]/div[2]/span/img")  # 点击按钮后，为使页面全部展示，将鼠标悬停在头像处
ActionChains(driver).move_to_element(k).perform()
khgl031 = driver.find_element_by_xpath("/html/body/div[1]/section/section/main/div/div[2]/div[2]/iframe")  # 获取页面的句柄
driver.switch_to.frame(khgl031)

driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div/div[3]/div[3]/div[1]/div[1]/div/div/button[1]").click()   #点击刷新按钮
time.sleep(2)
currentPageUrl = driver.current_url
print("当前页面的url是：", currentPageUrl)     # 获取当前URL地址
code = requests.get(currentPageUrl).status_code
print("企业客户信息维护状态码校验:{}".format(code))   # 获取当前URL的状态码
driver.refresh()   #刷新整个页面
xuanting2 = driver.find_element_by_class_name("menuImg_box")  # 鼠标悬停在导航按钮
ActionChains(driver).move_to_element(xuanting2).perform()
bjgl = driver.find_element_by_xpath('//*[text()="报价管理"]')  # 点击“报价管理”节点
ActionChains(driver).move_to_element(bjgl).perform()
bjgl01 = driver.find_element_by_xpath('/html/body/div[1]/section/section/div/div[2]/div/div')  # 点击“报价测算”按钮
bjgl01.click()
k = driver.find_element_by_xpath("/html/body/div[1]/section/section/header/div/div[3]/div[2]/span/img")  # 点击按钮后，为使页面全部展示，将鼠标悬停在头像处
ActionChains(driver).move_to_element(k).perform()
bjcs = driver.find_element_by_xpath("/html/body/div[1]/section/section/main/div/div[2]/div[2]/iframe")  # 获取页面的句柄
driver.switch_to.frame(bjcs)
driver.find_element_by_xpath("/html/body/div/div[2]/div[2]/div[1]/div[1]/div/button[1]").click()   #点击刷新按钮
time.sleep(2)
currentPageUrl = driver.current_url
print("当前页面的url是：", currentPageUrl)     # 获取当前URL地址
code = requests.get(currentPageUrl).status_code
print("报价测算状态码校验:{}".format(code))   # 获取当前URL的状态码
driver.refresh()   #刷新整个页面
xuanting2 = driver.find_element_by_class_name("menuImg_box")  # 鼠标悬停在导航按钮
ActionChains(driver).move_to_element(xuanting2).perform()
sxgl = driver.find_element_by_xpath('//*[text()="授信管理"]')  # 点击“授信管理”节点
ActionChains(driver).move_to_element(sxgl).perform()
sxgl01 = driver.find_element_by_xpath('/html/body/div[1]/section/section/div/div[2]/div[1]/div')  # 点击“授信管理”按钮
sxgl01.click()
k = driver.find_element_by_xpath("/html/body/div[1]/section/section/header/div/div[3]/div[2]/span/img")  # 点击按钮后，为使页面全部展示，将鼠标悬停在头像处
ActionChains(driver).move_to_element(k).perform()
sxgl011 = driver.find_element_by_xpath("/html/body/div[1]/section/section/main/div/div[2]/div[2]/iframe")  # 获取页面的句柄
driver.switch_to.frame(sxgl011)
driver.find_element_by_xpath("/html/body/div/div/div[2]/div[1]/div[1]/div/button[1]").click()   #点击刷新按钮
time.sleep(2)
currentPageUrl = driver.current_url
print("当前页面的url是：", currentPageUrl)     # 获取当前URL地址
code = requests.get(currentPageUrl).status_code
print("授信管理状态码校验:{}".format(code))   # 获取当前URL的状态码
driver.refresh()   #刷新整个页面
xuanting2 = driver.find_element_by_class_name("menuImg_box")  # 鼠标悬停在导航按钮
ActionChains(driver).move_to_element(xuanting2).perform()
sxgl = driver.find_element_by_xpath('//*[text()="授信管理"]')  # 点击“授信管理”节点
ActionChains(driver).move_to_element(sxgl).perform()
sxcx01 = driver.find_element_by_xpath('/html/body/div[1]/section/section/div/div[2]/div[2]/div')  # 点击“授信查询”按钮
sxcx01.click()
k = driver.find_element_by_xpath("/html/body/div[1]/section/section/header/div/div[3]/div[2]/span/img")  # 点击按钮后，为使页面全部展示，将鼠标悬停在头像处
ActionChains(driver).move_to_element(k).perform()
sxgl012 = driver.find_element_by_xpath("/html/body/div[1]/section/section/main/div/div[2]/div[2]/iframe")  # 获取页面的句柄
driver.switch_to.frame(sxgl012)
driver.find_element_by_xpath("/html/body/div/div/div[2]/div/div[1]/div[1]/div/div/button").click()   #点击刷新按钮
time.sleep(2)
currentPageUrl = driver.current_url
print("当前页面的url是：", currentPageUrl)     # 获取当前URL地址
code = requests.get(currentPageUrl).status_code
print("授信查询状态码校验:{}".format(code))   # 获取当前URL的状态码
driver.refresh()   #刷新整个页面
xuanting2 = driver.find_element_by_class_name("menuImg_box")  # 鼠标悬停在导航按钮
ActionChains(driver).move_to_element(xuanting2).perform()
xmgl = driver.find_element_by_xpath('//*[text()="项目管理"]')  # 点击“项目管理”节点
ActionChains(driver).move_to_element(xmgl).perform()
xmps01 = driver.find_element_by_xpath('/html/body/div[1]/section/section/div/div[2]/div/div')  # 点击“项目评审”按钮
xmps01.click()
k = driver.find_element_by_xpath("/html/body/div[1]/section/section/header/div/div[3]/div[2]/span/img")  # 点击按钮后，为使页面全部展示，将鼠标悬停在头像处
ActionChains(driver).move_to_element(k).perform()
xmps011 = driver.find_element_by_xpath("/html/body/div[1]/section/section/main/div/div[2]/div[2]/iframe")  # 获取页面的句柄
driver.switch_to.frame(xmps011)
driver.find_element_by_xpath("/html/body/div/div/div[1]/div[2]/div[2]").click()   #点击已发起流程
driver.find_element_by_xpath("/html/body/div/div/div[1]/div[3]/div[4]/div[1]/div[1]/div/div/button[1]").click()  #点击刷新按钮
time.sleep(2)
currentPageUrl = driver.current_url
print("当前页面的url是：", currentPageUrl)     # 获取当前URL地址
code = requests.get(currentPageUrl).status_code
print("项目评审状态码校验:{}".format(code))   # 获取当前URL的状态码
driver.refresh()   #刷新整个页面
xuanting2 = driver.find_element_by_class_name("menuImg_box")  # 鼠标悬停在导航按钮
ActionChains(driver).move_to_element(xuanting2).perform()
htgl = driver.find_element_by_xpath('//*[text()="合同管理"]')  # 点击“合同管理”节点
ActionChains(driver).move_to_element(htgl).perform()
xmps01 = driver.find_element_by_xpath('/html/body/div[1]/section/section/div/div[2]/div[1]/div')  # 点击“合同台账”按钮
xmps01.click()
k = driver.find_element_by_xpath("/html/body/div[1]/section/section/header/div/div[3]/div[2]/span/img")  # 点击按钮后，为使页面全部展示，将鼠标悬停在头像处
ActionChains(driver).move_to_element(k).perform()
httz01 = driver.find_element_by_xpath("/html/body/div[1]/section/section/main/div/div[2]/div[2]/iframe")  # 获取页面的句柄
driver.switch_to.frame(httz01)
driver.find_element_by_xpath("/html/body/div/div[2]/div[2]/div[1]/div[1]/div/button[1]").click()  #点击刷新按钮
time.sleep(2)
currentPageUrl = driver.current_url
print("当前页面的url是：", currentPageUrl)     # 获取当前URL地址
code = requests.get(currentPageUrl).status_code
print("合同管理状态码校验:{}".format(code))   # 获取当前URL的状态码
driver.refresh()   #刷新整个页面
xuanting2 = driver.find_element_by_class_name("menuImg_box")  # 鼠标悬停在导航按钮
ActionChains(driver).move_to_element(xuanting2).perform()
htgl = driver.find_element_by_xpath('//*[text()="合同管理"]')  # 点击“合同管理”节点
ActionChains(driver).move_to_element(htgl).perform()
qy = driver.find_element_by_xpath('/html/body/div[1]/section/section/div/div[2]/div[2]/div')  # 点击“合同签约”按钮
qy.click()
k = driver.find_element_by_xpath("/html/body/div[1]/section/section/header/div/div[3]/div[2]/span/img")  # 点击按钮后，为使页面全部展示，将鼠标悬停在头像处
ActionChains(driver).move_to_element(k).perform()
httz = driver.find_element_by_xpath("/html/body/div[1]/section/section/main/div/div[2]/div[2]/iframe")  # 获取页面的句柄
driver.switch_to.frame(httz)
driver.find_element_by_xpath("/html/body/div/div[2]/div/div[3]/div[3]/div[1]/div[1]/div/div/button[1]").click()  #点击刷新按钮
time.sleep(2)
currentPageUrl = driver.current_url
print("当前页面的url是：", currentPageUrl)     # 获取当前URL地址
code = requests.get(currentPageUrl).status_code
print("合同签约状态码校验:{}".format(code))   # 获取当前URL的状态码
driver.refresh()   #刷新整个页面
xuanting2 = driver.find_element_by_class_name("menuImg_box")  # 鼠标悬停在导航按钮
ActionChains(driver).move_to_element(xuanting2).perform()
htgl = driver.find_element_by_xpath('//*[text()="合同管理"]')  # 点击“合同管理”节点
ActionChains(driver).move_to_element(htgl).perform()
qy = driver.find_element_by_xpath('/html/body/div[1]/section/section/div/div[2]/div[3]/div')  # 点击“合同结清”按钮
qy.click()
k = driver.find_element_by_xpath("/html/body/div[1]/section/section/header/div/div[3]/div[2]/span/img")  # 点击按钮后，为使页面全部展示，将鼠标悬停在头像处
ActionChains(driver).move_to_element(k).perform()
httz = driver.find_element_by_xpath("/html/body/div[1]/section/section/main/div/div[2]/div[2]/iframe")  # 获取页面的句柄
driver.switch_to.frame(httz)
driver.find_element_by_xpath("/html/body/div/div[2]/div[3]/div[3]/div[1]/div[1]/div/div/button[1]").click()  #点击刷新按钮
time.sleep(2)
currentPageUrl = driver.current_url
print("当前页面的url是：", currentPageUrl)     # 获取当前URL地址
code = requests.get(currentPageUrl).status_code
print("合同结清状态码校验:{}".format(code))   # 获取当前URL的状态码
driver.refresh()   #刷新整个页面
xuanting2 = driver.find_element_by_class_name("menuImg_box")  # 鼠标悬停在导航按钮
ActionChains(driver).move_to_element(xuanting2).perform()
htgl = driver.find_element_by_xpath('//*[text()="合同管理"]')  # 点击“合同管理”节点
ActionChains(driver).move_to_element(htgl).perform()
qy = driver.find_element_by_xpath('/html/body/div[1]/section/section/div/div[2]/div[4]/div')  # 点击“合同提前结清”按钮
qy.click()
k = driver.find_element_by_xpath("/html/body/div[1]/section/section/header/div/div[3]/div[2]/span/img")  # 点击按钮后，为使页面全部展示，将鼠标悬停在头像处
ActionChains(driver).move_to_element(k).perform()
httz = driver.find_element_by_xpath("/html/body/div[1]/section/section/main/div/div[2]/div[2]/iframe")  # 获取页面的句柄
driver.switch_to.frame(httz)
driver.find_element_by_xpath("/html/body/div/div[2]/div[3]/div[3]/div[1]/div[1]/div[1]/div/button[1]").click()  #点击刷新按钮
time.sleep(5)
currentPageUrl = driver.current_url
print("当前页面的url是：", currentPageUrl)     # 获取当前URL地址
code = requests.get(currentPageUrl).status_code
print("合同提前结清状态码校验:{}".format(code))   # 获取当前URL的状态码
driver.refresh()   #刷新整个页面
xuanting2 = driver.find_element_by_class_name("menuImg_box")  # 鼠标悬停在导航按钮
ActionChains(driver).move_to_element(xuanting2).perform()
htgl = driver.find_element_by_xpath('//*[text()="变更管理"]')  # 点击“变更管理”节点
ActionChains(driver).move_to_element(htgl).perform()
qy = driver.find_element_by_xpath('/html/body/div[1]/section/section/div/div[2]/div[1]/div')  # 点击“变更管理”按钮
qy.click()
k = driver.find_element_by_xpath("/html/body/div[1]/section/section/header/div/div[3]/div[2]/span/img")  # 点击按钮后，为使页面全部展示，将鼠标悬停在头像处
ActionChains(driver).move_to_element(k).perform()
httz = driver.find_element_by_xpath("/html/body/div[1]/section/section/main/div/div[2]/div[2]/iframe")  # 获取页面的句柄
driver.switch_to.frame(httz)
driver.find_element_by_xpath("/html/body/div/div[2]/div/div[3]/div[3]/div[1]/div[1]/div[1]/div/button[1]").click()  #点击刷新按钮
time.sleep(2)
currentPageUrl = driver.current_url
print("当前页面的url是：", currentPageUrl)     # 获取当前URL地址
code = requests.get(currentPageUrl).status_code
print("变更管理状态码校验:{}".format(code))   # 获取当前URL的状态码
driver.refresh()   #刷新整个页面
xuanting2 = driver.find_element_by_class_name("menuImg_box")  # 鼠标悬停在导航按钮
ActionChains(driver).move_to_element(xuanting2).perform()
htgl = driver.find_element_by_xpath('//*[text()="变更管理"]')  # 点击“变更管理”节点
ActionChains(driver).move_to_element(htgl).perform()
qy = driver.find_element_by_xpath('/html/body/div[1]/section/section/div/div[2]/div[2]/div')  # 点击“签约前项目变更”按钮
qy.click()
k = driver.find_element_by_xpath("/html/body/div[1]/section/section/header/div/div[3]/div[2]/span/img")  # 点击按钮后，为使页面全部展示，将鼠标悬停在头像处
ActionChains(driver).move_to_element(k).perform()
httz = driver.find_element_by_xpath("/html/body/div[1]/section/section/main/div/div[2]/div[2]/iframe")  # 获取页面的句柄
driver.switch_to.frame(httz)
driver.find_element_by_xpath("/html/body/div/div/div[1]/div/div[3]/div[3]/div[1]/div[1]/div/div/button[1]").click()  #点击刷新按钮
time.sleep(2)
currentPageUrl = driver.current_url
print("当前页面的url是：", currentPageUrl)     # 获取当前URL地址
code = requests.get(currentPageUrl).status_code
print("签约前项目变更状态码校验:{}".format(code))   # 获取当前URL的状态码
driver.refresh()   #刷新整个页面
xuanting2 = driver.find_element_by_class_name("menuImg_box")  # 鼠标悬停在导航按钮
ActionChains(driver).move_to_element(xuanting2).perform()
htgl = driver.find_element_by_xpath('//*[text()="变更管理"]')  # 点击“变更管理”节点
ActionChains(driver).move_to_element(htgl).perform()
qy = driver.find_element_by_xpath('/html/body/div[1]/section/section/div/div[2]/div[3]/div')  # 点击“签约后项目变更”按钮
qy.click()
k = driver.find_element_by_xpath("/html/body/div[1]/section/section/header/div/div[3]/div[2]/span/img")  # 点击按钮后，为使页面全部展示，将鼠标悬停在头像处
ActionChains(driver).move_to_element(k).perform()
httz = driver.find_element_by_xpath("/html/body/div[1]/section/section/main/div/div[2]/div[2]/iframe")  # 获取页面的句柄
driver.switch_to.frame(httz)
driver.find_element_by_xpath("/html/body/div/div[2]/div[1]/div/div[3]/div[3]/div[1]/div[1]/div/div/button[1]").click()  #点击刷新按钮
time.sleep(2)
currentPageUrl = driver.current_url
print("当前页面的url是：", currentPageUrl)     # 获取当前URL地址
code = requests.get(currentPageUrl).status_code
print("签约后项目变更状态码校验:{}".format(code))   # 获取当前URL的状态码
driver.refresh()   #刷新整个页面
xuanting2 = driver.find_element_by_class_name("menuImg_box")  # 鼠标悬停在导航按钮
ActionChains(driver).move_to_element(xuanting2).perform()
htgl = driver.find_element_by_xpath('//*[text()="收付款管理"]')  # 点击“收付款管理”节点
ActionChains(driver).move_to_element(htgl).perform()
qy = driver.find_element_by_xpath('/html/body/div[1]/section/section/div/div[2]/div[1]/div')  # 点击“收付款查询”按钮
qy.click()
k = driver.find_element_by_xpath("/html/body/div[1]/section/section/header/div/div[3]/div[2]/span/img")  # 点击按钮后，为使页面全部展示，将鼠标悬停在头像处
ActionChains(driver).move_to_element(k).perform()
httz = driver.find_element_by_xpath("/html/body/div[1]/section/section/main/div/div[2]/div[2]/iframe")  # 获取页面的句柄
driver.switch_to.frame(httz)
driver.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/div/div[1]/div[1]/div/div/button[1]").click()  #点击刷新按钮
time.sleep(2)
currentPageUrl = driver.current_url
print("当前页面的url是：", currentPageUrl)     # 获取当前URL地址
code = requests.get(currentPageUrl).status_code
print("收付款查询状态码校验:{}".format(code))   # 获取当前URL的状态码
driver.refresh()   #刷新整个页面
xuanting2 = driver.find_element_by_class_name("menuImg_box")  # 鼠标悬停在导航按钮
ActionChains(driver).move_to_element(xuanting2).perform()
htgl = driver.find_element_by_xpath('//*[text()="收付款管理"]')  # 点击“收付款管理”节点
ActionChains(driver).move_to_element(htgl).perform()
qy = driver.find_element_by_xpath('/html/body/div[1]/section/section/div/div[2]/div[2]/div')  # 点击“付款申请”按钮
qy.click()
k = driver.find_element_by_xpath("/html/body/div[1]/section/section/header/div/div[3]/div[2]/span/img")  # 点击按钮后，为使页面全部展示，将鼠标悬停在头像处
ActionChains(driver).move_to_element(k).perform()
httz = driver.find_element_by_xpath("/html/body/div[1]/section/section/main/div/div[2]/div[2]/iframe")  # 获取页面的句柄
driver.switch_to.frame(httz)
driver.find_element_by_xpath("/html/body/div/div[2]/div/div/div[3]/div[3]/div[1]/div[1]/div/div/button").click()  #点击刷新按钮
time.sleep(2)
currentPageUrl = driver.current_url
print("当前页面的url是：", currentPageUrl)     # 获取当前URL地址
code = requests.get(currentPageUrl).status_code
print("付款申请状态码校验:{}".format(code))   # 获取当前URL的状态码
driver.refresh()   #刷新整个页面
xuanting2 = driver.find_element_by_class_name("menuImg_box")  # 鼠标悬停在导航按钮
ActionChains(driver).move_to_element(xuanting2).perform()
htgl = driver.find_element_by_xpath('//*[text()="收付款管理"]')  # 点击“收付款管理”节点
ActionChains(driver).move_to_element(htgl).perform()
qy = driver.find_element_by_xpath('/html/body/div[1]/section/section/div/div[2]/div[3]/div')  # 点击“付款申请”按钮
qy.click()
k = driver.find_element_by_xpath("/html/body/div[1]/section/section/header/div/div[3]/div[2]/span/img")  # 点击按钮后，为使页面全部展示，将鼠标悬停在头像处
ActionChains(driver).move_to_element(k).perform()
httz = driver.find_element_by_xpath("/html/body/div[1]/section/section/main/div/div[2]/div[2]/iframe")  # 获取页面的句柄
driver.switch_to.frame(httz)
driver.find_element_by_xpath("/html/body/div/div[2]/div[1]/div[3]/div[3]/div[1]/div[1]/div/div/button").click()  #点击刷新按钮
time.sleep(2)
currentPageUrl = driver.current_url
print("当前页面的url是：", currentPageUrl)     # 获取当前URL地址
code = requests.get(currentPageUrl).status_code
print("批量付款申请状态码校验:{}".format(code))   # 获取当前URL的状态码
driver.refresh()   #刷新整个页面
xuanting2 = driver.find_element_by_class_name("menuImg_box")  # 鼠标悬停在导航按钮
ActionChains(driver).move_to_element(xuanting2).perform()
htgl = driver.find_element_by_xpath('//*[text()="租后风险管理"]')  # 点击“租后风险管理”节点
ActionChains(driver).move_to_element(htgl).perform()
qy = driver.find_element_by_xpath('/html/body/div[1]/section/section/div/div[2]/div[1]/div')  # 点击“风险金台账”按钮
qy.click()
k = driver.find_element_by_xpath("/html/body/div[1]/section/section/header/div/div[3]/div[2]/span/img")  # 点击按钮后，为使页面全部展示，将鼠标悬停在头像处
ActionChains(driver).move_to_element(k).perform()
httz = driver.find_element_by_xpath("/html/body/div[1]/section/section/main/div/div[2]/div[2]/iframe")  # 获取页面的句柄
driver.switch_to.frame(httz)
driver.find_element_by_xpath("/html/body/div/div[2]/div/div[2]/div/div[1]/div[1]/div/div/button").click()  #点击刷新按钮
time.sleep(2)
currentPageUrl = driver.current_url
print("当前页面的url是：", currentPageUrl)     # 获取当前URL地址
code = requests.get(currentPageUrl).status_code
print("租后风险管理状态码校验:{}".format(code))   # 获取当前URL的状态码
driver.refresh()   #刷新整个页面
xuanting2 = driver.find_element_by_class_name("menuImg_box")  # 鼠标悬停在导航按钮
ActionChains(driver).move_to_element(xuanting2).perform()
htgl = driver.find_element_by_xpath('//*[text()="租后风险管理"]')  # 点击“租后风险管理”节点
ActionChains(driver).move_to_element(htgl).perform()
qy = driver.find_element_by_xpath('/html/body/div[1]/section/section/div/div[2]/div[2]/div')  # 点击“风险金处理”按钮
qy.click()
k = driver.find_element_by_xpath("/html/body/div[1]/section/section/header/div/div[3]/div[2]/span/img")  # 点击按钮后，为使页面全部展示，将鼠标悬停在头像处
ActionChains(driver).move_to_element(k).perform()
httz = driver.find_element_by_xpath("/html/body/div[1]/section/section/main/div/div[2]/div[2]/iframe")  # 获取页面的句柄
driver.switch_to.frame(httz)
driver.find_element_by_xpath("/html/body/div/div[2]/div/div[2]/div[3]/div[3]/div/div[1]/div[1]/div/div/button[1]").click()  #点击刷新按钮
time.sleep(5)
currentPageUrl = driver.current_url
print("当前页面的url是：", currentPageUrl)     # 获取当前URL地址
code = requests.get(currentPageUrl).status_code
print("风险金台账状态码校验:{}".format(code))   # 获取当前URL的状态码
driver.refresh()   #刷新整个页面
xuanting2 = driver.find_element_by_class_name("menuImg_box")  # 鼠标悬停在导航按钮
ActionChains(driver).move_to_element(xuanting2).perform()
htgl = driver.find_element_by_xpath('//*[text()="租后风险管理"]')  # 点击“租后风险管理”节点
ActionChains(driver).move_to_element(htgl).perform()
qy = driver.find_element_by_xpath('/html/body/div[1]/section/section/div/div[2]/div[3]/div')  # 点击“违约金台账”按钮
qy.click()
k = driver.find_element_by_xpath("/html/body/div[1]/section/section/header/div/div[3]/div[2]/span/img")  # 点击按钮后，为使页面全部展示，将鼠标悬停在头像处
ActionChains(driver).move_to_element(k).perform()
httz = driver.find_element_by_xpath("/html/body/div[1]/section/section/main/div/div[2]/div[2]/iframe")  # 获取页面的句柄
driver.switch_to.frame(httz)
driver.find_element_by_xpath("/html/body/div/div/div/div[2]/div[1]/div[1]/div/button[1]").click()  #点击刷新按钮
time.sleep(2)
currentPageUrl = driver.current_url
print("当前页面的url是：", currentPageUrl)     # 获取当前URL地址
code = requests.get(currentPageUrl).status_code
print("违约金台账状态码校验:{}".format(code))   # 获取当前URL的状态码
driver.refresh()   #刷新整个页面
xuanting2 = driver.find_element_by_class_name("menuImg_box")  # 鼠标悬停在导航按钮
ActionChains(driver).move_to_element(xuanting2).perform()
htgl = driver.find_element_by_xpath('//*[text()="租后风险管理"]')  # 点击“租后风险管理”节点
ActionChains(driver).move_to_element(htgl).perform()
qy = driver.find_element_by_xpath('/html/body/div[1]/section/section/div/div[2]/div[4]/div')  # 点击“违约金减免”按钮
qy.click()
k = driver.find_element_by_xpath("/html/body/div[1]/section/section/header/div/div[3]/div[2]/span/img")  # 点击按钮后，为使页面全部展示，将鼠标悬停在头像处
ActionChains(driver).move_to_element(k).perform()
httz = driver.find_element_by_xpath("/html/body/div[1]/section/section/main/div/div[2]/div[2]/iframe")  # 获取页面的句柄
driver.switch_to.frame(httz)
driver.find_element_by_xpath("/html/body/div/div/div[2]/div[3]/div[1]/div/div[1]/div[1]/div/button[1]").click()  #点击刷新按钮
time.sleep(2)
currentPageUrl = driver.current_url
print("当前页面的url是：", currentPageUrl)     # 获取当前URL地址
code = requests.get(currentPageUrl).status_code
print("违约金减免状态码校验:{}".format(code))   # 获取当前URL的状态码
driver.refresh()   #刷新整个页面
xuanting2 = driver.find_element_by_class_name("menuImg_box")  # 鼠标悬停在导航按钮
ActionChains(driver).move_to_element(xuanting2).perform()
htgl = driver.find_element_by_xpath('//*[text()="租后风险管理"]')  # 点击“租后风险管理”节点
ActionChains(driver).move_to_element(htgl).perform()
qy = driver.find_element_by_xpath('/html/body/div[1]/section/section/div/div[2]/div[5]/div')  # 点击“回访安排”按钮
qy.click()
k = driver.find_element_by_xpath("/html/body/div[1]/section/section/header/div/div[3]/div[2]/span/img")  # 点击按钮后，为使页面全部展示，将鼠标悬停在头像处
ActionChains(driver).move_to_element(k).perform()
httz = driver.find_element_by_xpath("/html/body/div[1]/section/section/main/div/div[2]/div[2]/iframe")  # 获取页面的句柄
driver.switch_to.frame(httz)
driver.find_element_by_xpath("/html/body/div/div[2]/div/div[2]/div/div[1]/div[1]/div/div/button[1]").click()  #点击刷新按钮
time.sleep(2)
currentPageUrl = driver.current_url
print("当前页面的url是：", currentPageUrl)     # 获取当前URL地址
code = requests.get(currentPageUrl).status_code
print("回访安排状态码校验:{}".format(code))   # 获取当前URL的状态码
driver.refresh()   #刷新整个页面
xuanting2 = driver.find_element_by_class_name("menuImg_box")  # 鼠标悬停在导航按钮
ActionChains(driver).move_to_element(xuanting2).perform()
htgl = driver.find_element_by_xpath('//*[text()="租后风险管理"]')  # 点击“租后风险管理”节点
ActionChains(driver).move_to_element(htgl).perform()
qy = driver.find_element_by_xpath('/html/body/div[1]/section/section/div/div[2]/div[6]/div')  # 点击“现场检查”按钮
qy.click()
k = driver.find_element_by_xpath("/html/body/div[1]/section/section/header/div/div[3]/div[2]/span/img")  # 点击按钮后，为使页面全部展示，将鼠标悬停在头像处
ActionChains(driver).move_to_element(k).perform()
httz = driver.find_element_by_xpath("/html/body/div[1]/section/section/main/div/div[2]/div[2]/iframe")  # 获取页面的句柄
driver.switch_to.frame(httz)
driver.find_element_by_xpath("/html/body/div/div[2]/div/div/div[2]/div/div[1]/div[1]/div/div/button[1]").click()  #点击刷新按钮
time.sleep(2)
currentPageUrl = driver.current_url
print("当前页面的url是：", currentPageUrl)     # 获取当前URL地址
code = requests.get(currentPageUrl).status_code
print("现场检查状态码校验:{}".format(code))   # 获取当前URL的状态码
driver.refresh()   #刷新整个页面
xuanting2 = driver.find_element_by_class_name("menuImg_box")  # 鼠标悬停在导航按钮
ActionChains(driver).move_to_element(xuanting2).perform()
htgl = driver.find_element_by_xpath('//*[text()="租后风险管理"]')  # 点击“租后风险管理”节点
ActionChains(driver).move_to_element(htgl).perform()
qy = driver.find_element_by_xpath('/html/body/div[1]/section/section/div/div[2]/div[7]/div')  # 点击“资产风险“按钮
qy.click()
k = driver.find_element_by_xpath("/html/body/div[1]/section/section/header/div/div[3]/div[2]/span/img")  # 点击按钮后，为使页面全部展示，将鼠标悬停在头像处
ActionChains(driver).move_to_element(k).perform()
httz = driver.find_element_by_xpath("/html/body/div[1]/section/section/main/div/div[2]/div[2]/iframe")  # 获取页面的句柄
driver.switch_to.frame(httz)
driver.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/div[1]/div[1]/div/button").click()  #点击刷新按钮
time.sleep(2)
currentPageUrl = driver.current_url
print("当前页面的url是：", currentPageUrl)     # 获取当前URL地址
code = requests.get(currentPageUrl).status_code
print("资产风险评定状态码校验:{}".format(code))   # 获取当前URL的状态码
driver.refresh()   #刷新整个页面
xuanting2 = driver.find_element_by_class_name("menuImg_box")  # 鼠标悬停在导航按钮
ActionChains(driver).move_to_element(xuanting2).perform()
htgl = driver.find_element_by_xpath('//*[text()="报表中心"]')  # 点击“报表中心”节点
ActionChains(driver).move_to_element(htgl).perform()
qy = driver.find_element_by_xpath('/html/body/div[1]/section/section/div/div[2]/div[1]/div')  # 点击“贷款日均报“按钮
qy.click()
k = driver.find_element_by_xpath("/html/body/div[1]/section/section/header/div/div[3]/div[2]/span/img")  # 点击按钮后，为使页面全部展示，将鼠标悬停在头像处
ActionChains(driver).move_to_element(k).perform()
httz = driver.find_element_by_xpath("/html/body/div[1]/section/section/main/div/div[2]/div[2]/iframe")  # 获取页面的句柄
driver.switch_to.frame(httz)
driver.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/div/div[1]/div[1]/div/div/button[1]").click()  #点击刷新按钮
time.sleep(2)
currentPageUrl = driver.current_url
print("当前页面的url是：", currentPageUrl)     # 获取当前URL地址
code = requests.get(currentPageUrl).status_code
print("贷款日均报状态码校验:{}".format(code))   # 获取当前URL的状态码
driver.refresh()   #刷新整个页面
xuanting2 = driver.find_element_by_class_name("menuImg_box")  # 鼠标悬停在导航按钮
ActionChains(driver).move_to_element(xuanting2).perform()
htgl = driver.find_element_by_xpath('//*[text()="报表中心"]')  # 点击“报表中心”节点
ActionChains(driver).move_to_element(htgl).perform()
qy = driver.find_element_by_xpath('/html/body/div[1]/section/section/div/div[2]/div[2]/div')  # 点击“合同基本信息“按钮
qy.click()
k = driver.find_element_by_xpath("/html/body/div[1]/section/section/header/div/div[3]/div[2]/span/img")  # 点击按钮后，为使页面全部展示，将鼠标悬停在头像处
ActionChains(driver).move_to_element(k).perform()
httz = driver.find_element_by_xpath("/html/body/div[1]/section/section/main/div/div[2]/div[2]/iframe")  # 获取页面的句柄
driver.switch_to.frame(httz)
driver.find_element_by_xpath("/html/body/div/div[2]/div/div/div/div[1]/div/button").click()  #点击刷新按钮
time.sleep(2)
currentPageUrl = driver.current_url
print("当前页面的url是：", currentPageUrl)     # 获取当前URL地址
code = requests.get(currentPageUrl).status_code
print("合同基本信息状态码校验:{}".format(code))   # 获取当前URL的状态码
driver.refresh()   #刷新整个页面
xuanting2 = driver.find_element_by_class_name("menuImg_box")  # 鼠标悬停在导航按钮
ActionChains(driver).move_to_element(xuanting2).perform()
htgl = driver.find_element_by_xpath('//*[text()="报表中心"]')  # 点击“报表中心”节点
ActionChains(driver).move_to_element(htgl).perform()
qy = driver.find_element_by_xpath('/html/body/div[1]/section/section/div/div[2]/div[3]/div')  # 点击“在审项目明细“按钮
qy.click()
k = driver.find_element_by_xpath("/html/body/div[1]/section/section/header/div/div[3]/div[2]/span/img")  # 点击按钮后，为使页面全部展示，将鼠标悬停在头像处
ActionChains(driver).move_to_element(k).perform()
httz = driver.find_element_by_xpath("/html/body/div[1]/section/section/main/div/div[2]/div[2]/iframe")  # 获取页面的句柄
driver.switch_to.frame(httz)
driver.find_element_by_xpath("/html/body/div/div[2]/div/div/div/div[1]/div/button").click()  #点击刷新按钮
time.sleep(2)
currentPageUrl = driver.current_url
print("当前页面的url是：", currentPageUrl)     # 获取当前URL地址
code = requests.get(currentPageUrl).status_code
print("在审项目明细状态码校验:{}".format(code))   # 获取当前URL的状态码
driver.refresh()   #刷新整个页面
xuanting2 = driver.find_element_by_class_name("menuImg_box")  # 鼠标悬停在导航按钮
ActionChains(driver).move_to_element(xuanting2).perform()
htgl = driver.find_element_by_xpath('//*[text()="报表中心"]')  # 点击“报表中心”节点
ActionChains(driver).move_to_element(htgl).perform()
qy = driver.find_element_by_xpath('/html/body/div[1]/section/section/div/div[2]/div[4]/div')  # 点击“自主审批项目用时审批表“按钮
qy.click()
k = driver.find_element_by_xpath("/html/body/div[1]/section/section/header/div/div[3]/div[2]/span/img")  # 点击按钮后，为使页面全部展示，将鼠标悬停在头像处
ActionChains(driver).move_to_element(k).perform()
httz = driver.find_element_by_xpath("/html/body/div[1]/section/section/main/div/div[2]/div[2]/iframe")  # 获取页面的句柄
driver.switch_to.frame(httz)
driver.find_element_by_xpath("/html/body/div/div[2]/div[2]/div[2]/button[1]").click()
driver.find_element_by_xpath("/html/body/div/div[2]/div[2]/div[2]/button[2]").click()
driver.find_element_by_xpath("/html/body/div/div[2]/div[2]/div[2]/button[3]").click()
driver.find_element_by_xpath("/html/body/div/div[2]/div[2]/div[2]/button[4]").click()
time.sleep(2)
currentPageUrl = driver.current_url
print("当前页面的url是：", currentPageUrl)     # 获取当前URL地址
code = requests.get(currentPageUrl).status_code
print("自主审批项目用时审批表状态码校验:{}".format(code))   # 获取当前URL的状态码
driver.refresh()   #刷新整个页面
time.sleep(5)
driver.close()  # 关闭进程