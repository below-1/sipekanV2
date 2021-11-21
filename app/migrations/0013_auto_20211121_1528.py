# Generated by Django 3.2.9 on 2021-11-21 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_auto_20211121_1232'),
    ]

    operations = [
        migrations.RenameField(
            model_name='dataujikendaraan',
            old_name='srgb_perbedaan_belakang',
            new_name='er_perbedaan_belakang',
        ),
        migrations.RenameField(
            model_name='dataujikendaraan',
            old_name='srgb_perbedaan_depan',
            new_name='er_perbedaan_depan',
        ),
        migrations.RenameField(
            model_name='dataujikendaraan',
            old_name='srgb_rem_parkir',
            new_name='er_rem_parkir',
        ),
        migrations.RenameField(
            model_name='dataujikendaraan',
            old_name='srgb_rem_utama',
            new_name='er_rem_utama',
        ),
        migrations.RemoveField(
            model_name='dataujikendaraan',
            name='pengembung_sendi_peluru',
        ),
        migrations.RemoveField(
            model_name='dataujikendaraan',
            name='penguasaan_ban_or_pelek',
        ),
        migrations.RemoveField(
            model_name='dataujikendaraan',
            name='srgb_efisiensi_rem',
        ),
        migrations.RemoveField(
            model_name='dataujikendaraan',
            name='sta_sta',
        ),
        migrations.AddField(
            model_name='dataujikendaraan',
            name='bemper',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='dataujikendaraan',
            name='keamanan_bodi',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='dataujikendaraan',
            name='kondisi_bodi',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='dataujikendaraan',
            name='penguatan_ban_or_pelek',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='dataujikendaraan',
            name='penyambung_sendi_peluru',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='dataujikendaraan',
            name='perodo',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='dataujikendaraan',
            name='rangka_penopang',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='dataujikendaraan',
            name='ruang_pengemudi',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='dataujikendaraan',
            name='sambungan_kereta_cadangan',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='dataujikendaraan',
            name='tempat_duduk_berdiri',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='dataujikendaraan',
            name='tempat_roda_cadangan',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='dataujikendaraan',
            name='ukuran_dan_jenis_pelek',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='dataujikendaraan',
            name='bukti_image',
            field=models.ImageField(null=True, upload_to='static/uploads/'),
        ),
        migrations.AlterField(
            model_name='dataujikendaraan',
            name='kendaraan_image',
            field=models.ImageField(null=True, upload_to='static/uploads/'),
        ),
    ]