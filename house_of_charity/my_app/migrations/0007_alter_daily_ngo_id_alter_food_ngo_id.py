# Generated by Django 5.1.4 on 2024-12-21 10:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0006_alter_money_ngo_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='daily',
            name='ngo_id',
            field=models.ForeignKey(db_column='ngo', null=True, on_delete=django.db.models.deletion.CASCADE, to='my_app.ngo_details'),
        ),
        migrations.AlterField(
            model_name='food',
            name='ngo_id',
            field=models.ForeignKey(db_column='ngo', null=True, on_delete=django.db.models.deletion.CASCADE, to='my_app.ngo_details'),
        ),
    ]