# Generated by Django 3.2.9 on 2021-11-19 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='dataujikendaraan',
            name='alat_pengendalian',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='dataujikendaraan',
            name='kaca_penahan_sinar',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='dataujikendaraan',
            name='kaca_spion',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='dataujikendaraan',
            name='klakson',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='dataujikendaraan',
            name='lampu_indikasi',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='dataujikendaraan',
            name='pandangan_kedepan',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='dataujikendaraan',
            name='pelat_nomor',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='dataujikendaraan',
            name='penghapus_kaca_depan',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='dataujikendaraan',
            name='perlengkapan',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='dataujikendaraan',
            name='spedometer',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='dataujikendaraan',
            name='tulisan',
            field=models.BooleanField(default=True),
        ),
    ]
