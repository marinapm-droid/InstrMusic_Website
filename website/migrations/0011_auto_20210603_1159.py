# Generated by Django 3.2.2 on 2021-06-03 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0010_result_quizz_final_result'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='birthday',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='comment',
            name='question7',
            field=models.CharField(max_length=30),
        ),
    ]
