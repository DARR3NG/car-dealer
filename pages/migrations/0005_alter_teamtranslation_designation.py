# Generated by Django 4.2.4 on 2023-09-27 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0004_remove_team_designation_remove_team_first_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teamtranslation',
            name='designation',
            field=models.CharField(max_length=255, verbose_name='designation'),
        ),
    ]
