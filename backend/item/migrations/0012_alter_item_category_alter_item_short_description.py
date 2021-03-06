# Generated by Django 4.0.3 on 2022-05-26 12:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0011_alter_item_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='item.category'),
        ),
        migrations.AlterField(
            model_name='item',
            name='short_description',
            field=models.TextField(default='Description', max_length=140, null=True),
        ),
    ]
