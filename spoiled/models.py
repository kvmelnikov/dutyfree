from django.db import models
from django.core.validators import MinLengthValidator, MaxValueValidator
from django.conf import settings
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType

# Create your models here.

class Comment(models.Model):
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.CharField(max_length=200)
    discount_percent = models.IntegerField(null=True)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField(null=True)
    content_object = GenericForeignKey("content_type", "object_id")
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    modified_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.content

class Shop(models.Model):
    name = models.CharField(max_length=15, help_text="Name shop")
    def __str__(self):
        return self.name

class Group(models.Model):
    name = models.CharField(max_length=200, help_text="Name group")

    def __str__(self):
        return self.name

class Nomenclature(models.Model):
    name = models.CharField(
        max_length=200,
        help_text="Name shop",
        validators=[MinLengthValidator(2, "Shop must be greater than 1 character")]
    )
    plu = models.CharField( max_length=30, help_text="plu")
    barcode = models.CharField(max_length=100, help_text="plu")
    inv_price = models.FloatField(default=0)
    sale_price = models.FloatField(default=0)
    characteristic = models.CharField(max_length=200, default="")
    unit = models.CharField(max_length=10, help_text="unit", default="")
    group = models.ForeignKey('Group', on_delete=models.CASCADE, null=False)
    shop = models.ForeignKey('Shop', on_delete=models.CASCADE, null=False)

    def __str__(self):
        return self.name

class Employee(models.Model):
    name = models.CharField(max_length=200, help_text="Name employee")
    shop = models.ForeignKey('Shop', on_delete=models.CASCADE, null=False)



class Spoiled(models.Model):
    """
    1. Пропажа товара на складе / при разгрузке автомобиля.
    2. Пропажа, бой, брак, истекший срок годности товара в торговом зале.
    3. Бой товара в торговом зале или на складе сотрудником магазина.

    Нельзя Продать
    Можно продать
    Сотрудники
    """
    WAREHOUSE = 'WH'
    TRAIDING_FLOOR = "TF"
    STAFF = 'ST'
    SUB_DESCRIPTION = [
        (WAREHOUSE, '1. Пропажа товара на складе / при разгрузке автомобиля.'),
        (TRAIDING_FLOOR, '2. Пропажа, бой, брак, истекший срок годности товара в торговом зале.'),
        (STAFF, '3. Бой товара в торговом зале или на складе сотрудником магазина.')
    ]

    NOT_SALE = 'NS'
    SALE_DISCOUNT = 'SD'
    EMPLOYEES_WILL_BUY = 'EB'
    FUTURE_SPOILED = [
        (NOT_SALE, 'Нельзя Продать'),
        (SALE_DISCOUNT, 'Можно продать'),
        (EMPLOYEES_WILL_BUY, 'Сотрудники')
    ]

    description_comment = models.TextField(max_length=200, default="", null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    quantity = models.PositiveSmallIntegerField(default=0)
    picture = models.BinaryField(null=True, blank=True, editable=True)
    content_type = models.CharField(max_length=256, null=True, blank=True, help_text="The MIMEType of th file")
    name_photo = models.CharField(max_length=256, null=True, blank=True, help_text="Name foto")
    write_off = models.IntegerField(default=0)
    future_spoiled = models.CharField( max_length=2, choices=FUTURE_SPOILED, default=NOT_SALE, verbose_name="Что делать с браком")
    sub_description = models.CharField(max_length=2, choices=SUB_DESCRIPTION, default=WAREHOUSE, verbose_name="Вид обстоятельств")
    employee = models.ForeignKey('Employee', on_delete=models.CASCADE, null=True, db_constraint=False)
    nomenclature = models.ForeignKey('Nomenclature', on_delete=models.CASCADE, null=False, db_constraint=False)
    shop = models.ForeignKey('Shop', on_delete=models.CASCADE, null=False, db_constraint=True)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=0, db_constraint=False)
    comments = GenericRelation(Comment, default="", related_name="comments")


            

