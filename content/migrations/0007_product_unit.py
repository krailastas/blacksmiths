# Generated by Django 2.1 on 2019-03-07 04:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0006_product_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='unit',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]