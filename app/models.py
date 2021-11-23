from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from django.db import models

class StatusPengujian(models.TextChoices):
    DRAFT = 'DR', _('Draft')
    LULUS = 'LU', _('Lulus')
    TIDAK_LULUS = 'TL', _('Tidak Lulus')

# Create your models here.
class DataUjiKendaraan(models.Model):
    nomor_kendaraan = models.CharField(max_length=200)
    nama_pemilik = models.CharField(max_length=200)
    status = models.CharField(
        max_length=2,
        choices=StatusPengujian.choices,
        default=StatusPengujian.DRAFT
    )
    tanggal_pemeriksaan = models.DateField(default=timezone.now)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    bukti_image = models.ImageField(upload_to='static/uploads/', null=True)
    kendaraan_image = models.ImageField(upload_to='static/uploads/', null=True, default='truck_default.jpg')
    user_token = models.CharField(max_length=200, null=True, unique=True)

    # Peralatan
    no_chasis = models.BooleanField(default=True)
    pelat_pabrik_pembuat = models.BooleanField(default=True)
    pelat_nomor = models.BooleanField(default=True)
    tulisan = models.BooleanField(default=True)

    penghapus_kaca_depan_l = models.BooleanField(default=True)
    penghapus_kaca_depan_r = models.BooleanField(default=True)

    klakson = models.BooleanField(default=True)

    kaca_spion_l = models.BooleanField(default=True)
    kaca_spion_r = models.BooleanField(default=True)

    pandangan_kedepan = models.BooleanField(default=True)
    kaca_penahan_sinar = models.BooleanField(default=True)
    alat_pengendalian = models.BooleanField(default=True)
    lampu_indikasi = models.BooleanField(default=True)
    spedometer = models.BooleanField(default=True)
    perlengkapan = models.BooleanField(default=True)

    # Sistem Penerangan
    lampu_jauh_l = models.BooleanField(default=True)
    lampu_jauh_r = models.BooleanField(default=True)

    tambahan_lampu_jauh_l = models.BooleanField(default=True)
    tambahan_lampu_jauh_r = models.BooleanField(default=True)

    lampu_dekat_l = models.BooleanField(default=True)
    lampu_dekat_r = models.BooleanField(default=True)

    arah_lampu_l = models.BooleanField(default=True)
    arah_lampu_r = models.BooleanField(default=True)

    lampu_kabut_l = models.BooleanField(default=True)
    lampu_kabut_r = models.BooleanField(default=True)

    lampu_posisi_l = models.BooleanField(default=True)
    lampu_posisi_r = models.BooleanField(default=True)

    lampu_posisi_belakang_l = models.BooleanField(default=True)
    lampu_posisi_belakang_r = models.BooleanField(default=True)

    lampu_rem_l = models.BooleanField(default=True)
    lampu_rem_r = models.BooleanField(default=True)

    lampu_pelat_nomor = models.BooleanField(default=True)

    lampu_mundur_l = models.BooleanField(default=True)
    lampu_mundur_r = models.BooleanField(default=True)

    lampu_kabut_belakang_l = models.BooleanField(default=True)
    lampu_kabut_belakang_r = models.BooleanField(default=True)

    lampu_arah_peringatan_l = models.BooleanField(default=True)
    lampu_arah_peringatan_r = models.BooleanField(default=True)

    reflektor_merah_l = models.BooleanField(default=True)
    reflektor_merah_r = models.BooleanField(default=True)

    lampu_tambahan_lain_l = models.BooleanField(default=True)
    lampu_tambahan_lain_r = models.BooleanField(default=True)

    # Sistem Kemudi
    roda_kemudi = models.BooleanField(default=True)
    spelling_roda_kemudi = models.BooleanField(default=True)
    balang_kemudi = models.BooleanField(default=True)
    roda_gigi_kemudi = models.BooleanField(default=True)

    sambungan_kemudi_l = models.BooleanField(default=True)
    sambungan_kemudi_r = models.BooleanField(default=True)

    penyambung_sendi_peluru_l = models.BooleanField(default=True)
    penyambung_sendi_peluru_r = models.BooleanField(default=True)

    power_steering = models.BooleanField(default=True)
    side_slip = models.BooleanField(default=True)

    # As dan Suspensi
    suspensi_roda_depan_l = models.BooleanField(default=True)
    suspensi_roda_depan_r = models.BooleanField(default=True)

    suspensi_roda_belakang_l = models.BooleanField(default=True)
    suspensi_roda_belakang_r = models.BooleanField(default=True)

    sumbu_l = models.BooleanField(default=True)
    sumbu_r = models.BooleanField(default=True)

    pemasangan_sumbu_l = models.BooleanField(default=True)
    pemasangan_sumbu_r = models.BooleanField(default=True)

    pegas_l = models.BooleanField(default=True)
    pegas_r = models.BooleanField(default=True)

    bantalan_roda_l = models.BooleanField(default=True)
    bantalan_roda_r = models.BooleanField(default=True)

    # Ban dan Pelek
    ukuran_dan_jenis_ban = models.BooleanField(default=True)
    keadaan_ban = models.BooleanField(default=True)
    kedalaman_kembang_ban = models.BooleanField(default=True)
    ukuran_dan_jenis_pelek = models.BooleanField(default=True)
    keadaan_pelek = models.BooleanField(default=True)
    penguatan_ban_or_pelek = models.BooleanField(default=True)

    # Rangka dan Bodi
    rangka_penopang = models.BooleanField(default=True)
    bemper = models.BooleanField(default=True)
    tempat_roda_cadangan = models.BooleanField(default=True)
    keamanan_bodi = models.BooleanField(default=True)
    kondisi_bodi = models.BooleanField(default=True)
    ruang_pengemudi = models.BooleanField(default=True)
    tempat_duduk_berdiri = models.BooleanField(default=True)
    sambungan_kereta_cadangan = models.BooleanField(default=True)

    # Sistem Rem
    pedal_rem = models.BooleanField(default=True)
    speling_pedal = models.BooleanField(default=True)
    kebocoran_kelemahan = models.BooleanField(default=True)

    sambungan_tuas_kabel_l = models.BooleanField(default=True)
    sambungan_tuas_kabel_r = models.BooleanField(default=True)

    pipa_selang_l = models.BooleanField(default=True)
    pipa_selang_r = models.BooleanField(default=True)

    selinder_katup_l = models.BooleanField(default=True)
    selinder_katup_r = models.BooleanField(default=True)

    teromol_cakram_l = models.BooleanField(default=True)
    teromol_cakram_r = models.BooleanField(default=True)

    perodo_l = models.BooleanField(default=True)
    perodo_r = models.BooleanField(default=True)

    sv_fungsi = models.BooleanField(default=True)
    sv_kebocoran = models.BooleanField(default=True)
    sta_kebocoran = models.BooleanField(default=True)
    sta_waktu_pengisian = models.BooleanField(default=True)

    sta_penggerak_rem_l = models.BooleanField(default=True)
    sta_penggerak_rem_r = models.BooleanField(default=True)

    sta_pengisian_kereta_gandengan = models.BooleanField(default=True)
    sta_tekanan_angin = models.BooleanField(default=True)
    rp_tuas_tangan_pedal = models.BooleanField(default=True)
    rp_speling_tuas_tangan_pedal = models.BooleanField(default=True)
    rp_kebocoran_kelemahan = models.BooleanField(default=True)

    rp_sambungan_tuas_kabel_l = models.BooleanField(default=True)
    rp_sambungan_tuas_kabel_r = models.BooleanField(default=True)

    srgb_fungsi = models.BooleanField(default=True)
    srgb_efisiensi_rem = models.BooleanField(default=True)
    er_rem_utama = models.BooleanField(default=True)
    er_perbedaan_depan = models.BooleanField(default=True)
    er_perbedaan_belakang = models.BooleanField(default=True)
    er_rem_parkir = models.BooleanField(default=True)

    # Mesin dan Transmisi
    dudukan_mesin = models.BooleanField(default=True)
    kondisi_mesin = models.BooleanField(default=True)
    transmisi = models.BooleanField(default=True)
    sistem_gas_buang = models.BooleanField(default=True)
    emisi_asap = models.BooleanField(default=True)
    emisi_co = models.BooleanField(default=True)

    # Lain - lain
    sistem_bahan_bakar = models.BooleanField(default=True)
    sistem_kelistrikan = models.BooleanField(default=True)