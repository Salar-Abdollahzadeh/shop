# Generated by Django 3.2.7 on 2021-10-09 09:15

from django.db import migrations, models
import utils


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_alter_productgallery_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(upload_to=utils.upload_image_path),
        ),
    ]
