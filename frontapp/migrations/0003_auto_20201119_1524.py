# Generated by Django 3.1 on 2020-11-19 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontapp', '0002_product_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='SKU',
        ),
        migrations.RemoveField(
            model_name='product',
            name='Shipping',
        ),
        migrations.RemoveField(
            model_name='product',
            name='condition',
        ),
        migrations.RemoveField(
            model_name='product',
            name='delivery',
        ),
        migrations.RemoveField(
            model_name='product',
            name='material',
        ),
        migrations.RemoveField(
            model_name='product',
            name='size',
        ),
        migrations.RemoveField(
            model_name='product',
            name='warranty',
        ),
        migrations.RemoveField(
            model_name='product',
            name='wire',
        ),
        migrations.AddField(
            model_name='product',
            name='url',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=200),
        ),
    ]
