# Generated by Django 4.0.3 on 2022-03-27 05:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0005_category_item_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
