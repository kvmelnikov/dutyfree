import csv

from spoiled.models import Shop, Nomenclature, Group

def run():
    fhand = open('spoiled/mytable_csv.csv')
    reader = csv.reader(fhand)
    next(reader)

    Nomenclature.objects.all().delete()
    Shop.objects.all().delete()

    s1 = Shop(name='Flagman')
    s2 = Shop(name="Apsny")
    s1.save()
    s2.save()


    for row in reader:
        try:
            inv = float((row[6].replace(',','.')).replace(' ', ''))
            sale = float((row[7].replace(',','.')).replace(' ', ''))
            group = Group(name=row[2])
            group.save()
            n = Nomenclature(shop=s2, name=row[4], barcode=row[0],
                                 inv_price=inv, sale_price=sale,
                                          plu=row[3], group=group, characteristic=row[1], unit=row[5])
            n.save()
        except ValueError:
            print("except", row)