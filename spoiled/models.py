from django.db import models
from django.core.validators import MinLengthValidator
from django.conf import settings
# Create your models here.

class Shop(models.Model):
    name = models.CharField(
        max_length=200,
        help_text="Name shop",
        validators=[MinLengthValidator(2, "Shop must be greater than 1 character")]
    )
    def __str__(self):
        return self.name

class Group(models.Model):
    name = models.CharField(
        max_length=200,
        help_text="Name group",
        validators=[MinLengthValidator(2, "Shop must be greater than 1 character")]
    )

class Barcode(models.Model):
    name = models.CharField(
        max_length=20,
        help_text="Barcode"
    )

    def __str__(self):
        self.name

class Nomenclature(models.Model):
    name = models.CharField(
        max_length=200,
        help_text="Name shop",
        validators=[MinLengthValidator(2, "Shop must be greater than 1 character")]
    )
    plu = models.CharField(
        max_length=20,
        help_text="plu"
    )
    barcode = models.CharField(
        max_length=20,
        help_text="plu"
    )

    inv_price = models.FloatField(default=0)
    sale_price = models.FloatField(default=0)
    characteristic = models.CharField( max_length=200, help_text="characteristic", default="No")
    unit = models.CharField(max_length=10, help_text="unit", default="No")
    group = models.ForeignKey('Group', on_delete=models.CASCADE, null=False)
    shop = models.ForeignKey('Shop', on_delete=models.CASCADE, null=False)

    def __str__(self):
        return self.name

class Employee(models.Model):
    name = models.CharField(
        max_length=200,
        help_text="Name employee",
        validators=[MinLengthValidator(2, "Employee must be greater than 1 character")]
    )
    shop = models.ForeignKey('Shop', on_delete=models.CASCADE, null=False)

class Place(models.Model):
    name = models.CharField(
        max_length=200,
        help_text="Place spoiled",
        validators=[MinLengthValidator(2, "Place must be greater than 1 character")]
    )

    def __str__(self):
        return self.name

class Sub(models.Model):
    name = models.CharField(
        max_length=200,
        help_text="Sub spoiled",
        validators=[MinLengthValidator(2, "Sub must be greater than 1 character")]
    )

    def __str__(self):
        return self.name


class Spoiled(models.Model):
    comment = models.CharField(
        max_length=200,
        help_text="Что случилось",
        validators=[MinLengthValidator(2, "Employee must be greater than 1 character")]
    )

    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    quantity = models.IntegerField(default=0)
    picture = models.BinaryField(null=True, blank=True, editable=True)
    content_type = models.CharField(max_length=256, null=True, blank=True, help_text="The MIMEType of th file")
    name_photo = models.CharField(max_length=256, null=True, blank=True, help_text="Name foto")
    write_off = models.IntegerField(default=0)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=0, db_constraint=False)
    sub = models.ForeignKey('Sub', on_delete=models.CASCADE, null=True, db_constraint=True)
    place = models.ForeignKey('Place', on_delete=models.CASCADE, null=True, db_constraint=True)
    employee = models.ForeignKey('Employee', on_delete=models.CASCADE, null=True, db_constraint=False)
    nomenclature = models.ForeignKey('Nomenclature', on_delete=models.CASCADE, null=False, db_constraint=False)
    shop = models.ForeignKey('Shop', on_delete=models.CASCADE, null=False, db_constraint=True)

