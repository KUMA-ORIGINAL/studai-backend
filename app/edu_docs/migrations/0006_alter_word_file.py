# Generated by Django 5.0 on 2024-07-09 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('edu_docs', '0005_alter_word_discipline_alter_word_wishes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='word',
            name='file',
            field=models.FileField(upload_to='documents/%Y/%m/%d/'),
        ),
    ]
