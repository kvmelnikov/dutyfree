import csv

from spoiled.models import Shop, Nomenclature

def run():

    Nomenclature.objects.all().delete()
    Shop.objects.all().delete()