# Generated by Django 2.2.2 on 2019-06-18 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0003_auto_20190614_2032'),
    ]

    operations = [
        migrations.AlterField(
            model_name='content',
            name='html',
            field=models.TextField(blank=True),
        ),
    ]
