# Generated by Django 3.2.9 on 2021-11-23 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0017_dataujikendaraan_srgb_efisiensi_rem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dataujikendaraan',
            name='kendaraan_image',
            field=models.ImageField(default='truck_default.jpg', null=True, upload_to='static/uploads/'),
        ),
    ]
