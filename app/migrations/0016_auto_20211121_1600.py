# Generated by Django 3.2.9 on 2021-11-21 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0015_auto_20211121_1556'),
    ]

    operations = [
        migrations.RenameField(
            model_name='dataujikendaraan',
            old_name='arah_lampu',
            new_name='arah_lampu_l',
        ),
        migrations.RenameField(
            model_name='dataujikendaraan',
            old_name='bantalan_roda',
            new_name='arah_lampu_r',
        ),
        migrations.RenameField(
            model_name='dataujikendaraan',
            old_name='kaca_spion',
            new_name='bantalan_roda_l',
        ),
        migrations.RenameField(
            model_name='dataujikendaraan',
            old_name='lampu_arah_peringatan',
            new_name='bantalan_roda_r',
        ),
        migrations.RenameField(
            model_name='dataujikendaraan',
            old_name='lampu_dekat',
            new_name='kaca_spion_l',
        ),
        migrations.RenameField(
            model_name='dataujikendaraan',
            old_name='lampu_jauh',
            new_name='kaca_spion_r',
        ),
        migrations.RenameField(
            model_name='dataujikendaraan',
            old_name='lampu_kabut',
            new_name='lampu_arah_peringatan_l',
        ),
        migrations.RenameField(
            model_name='dataujikendaraan',
            old_name='lampu_kabut_belakang',
            new_name='lampu_arah_peringatan_r',
        ),
        migrations.RenameField(
            model_name='dataujikendaraan',
            old_name='lampu_mundur',
            new_name='lampu_dekat_l',
        ),
        migrations.RenameField(
            model_name='dataujikendaraan',
            old_name='lampu_posisi',
            new_name='lampu_dekat_r',
        ),
        migrations.RenameField(
            model_name='dataujikendaraan',
            old_name='lampu_posisi_belakang',
            new_name='lampu_jauh_l',
        ),
        migrations.RenameField(
            model_name='dataujikendaraan',
            old_name='lampu_rem',
            new_name='lampu_jauh_r',
        ),
        migrations.RenameField(
            model_name='dataujikendaraan',
            old_name='lampu_tambahan_lain',
            new_name='lampu_kabut_belakang_l',
        ),
        migrations.RenameField(
            model_name='dataujikendaraan',
            old_name='pegas',
            new_name='lampu_kabut_belakang_r',
        ),
        migrations.RenameField(
            model_name='dataujikendaraan',
            old_name='pemasangan_sumbu',
            new_name='lampu_kabut_l',
        ),
        migrations.RenameField(
            model_name='dataujikendaraan',
            old_name='penghapus_kaca_depan',
            new_name='lampu_kabut_r',
        ),
        migrations.RenameField(
            model_name='dataujikendaraan',
            old_name='penyambung_sendi_peluru',
            new_name='lampu_mundur_l',
        ),
        migrations.RenameField(
            model_name='dataujikendaraan',
            old_name='perodo',
            new_name='lampu_mundur_r',
        ),
        migrations.RenameField(
            model_name='dataujikendaraan',
            old_name='pipa_selang',
            new_name='lampu_posisi_belakang_l',
        ),
        migrations.RenameField(
            model_name='dataujikendaraan',
            old_name='reflektor_merah',
            new_name='lampu_posisi_belakang_r',
        ),
        migrations.RenameField(
            model_name='dataujikendaraan',
            old_name='rp_sambungan_tuas_kabel',
            new_name='lampu_posisi_l',
        ),
        migrations.RenameField(
            model_name='dataujikendaraan',
            old_name='sambungan_kemudi',
            new_name='lampu_posisi_r',
        ),
        migrations.RenameField(
            model_name='dataujikendaraan',
            old_name='sambungan_tuas_kabel',
            new_name='lampu_rem_l',
        ),
        migrations.RenameField(
            model_name='dataujikendaraan',
            old_name='selinder_katup',
            new_name='lampu_rem_r',
        ),
        migrations.RenameField(
            model_name='dataujikendaraan',
            old_name='sta_penggerak_rem',
            new_name='lampu_tambahan_lain_l',
        ),
        migrations.RenameField(
            model_name='dataujikendaraan',
            old_name='sumbu',
            new_name='lampu_tambahan_lain_r',
        ),
        migrations.RenameField(
            model_name='dataujikendaraan',
            old_name='suspensi_roda_belakang',
            new_name='pegas_l',
        ),
        migrations.RenameField(
            model_name='dataujikendaraan',
            old_name='suspensi_roda_depan',
            new_name='pegas_r',
        ),
        migrations.RenameField(
            model_name='dataujikendaraan',
            old_name='tambahan_lampu_jauh',
            new_name='pemasangan_sumbu_l',
        ),
        migrations.RenameField(
            model_name='dataujikendaraan',
            old_name='teromol_cakram',
            new_name='pemasangan_sumbu_r',
        ),
        migrations.AddField(
            model_name='dataujikendaraan',
            name='penghapus_kaca_depan_l',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='dataujikendaraan',
            name='penghapus_kaca_depan_r',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='dataujikendaraan',
            name='penyambung_sendi_peluru_l',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='dataujikendaraan',
            name='penyambung_sendi_peluru_r',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='dataujikendaraan',
            name='perodo_l',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='dataujikendaraan',
            name='perodo_r',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='dataujikendaraan',
            name='pipa_selang_l',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='dataujikendaraan',
            name='pipa_selang_r',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='dataujikendaraan',
            name='reflektor_merah_l',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='dataujikendaraan',
            name='reflektor_merah_r',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='dataujikendaraan',
            name='rp_sambungan_tuas_kabel_l',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='dataujikendaraan',
            name='rp_sambungan_tuas_kabel_r',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='dataujikendaraan',
            name='sambungan_kemudi_l',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='dataujikendaraan',
            name='sambungan_kemudi_r',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='dataujikendaraan',
            name='sambungan_tuas_kabel_l',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='dataujikendaraan',
            name='sambungan_tuas_kabel_r',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='dataujikendaraan',
            name='selinder_katup_l',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='dataujikendaraan',
            name='selinder_katup_r',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='dataujikendaraan',
            name='sta_penggerak_rem_l',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='dataujikendaraan',
            name='sta_penggerak_rem_r',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='dataujikendaraan',
            name='sumbu_l',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='dataujikendaraan',
            name='sumbu_r',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='dataujikendaraan',
            name='suspensi_roda_belakang_l',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='dataujikendaraan',
            name='suspensi_roda_belakang_r',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='dataujikendaraan',
            name='suspensi_roda_depan_l',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='dataujikendaraan',
            name='suspensi_roda_depan_r',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='dataujikendaraan',
            name='tambahan_lampu_jauh_l',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='dataujikendaraan',
            name='tambahan_lampu_jauh_r',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='dataujikendaraan',
            name='teromol_cakram_l',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='dataujikendaraan',
            name='teromol_cakram_r',
            field=models.BooleanField(default=True),
        ),
    ]
