# Generated by Django 4.1.3 on 2022-11-26 20:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0008_alter_administrationsettings_require_idp_login_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='administrationsettings',
            name='onedrive_email_notification_template',
            field=models.TextField(blank=True, default='', null=True, verbose_name='Email Body Template for Google to OneDrive Migration Email Notification'),
        ),
        migrations.AddField(
            model_name='administrationsettings',
            name='onedrive_sms_notification_template',
            field=models.TextField(blank=True, default='', null=True, verbose_name='SMS Message Template for Google to OneDrive Migration SMS Notification'),
        ),
        migrations.AddField(
            model_name='administrationsettings',
            name='sharepoint_email_notification_template',
            field=models.TextField(blank=True, default='', null=True, verbose_name='Email Body Template for Google to SharePoint Migration Email Notification'),
        ),
        migrations.AddField(
            model_name='administrationsettings',
            name='sharepoint_sms_notification_template',
            field=models.TextField(blank=True, default='', null=True, verbose_name='SMS Message Template for Google to SharePoint Migration SMS Notification'),
        ),
    ]