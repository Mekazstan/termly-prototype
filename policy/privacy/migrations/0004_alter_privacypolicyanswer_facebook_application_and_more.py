# Generated by Django 4.2.6 on 2023-10-31 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('privacy', '0003_alter_derivdata_option_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='privacypolicyanswer',
            name='facebook_application',
            field=models.BooleanField(default=False, verbose_name='Facebook application'),
        ),
        migrations.AlterField(
            model_name='privacypolicyanswer',
            name='mobile_application',
            field=models.BooleanField(default=False, verbose_name='Mobile application'),
        ),
        migrations.AlterField(
            model_name='privacypolicyanswer',
            name='website',
            field=models.BooleanField(default=False, verbose_name='Website'),
        ),
    ]
