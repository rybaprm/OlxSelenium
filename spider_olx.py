from time import sleep
from pprint import pprint

from selenium import webdriver
from selenium.webdriver.firefox.options import Options

# Declared default variable - search link of the site olx.ua
START_URL = '''https://www.olx.ua/nedvizhimost/zaporozhe/?search%5B
filter_float_price%3Afrom%5D=10000&search%5B
filter_float_price%3Ato%5D=23000&search%5Bdistrict_id%5D
=51&currency=USD'''

# Declared xpath variable for search to the site olx.ua
# xpath_olx_ad - xpath for find elements consist data of ad
xpath_olx_ad = '//*[@id="offers_table"]/tbody/tr[@class="wrap"]'
# xpath_olx_ad_url - xpath for find url in some ad data
xpath_olx_ad_url = './/*/div/h3/a'
# xpath_olx_ad_text - xpath for find text in some ad data
xpath_olx_ad_text = './/*/div/h3/a/strong'
# xpath_olx_ad_date - xpath for find date in some ad data
xpath_olx_ad_date = './/*/div[@class ="space rel"]/p/small[2]/span'
# xpath_olx_ad_price - xpath for find price in some ad data
xpath_olx_ad_price = './/*/div/p[@class="price"]/strong'
# xpath_olx_next_page - xpath for find elements consist url of next page
xpath_olx_next_page = '//*/span[@class="fbold next abs large"]/a'


# Declared class - search spider, consist some method's:
# __init__(), stop(), parse(), parse_pages()
class OlxSpider():
    # call's once, when create instants of class - method that create hidden
    # browser for parsing
    def __init__(self,start_url=START_URL):
        opts = Options() # call optoins for Firefox browser
        opts.set_headless()
        assert opts.headless # set hidden mode for browser
        self.browser = webdriver.Firefox(options=opts) # run browser
        self.browser.get(start_url) # open start_url

    # method that stops the browser
    def stop(self):
        self.browser.close() # close browser

    # method that parse ad elements on the page
    def parse(self):
        self.browser.delete_all_cookies() # delete cookies on browser
        sleep(1) # wait 1 second
        # loop that iterate ad elements on the page by XPATH
        for olx_ad in self.browser.find_elements_by_xpath(xpath_olx_ad):
            ad_url = olx_ad.find_element_by_xpath(
                xpath_olx_ad_url).get_attribute('href') # find URL of ad
            ad_text = olx_ad.find_element_by_xpath(
                xpath_olx_ad_text).text # find text of ad
            ad_date = olx_ad.find_element_by_xpath(
                xpath_olx_ad_date).text # find date of ad
            ad_price = olx_ad.find_element_by_xpath(
                xpath_olx_ad_price).text.strip('$').replace(' ','') # ad price
            # return dictionary that consist elements: link, text, date, price
            # of ad
            yield {
                'link': ad_url.split('#')[0],
                'text': ad_text.encode("cp1251", "ignore").decode("cp1251"),
                'date': ad_date,
                'price': ad_price
            }
        sleep(1) # wait 1 second
        self.browser.delete_all_cookies() # delete cookies on browser

    # method that that parse all pages in pagination
    def parse_pages(self):
        # endless loop
        while True:
            # loop that iterate ad elements (dictionary) return in the
            # method parse()
            for url in self.parse():
                pprint(url) # print value of dictionary url (consist
                            # elements of ad on the page)
            next_page = self.browser.find_elements_by_xpath(
                xpath_olx_next_page) # find next page
            # check for next page
            if next_page:
                # if next page exists - go to it
                self.browser.get(next_page[0].get_attribute('href'))
            else:
                # if next page not exists (end of pagination) - out of loop
                # 'while'
                break

        self.stop() # close hidden browser by using metod stop()