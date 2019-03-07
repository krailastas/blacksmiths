from django.db import models


class MainPages(models.Model):
    line_1 = models.CharField(max_length=255, blank=True, default='Кованые ворота<br/>в Киеве и области')
    line_2 = models.CharField(max_length=255, blank=True,
                              default='г. Винница, ул. Максима Шимка 12а<br/>Работаем без выходных')
    phone = models.CharField(max_length=128, blank=True, default='+3 (097) 000-94-64')
    line_3 = models.CharField(
        max_length=255, blank=True, default='КОВАНЫЕ ИЗДЕЛИЯ<br/>РУЧНОЙ РАБОТЫ<br/>С ГАРАНТИЕЙ 30 ЛЕТ')
    line_4 = models.CharField(
        max_length=255, blank=True, default='Начинаем работы через 2 дня<br/>после подписания договора')
    line_5 = models.CharField(
        max_length=255, blank=True, default='Собственное производство Полностью <br/> ручная робота')
    title = models.CharField(max_length=255, blank=True, default='BlackSmiths - кованные изделия в Украине')
    keywords = models.CharField(max_length=255, blank=True, default='BlackSmiths - кованные изделия в Украине')
    description = models.TextField(max_length=500, blank=True, default='BlackSmiths - кованные изделия в Украине')
    ceo_name = models.CharField(max_length=255, default='Александр Трофимчук', blank=True)
    ceo_title = models.CharField(
        max_length=255, blank=True, default='Технический директор компании <br/>"BlackSmiths Place"'
    )
    ceo_image = models.ImageField(upload_to='main/images', blank=True)


class Category(models.Model):
    title = models.CharField(max_length=255)
    order_title = models.CharField(max_length=255)
    menu_name = models.CharField(max_length=255)
    name_inside_catalog = models.CharField(max_length=255)
    image = models.ImageField(upload_to='category/images')
    keywords = models.CharField(max_length=255, blank=True, default='BlackSmiths - кованные изделия в Украине')
    description = models.TextField(max_length=500, blank=True, default='BlackSmiths - кованные изделия в Украине')
    is_active = models.BooleanField(default=True)
    order = models.IntegerField(default=1)

    def __str__(self):
        return self.title


class Product(models.Model):
    title = models.CharField(max_length=255)
    category = models.ForeignKey('content.Category', related_name='category_products', on_delete=models.CASCADE)
    order_title = models.CharField(max_length=255)
    price = models.CharField(max_length=255)
    unit = models.CharField(max_length=255)
    image = models.ImageField(upload_to='product/images')
    keywords = models.CharField(max_length=255, blank=True, default='BlackSmiths - кованные изделия в Украине')
    description = models.TextField(max_length=500, blank=True, default='BlackSmiths - кованные изделия в Украине')
    short_description = models.TextField(max_length=500, blank=True)
    is_active = models.BooleanField(default=True)
    order = models.IntegerField(default=1)

    def __str__(self):
        return self.title


class Images(models.Model):
    image = models.ImageField(upload_to='product/images')
    product = models.ForeignKey('content.Product', related_name='product_images', on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
    order = models.IntegerField(default=1)


class Personal(models.Model):
    fn = models.CharField(max_length=128, blank=True)
    ln = models.CharField(max_length=128, blank=True)
    title = models.CharField(max_length=128, blank=True)
    image = models.ImageField(upload_to='personal/images')
    is_active = models.BooleanField(default=True)
    order = models.IntegerField(default=1)

    def __str__(self):
        return '{} {}'.format(self.fn, self.ln)


class Galery(models.Model):
    image = models.ImageField(upload_to='galery/images')
    is_active = models.BooleanField(default=True)
    order = models.IntegerField(default=1)


class StatusChoices:
    PEDDING = 1
    DONE = 2
    CANCEL = 3

    CHOICES = (
        (PEDDING, 'PEDDING'),
        (DONE, 'DONE'),
        (CANCEL, 'CANCEL'),
    )


class Book(models.Model):
    name = models.CharField(max_length=255, blank=True)
    phone = models.CharField(max_length=255)
    comment = models.TextField(max_length=700, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(
        default=StatusChoices.PEDDING, choices=StatusChoices.CHOICES,
        blank=True, null=True
    )

    def __str__(self):
        return self.name
