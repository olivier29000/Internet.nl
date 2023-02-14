# Generated by Django 3.2.3 on 2021-10-05 10:42

import enumfields.fields
from django.db import migrations, models

import checks.models


class Migration(migrations.Migration):
    dependencies = [
        ("checks", "0007_null_mx"),
    ]

    operations = [
        migrations.AddField(
            model_name="domaintesttls",
            name="protocols_good",
            field=checks.models.ListField(null=True),
        ),
        migrations.AlterField(
            model_name="connectiontest",
            name="aaaa_ipv6",
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AlterField(
            model_name="connectiontest",
            name="addr_ipv6",
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AlterField(
            model_name="connectiontest",
            name="dnssec_val",
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AlterField(
            model_name="connectiontest",
            name="finished",
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AlterField(
            model_name="connectiontest",
            name="resolv_ipv6",
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AlterField(
            model_name="connectiontest",
            name="slaac_without_privext",
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AlterField(
            model_name="domaintestappsecpriv",
            name="content_security_policy_enabled",
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AlterField(
            model_name="domaintestappsecpriv",
            name="referrer_policy_enabled",
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AlterField(
            model_name="domaintestappsecpriv",
            name="server_reachable",
            field=models.BooleanField(default=True, null=True),
        ),
        migrations.AlterField(
            model_name="domaintestappsecpriv",
            name="x_content_type_options_enabled",
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AlterField(
            model_name="domaintestappsecpriv",
            name="x_frame_options_enabled",
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AlterField(
            model_name="domaintestappsecpriv",
            name="x_xss_protection_enabled",
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AlterField(
            model_name="domaintesttls",
            name="client_reneg",
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AlterField(
            model_name="domaintesttls",
            name="compression",
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AlterField(
            model_name="domaintesttls",
            name="could_not_test_smtp_starttls",
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AlterField(
            model_name="domaintesttls",
            name="dane_rollover",
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AlterField(
            model_name="domaintesttls",
            name="hsts_enabled",
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AlterField(
            model_name="domaintesttls",
            name="http_compression_enabled",
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AlterField(
            model_name="domaintesttls",
            name="secure_reneg",
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AlterField(
            model_name="domaintesttls",
            name="server_reachable",
            field=models.BooleanField(default=True, null=True),
        ),
        migrations.AlterField(
            model_name="domaintesttls",
            name="tls_enabled",
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AlterField(
            model_name="mailtestauth",
            name="dkim_available",
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AlterField(
            model_name="mailtestauth",
            name="dmarc_available",
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AlterField(
            model_name="mailtestauth",
            name="spf_available",
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AlterField(
            model_name="mailtestdnssec",
            name="mx_status",
            field=enumfields.fields.EnumIntegerField(default=False, enum=checks.models.MxStatus, null=True),
        ),
        migrations.AlterField(
            model_name="mailtestipv6",
            name="mx_status",
            field=enumfields.fields.EnumIntegerField(default=False, enum=checks.models.MxStatus, null=True),
        ),
        migrations.AlterField(
            model_name="mailtesttls",
            name="mx_status",
            field=enumfields.fields.EnumIntegerField(default=False, enum=checks.models.MxStatus, null=True),
        ),
    ]
