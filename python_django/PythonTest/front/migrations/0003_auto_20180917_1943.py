# Generated by Django 2.1.1 on 2018-09-17 11:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('front', '0002_auto_20180917_1940'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookorder',
            name='book',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='front.Book'),
        ),
    ]
