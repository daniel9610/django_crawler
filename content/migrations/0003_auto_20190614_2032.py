# Generated by Django 2.2.2 on 2019-06-14 20:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0002_content_secondary_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='content',
            name='secondary_url',
            field=models.TextField(blank=True, max_length=300),
        ),
    ]
