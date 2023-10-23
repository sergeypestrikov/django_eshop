from django.db import models


# Модель категории товара
class ProductCategory(models.Model):
    name = models.CharField(verbose_name='наименование', max_length=64, unique=True)
    description = models.TextField(verbose_name='описание', blank=True)

    def __str__(self):
        return f'{self.id} - {self.name}'


# Модель товара
class Product(models.Model):
    GENDER = [('MALE', 'Муж'), ('FEMALE', 'Жен'), ('UNISEX', 'Унисекс')]

    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    name = models.CharField(verbose_name='наименование товара', max_length=128)
    brand = models.CharField(verbose_name='бренд', max_length=64, default='без бренда')
    description = models.TextField(verbose_name='описание товара', blank=True)
    gender = models.CharField(verbose_name='пол', max_length=32, choices=GENDER, default='MALE')
    image = models.ImageField(upload_to='product_images', blank=True)
    price = models.DecimalField(verbose_name='стоимость', max_digits=8, decimal_places=2, default=0)
    quantity = models.PositiveIntegerField(verbose_name='количество', default=0)

    def __str__(self):
        return f'{self.name} {self.category}'