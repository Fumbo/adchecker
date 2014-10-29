from needle.cases import NeedleTestCase
from selenium.webdriver.common.keys import Keys

class AuchanTest(NeedleTestCase):
        
    def test_carrousel(self):
        """Test carrousel"""
        self.description = "Carrousel"
        self.driver.get('http://www.auchandrive.fr/')
        champs_map = self.driver.find_element_by_name('champs_map')
        champs_map.send_keys("Plaisir", Keys.ENTER)
        drive = self.driver.find_element_by_xpath('//*[@id="liste_drives"]/ul/li[1]/span/a')
        drive.click()
        drive = self.driver.find_element_by_xpath('/html/body/div/div[3]/div[2]/a')
        drive.click()
        self.driver.execute_script("document.getElementsByClassName('slide0 ')[0].style.zIndex = '50';")
        self.driver.execute_script("document.getElementsByClassName('slide0 ')[0].style.display = 'block';")
        self.assertScreenshot('.slide0 ', 'slide0 ')
        self.driver.execute_script("document.getElementsByClassName('slide1')[0].style.zIndex = '51';")
        self.driver.execute_script("document.getElementsByClassName('slide1')[0].style.display = 'block';")
        self.assertScreenshot('.slide1', 'slide1')
        self.driver.execute_script("document.getElementsByClassName('slide3')[0].style.zIndex = '52';")
        self.driver.execute_script("document.getElementsByClassName('slide3')[0].style.display = 'block';")
        self.assertScreenshot('.slide3', 'slide3')
