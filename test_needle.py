from needle.cases import NeedleTestCase
from needle.driver import NeedlePhantomJS
from selenium.webdriver.common.keys import Keys


# class BBCNewsTest(NeedleTestCase):
#
#     @classmethod
#     def get_web_driver(cls):
#         return NeedlePhantomJS()
#
#     def test_masthead(self):
#         self.driver.get('http://www.bbc.co.uk/news/')
#         self.assertScreenshot('#blq-mast', 'bbc-masthead')


class AuchanTest(NeedleTestCase):

    @classmethod
    def get_web_driver(cls):
        return NeedlePhantomJS()

    def test_carrousel(self):
        self.driver.get('http://www.auchandrive.fr/')
        champs_map = self.driver.find_element_by_name('champs_map')
        champs_map.send_keys("Plaisir", Keys.ENTER)
        drive = self.driver.find_element_by_xpath('//*[@id="liste_drives"]/ul/li[1]/span/a')
        drive.click()
        drive = self.driver.find_element_by_xpath('/html/body/div/div[3]/div[2]/a')
        drive.click()
        self.driver.execute_script("document.getElementsByClassName('slide0')[0].style.zIndex = '50';")
        self.driver.execute_script("document.getElementsByClassName('slide0')[0].style.display = 'block';")
        self.assertScreenshot('.slide0', 'slide0')
        self.driver.execute_script("document.getElementsByClassName('slide1')[0].style.zIndex = '51';")
        self.driver.execute_script("document.getElementsByClassName('slide1')[0].style.display = 'block';")
        self.assertScreenshot('.slide1', 'slide1')
        self.driver.execute_script("document.getElementsByClassName('slide2')[0].style.zIndex = '52';")
        self.driver.execute_script("document.getElementsByClassName('slide2')[0].style.display = 'block';")
        self.assertScreenshot('.slide2', 'slide2')
        self.driver.execute_script("document.getElementsByClassName('slide4')[0].style.zIndex = '53';")
        self.driver.execute_script("document.getElementsByClassName('slide4')[0].style.display = 'block';")
        self.assertScreenshot('.slide4', 'slide4')
