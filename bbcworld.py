import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome('/Users/powermac/Downloads/chromedriver')
base_url = u'https://twitter.com/'
query_bbc = u'BBCWorld'
query_economist = u'TheEconomist'
query_time = u'TIME'
query_ap = u'AP'
query_nashscene = u'NashvilleScene'
query_nc5 = u'NC5'


url = base_url + query_bbc
browser.get(url)
time.sleep(1)

body = browser.find_element_by_tag_name('body')

for _ in range(5):
    body.send_keys(Keys.PAGE_DOWN)
    time.sleep(0.2)

tweets = browser.find_elements_by_class_name('tweet-text')
print('BBC World')
for tweet in tweets:
    print("**********")
    print(tweet.text)







