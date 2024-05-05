# Generated by Django 5.0.2 on 2024-05-02 19:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='linkPrecedence',
            field=models.CharField(choices=[('primary', 'primary'), ('secondary', 'secondary')], default='primary', max_length=10),
        ),
        migrations.AlterField(
            model_name='contact',
            name='linkedId',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.contact'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='phoneNumber',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]