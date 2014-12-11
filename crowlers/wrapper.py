# coding=utf-8
import os
import sys
from subprocess import call

import django
from django.utils import timezone


sys.path = [os.environ.get('ADCHECKER_ROOT', '../')] + sys.path

os.environ.setdefault(
    "DJANGO_SETTINGS_MODULE",
    "advchecker.settings"
)
django.setup()

import re
from selenium import webdriver
from campagnes.models import Enseigne, PlanificationCampagne


class SnapRobot:
    def __init__(self, web_driver, enseigne):
        self.driver = web_driver
        self.enseigne = enseigne

    def take_screenshot(self, folder, filename):
        call(["mkdir", "-p", os.environ.get('ADCHECKER_ROOT', '../') + 'static/screenshots/' + folder])
        self.driver.set_window_size(1920, 1080)
        scheight = .1
        while scheight < 9.9:
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight/%s);" % scheight)
            scheight += .1
        self.driver.execute_script("window.scrollTo(0, 0);")
        self.driver.save_screenshot(os.environ.get('ADCHECKER_ROOT', '../') + 'static/screenshots/' + filename)


class AuchanRobot(SnapRobot):
    def __init__(self):
        SnapRobot.__init__(self,
                           web_driver=webdriver.PhantomJS(),
                           enseigne=Enseigne.objects.get(nom="Auchan"))
        self.driver.get(self.enseigne.url)
        self.magasin = None

    def go_to_magasin(self, magasin):
        self.driver.add_cookie({'name': "auchanCook",
                                'value': re.search('-(\d+)$', magasin.identifiant).group(1) + '|',
                                'path': '/'})
        self.driver.add_cookie({'name': "gammePoisson2", 'value': '2', 'path': '/'})
        self.driver.get_cookies()
        self.driver.get(self.enseigne.url + 'drive/' + magasin.identifiant)
        self.magasin = magasin

    def go_to_rayon(self, full_path_rayon):
        self.driver.get(self.enseigne.url + 'drive/' + self.magasin.identifiant + '/' +
                        full_path_rayon)

    def __del__(self):
        self.driver.quit()


if __name__ == '__main__':
    auchan = AuchanRobot()
    query_tests = PlanificationCampagne.objects.filter(
        status="WAIT"
    ).filter(
        date_execution__lte=timezone.localtime(timezone.now())
    )
    if not query_tests:
        print("----Aucun nouveaux tests a faire")
        sys.exit(1)

    for test in query_tests:
        print("----Navigation sur %s>%s>%s" % (test.magasin.enseigne.nom, test.magasin.ville, test.rayon))
        auchan.go_to_magasin(test.magasin)
        auchan.go_to_rayon(test.rayon.get_identifiant_path())
        folder = "%s_%s/%s/%s" % (test.campagne.id, test.campagne.nom, test.magasin.enseigne.nom,
                                  test.magasin.identifiant)
        screen_name = '%s/%s.png' % (folder, test.id)
        print("----Screenshot : %s" % screen_name)
        auchan.take_screenshot(folder, screen_name)
        test.screenshot = screen_name
        test.status = "PASS"
        test.save()
    sys.exit(0)