from selenium import webdriver

def playVideo(s):
    driver = webdriver.Chrome()
    driver.get('https://www.youtube.com/results?search_query='+s)
    name = 'style-scope ytd-video-renderer'
    button = driver.find_element_by_class_name(name)
    button.click()
#s='kids+videos'
#playVideo(s)
