# Generated by Django 4.1.2 on 2022-10-15 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BankingSystem', '0002_alter_accounttype_name_alter_profile_current_balance'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accounttype',
            name='Name',
            field=models.CharField(default='savings', max_length=20, null=True),
        ),
    ]
