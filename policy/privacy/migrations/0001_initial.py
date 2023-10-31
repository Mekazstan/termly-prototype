# Generated by Django 4.2.6 on 2023-10-30 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DerivData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('option', models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No')], max_length=3)),
            ],
        ),
        migrations.CreateModel(
            name='EnglishSpellingOption',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='InfoApp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_will_request_geolocation', models.BooleanField(blank=True, verbose_name="Will you be requesting access to your users' geolocations?")),
                ('user_will_request_features', models.BooleanField(blank=True, verbose_name="Will you be requesting access to features on your users' mobile devices?")),
                ('user_will_collect_device_info', models.BooleanField(blank=True, verbose_name="Will you be collecting any information regarding your users' mobile devices?")),
                ('user_will_send_push_notifications', models.BooleanField(blank=True, verbose_name='Will you be sending push notifications to your users?')),
                ('has_offer_wall', models.BooleanField(blank=True, verbose_name="Does your mobile app have an 'offer wall'?")),
            ],
        ),
        migrations.CreateModel(
            name='PersonalInfoOption',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='PrivacyPolicyAnswer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('website', models.BooleanField(blank=True, verbose_name='Website')),
                ('mobile_application', models.BooleanField(blank=True, verbose_name='Mobile application')),
                ('facebook_application', models.BooleanField(blank=True, verbose_name='Facebook application')),
            ],
        ),
        migrations.CreateModel(
            name='RegistrationOption',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('option', models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No')], max_length=3)),
            ],
        ),
        migrations.CreateModel(
            name='SensitiveInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('option', models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No')], max_length=3)),
            ],
        ),
        migrations.CreateModel(
            name='SocialReg',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('option', models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No')], max_length=3)),
            ],
        ),
        migrations.CreateModel(
            name='UrlAnswer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('website', models.URLField(blank=True, verbose_name='Website URL')),
                ('mobile_application', models.URLField(blank=True, verbose_name='Mobile Application URL')),
                ('facebook_application', models.URLField(blank=True, verbose_name='Facebook Application URL')),
            ],
        ),
        migrations.CreateModel(
            name='UserAge',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('target_users_under_18', models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No')], max_length=3)),
            ],
        ),
        migrations.CreateModel(
            name='UserLocation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('US_users', models.BooleanField(blank=True, verbose_name='Do you have users in the United States?')),
                ('EU_users', models.BooleanField(blank=True, verbose_name='Do you have users in the EU, UK, Switzerland, Iceland, Liechtenstein, or Norway?')),
                ('Canada_users', models.BooleanField(blank=True, verbose_name='Do you have users in Canada?')),
            ],
        ),
        migrations.CreateModel(
            name='SelectedInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('selected_options', models.ManyToManyField(blank=True, to='privacy.personalinfooption')),
            ],
        ),
    ]