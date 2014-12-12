# coding=utf-8
import os
import sys
from subprocess import call

import django
from django.utils import timezone
from django.conf import settings


os.environ.setdefault(
    "DJANGO_SETTINGS_MODULE",
    "advchecker.settings"
)
django.setup()

sys.path = [settings.BASE_DIR] + sys.path

from campagnes.models import PlanificationCampagne


class SnapRobot:
    def __init__(self, web_driver):
        self.driver = web_driver

    def go_to_url(self, url):
        self.driver.get(url)

    def take_screenshot(self, folder, filename):
        print("----Screenshot : %s" % filename)
        call(["mkdir", "-p", settings.MEDIA_ROOT + '/screenshots/' + folder])
        self.driver.set_window_size(1920, 1080)
        scheight = .1
        while scheight < 9.9:
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight/%s);" % scheight)
            scheight += .1
        self.driver.execute_script("window.scrollTo(0, 0);")
        self.driver.save_screenshot(settings.MEDIA_ROOT + '/screenshots/' + filename)


if __name__ == '__main__':
    query_tests = PlanificationCampagne.objects.filter(
        status="WAIT"
    ).filter(
        date_execution__lte=timezone.localtime(timezone.now())
    )

    if not query_tests:
        print("----Aucun nouveaux tests a faire")
        sys.exit(0)

    for test in query_tests:
        imp = __import__("crowlers.%s" % test.magasin.enseigne.nom.lower(), fromlist=['Crowler'])

        crowler = imp.Crowler()
        print("----Navigation vers %s>%s>%s" % (test.magasin.enseigne.nom, test.magasin.ville, test.rayon))
        crowler.execute(test)
