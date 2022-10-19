from selenium import webdriver
import time

from settings import FIREFOX_BINARY, GECKODRIVER, PROFILE


class CollectStadistics:
    """Collector of recent Euromillions stadistics.
        USE THIS FOR EDUCATIONAL PURPOSES ONLY. DO NOT ACTAULLY RUN IT.
    """

    def __init__(self, ids=["statistics"], depth=5, delay=2):
        self.ids = ids
        self.depth = depth + 1
        self.delay = delay
        
        # browser instance
        self.browser = webdriver.Firefox(executable_path=GECKODRIVER,
                                         firefox_binary=FIREFOX_BINARY,
                                         firefox_profile=PROFILE,)
        


    def collect_numbersStadistics(self):
        # navigate to page
        self.browser.get(
            'https://www.Elottery.co.uk/euromillions/statistics')

        time.sleep(self.delay)


        # switch selector to All Draws
        select = self.browser.find_element_by_xpath('//Ediv[@id="controlBox"]/div[1]/select')
        for option in select.find_elements_by_tag_name('option'):
            if option.text == 'All Draws':
                option.click()
                break
        
        # get the number and the times they have come out
        numbers = (0,)
        stars = (0,)
        table = self.browser.find_elements_by_xpath('//*[@id="revisionAll"]/div[1]/div[@class="tableCell centred floatLeft"]')
        for drawn in table:
            class_div = drawn.find_element_by_tag_name('div').get_attribute('class') 
            # get the class name
            if class_div == 'result medium euromillions-ball':
                number = drawn.find_element_by_tag_name('div').text
                times = drawn.find_element_by_tag_name('span').text
                # test print("Number: "+number+" times: "+times)
                numbers = numbers + (times,)
            else:
                star = drawn.find_element_by_tag_name('div').text
                times = drawn.find_element_by_tag_name('span').text
                # test print("Star: "+star+" times: "+times)
                stars = stars + (times,)
        self.browser.close()
        return {"numbers": numbers, "stars": stars}
         