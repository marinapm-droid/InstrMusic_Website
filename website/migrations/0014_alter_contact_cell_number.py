# Generated by Django 3.2.2 on 2021-06-03 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0013_contact_birthday'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='cell_number',
            field=models.IntegerField(),
        ),
    ]
