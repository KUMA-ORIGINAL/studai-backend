# Generated by Django 5.0 on 2024-07-10 21:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0003_alter_payment_word'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='price',
            field=models.PositiveIntegerField(default=1),
            preserve_default=False,
        ),
    ]
