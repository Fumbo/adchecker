# coding=utf-8
import re

from selenium import webdriver

from wrapper import SnapRobot
from campagnes.models import Enseigne


class Crowler(SnapRobot):
    def __init__(self):
        SnapRobot.__init__(self,
                           web_driver=webdriver.PhantomJS(service_log_path='/var/log/ghostdriver.log'))
        self.enseigne = Enseigne.objects.get(nom="Auchan")
        self.magasin = None
        self.driver.get(self.enseigne.url)

    def go_to_magasin(self, magasin):
        self.driver.add_cookie({'name': "auchanCook",
                                'value': re.search('-(\d+)$', magasin.identifiant).group(1) + '|',
                                'path': '/'})
        self.driver.add_cookie({'name': "gammePoisson2", 'value': '2', 'path': '/'})
        self.driver.get_cookies()
        self.driver.get(self.enseigne.url + 'drive/' + magasin.identifiant)
        self.magasin = magasin

    def go_to_rayon(self, full_path_rayon):
        if self.magasin:
            self.driver.get(self.enseigne.url + 'drive/' + self.magasin.identifiant + '/' +
                            full_path_rayon)

    def __del__(self):
        self.driver.quit()

    def execute(self, test):
        self.go_to_magasin(test.magasin)
        self.go_to_rayon(test.rayon.get_identifiant_path())
        folder = "%s_%s/%s/%s" % (test.campagne.id, test.campagne.nom, test.magasin.enseigne.nom,
                                  test.magasin.identifiant)
        screen_name = '%s/%s.png' % (folder, test.id)
        self.take_screenshot(folder, screen_name)
        test.screenshot = screen_name
        test.status = "PASS"
        test.save()
