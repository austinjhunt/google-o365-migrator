# Generated by Django 4.1.3 on 2022-11-19 23:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='administrationsettings',
            name='google_service_account_auth_client_email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='administrationsettings',
            name='google_service_account_auth_client_id',
            field=models.CharField(blank=True, max_length=32, null=True),
        ),
        migrations.AddField(
            model_name='administrationsettings',
            name='google_service_account_auth_private_key',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='administrationsettings',
            name='google_service_account_auth_private_key_id',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
        migrations.AddField(
            model_name='administrationsettings',
            name='google_service_account_auth_project_id',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
        migrations.AddField(
            model_name='administrationsettings',
            name='smtp_password',
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
        migrations.AddField(
            model_name='administrationsettings',
            name='smtp_port',
            field=models.IntegerField(blank=True, default=587, null=True),
        ),
        migrations.AddField(
            model_name='administrationsettings',
            name='smtp_send_email_notifications',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='administrationsettings',
            name='smtp_server',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
        migrations.AddField(
            model_name='administrationsettings',
            name='smtp_subject',
            field=models.TextField(blank=True, default='Google Drive to SharePoint Migration Complete', null=True),
        ),
        migrations.AddField(
            model_name='administrationsettings',
            name='smtp_username',
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
        migrations.AlterField(
            model_name='administrationsettings',
            name='google_oauth_auth_client_secret',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='administrationsettings',
            name='google_oauth_auth_provider_x509_cert_url',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='administrationsettings',
            name='google_oauth_auth_uri',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='administrationsettings',
            name='google_oauth_client_id',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='administrationsettings',
            name='google_oauth_token_uri',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='administrationsettings_listattributeitem',
            name='list_type',
            field=models.CharField(choices=[('GOARU', 'Google OAuth Redirect URI'), ('GOAJO', 'Google OAuth JS Origin'), ('GSVCAURI', 'Google Service Account Auth URI'), ('GSVCTURI', 'Google Service Account Token URI'), ('GSVCAPX509URI', 'Google Service Account Auth Provider X509 Cert URL'), ('GSVCCLIX509URI', 'Google Service Account Client X509 Cert URL')], default='GOARU', max_length=32),
        ),
    ]