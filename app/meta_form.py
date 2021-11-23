from collections import namedtuple

class FormField:
    def __init__(self, name, label, separator=False, value=None):
        self.name = name
        self.label = label
        self.separator = separator
        self.value = value
FormGroup = namedtuple('FormGroup', ['name', 'title', 'components'])

meta_form__data_uji_kendaraan = [
    FormGroup('peralatan', 'Peralatan', [
        FormField('no_chasis', 'nomor chasis'),
        FormField('pelat_pabrik_pembuat', 'pelat pabrik pembuat'),
        FormField('pelat_nomor', 'pelat nomor'),
        FormField('tulisan', 'tulisan'),

        FormField('penghapus_kaca_depan_l', 'penghapus kaca depan L'),
        FormField('penghapus_kaca_depan_r', 'penghapus kaca depan R'),

        FormField('klakson', 'klakson'),

        FormField('kaca_spion_l', 'kaca spion L'),
        FormField('kaca_spion_l', 'kaca spion R'),

        FormField('pandangan_kedepan', 'pandangan kedepan'),
        FormField('kaca_penahan_sinar', 'kaca penahan sinar'),
        FormField('alat_pengendalian', 'alat pengendalian'),
        FormField('lampu_indikasi', 'lampu indikasi'),
        FormField('spedometer', 'spedometer'),
        FormField('perlengkapan', 'perlengkapan')
    ]),
    FormGroup('sistem_penerangan', 'sistem penerangan', [
        FormField('lampu_jauh_l', 'lampu jauh L'),
        FormField('lampu_jauh_r', 'lampu jauh R'),

        FormField('tambahan_lampu_jauh_l', 'tambahan lampu jauh L'),
        FormField('tambahan_lampu_jauh_r', 'tambahan lampu jauh R'),

        FormField('lampu_dekat_l', 'lampu dekat L'),
        FormField('lampu_dekat_r', 'lampu dekat R'),

        FormField('arah_lampu_l', 'arah lampu L'),
        FormField('arah_lampu_r', 'arah lampu R'),

        FormField('lampu_kabut_r', 'lampu kabut L'),
        FormField('lampu_kabut_l', 'lampu kabut R'),

        FormField('lampu_posisi_l', 'lampu posisi L'),
        FormField('lampu_posisi_r', 'lampu posisi R'),

        FormField('lampu_posisi_belakang_l', 'lampu posisi belakang L'),
        FormField('lampu_posisi_belakang_r', 'lampu posisi belakang R'),

        FormField('lampu_rem_l', 'lampu rem L'),
        FormField('lampu_rem_r', 'lampu rem R'),

        FormField('lampu_pelat_nomor', 'lampu pelat nomor'),

        FormField('lampu_mundur_l', 'lampu mundur L'),
        FormField('lampu_mundur_r', 'lampu mundur R'),

        FormField('lampu_kabut_belakang_l', 'lampu_kabut_belakang L'),
        FormField('lampu_kabut_belakang_r', 'lampu_kabut_belakang R'),

        FormField('lampu_arah_peringatan_l', 'lampu arah peringatan L'),
        FormField('lampu_arah_peringatan_r', 'lampu arah peringatan R'),

        FormField('reflektor_merah_l', 'reflektor merah L'),
        FormField('reflektor_merah_r', 'reflektor merah R'),

        FormField('lampu_tambahan_lain_l', 'lampu tambahan lain L'),
        FormField('lampu_tambahan_lain_r', 'lampu tambahan lain R')
    ]),

    FormGroup('sistem_kemudi', 'sistem kemudi', [
        FormField('roda_kemudi', 'roda kemudi'),
        FormField('spelling_roda_kemudi', 'spelling_roda kemudi'),
        FormField('balang_kemudi', 'balang kemudi'),
        FormField('roda_gigi_kemudi', 'roda gigi kemudi'),

        FormField('sambungan_kemudi_l', 'sambungan kemudi L'),
        FormField('sambungan_kemudi_r', 'sambungan kemudi R'),

        FormField('penyambung_sendi_peluru_l', 'penyambung sendi peluru L'),
        FormField('penyambung_sendi_peluru_r', 'penyambung sendi peluru R'),

        FormField('power_steering', 'power_steering'),
        FormField('side_slip', 'side slip')
    ]),
    FormGroup('as_suspensi', 'as dan suspensi', [
        FormField('suspensi_roda_depan_l', 'suspensi roda depan L'),
        FormField('suspensi_roda_depan_r', 'suspensi roda depan R'),

        FormField('suspensi_roda_belakang_l', 'suspensi roda belakang L'),
        FormField('suspensi_roda_belakang_r', 'suspensi roda belakang R'),

        FormField('sumbu_l', 'sumbu L'),
        FormField('sumbu_r', 'sumbu R'),

        FormField('pemasangan_sumbu_l', 'pemasangan sumbu L'),
        FormField('pemasangan_sumbu_r', 'pemasangan sumbu R'),

        FormField('pegas_l', 'pegas L'),
        FormField('pegas_r', 'pegas R'),

        FormField('bantalan_roda_l', 'bantalan roda L'),
        FormField('bantalan_roda_r', 'bantalan roda R')
    ]),
    FormGroup('ban_pelek', 'ban dan pelek', [
        FormField('ukuran_dan_jenis_ban', 'ukuran dan jenis ban'),
        FormField('keadaan_ban', 'keadaan ban'),
        FormField('kedalaman_kembang_ban', 'kedalaman kembang ban'),
        FormField('ukuran_dan_jenis_pelek', 'ukuran dan jenis pelek'),
        FormField('keadaan_pelek', 'keadaan pelek'),
        FormField('penguatan_ban_or_pelek', 'penguatan ban/pelek')
    ]),
    FormGroup('rangka_bodi', 'rangka dan bodi', [
        FormField('rangka_penopang', 'rangka penopang'),
        FormField('bemper', 'bemper'),
        FormField('tempat_roda_cadangan', 'tempat roda cadangan'),
        FormField('keamanan_bodi', 'keamanan bodi'),
        FormField('kondisi_bodi', 'kondisi bodi'),
        FormField('ruang_pengemudi', 'ruang pengemudi'),
        FormField('tempat_duduk_berdiri', 'tempat duduk/berdiri'),
        FormField('sambungan_kereta_cadangan', 'sambungan kereta cadangan')
    ]),
    FormGroup('sistem_rem', 'sistem rem', [
        FormField('pedal_rem', 'pedal rem'),
        FormField('speling_pedal', 'spelling pedal'),
        FormField('kebocoran_kelemahan', 'kebocoran kelemahan'),

        FormField('sambungan_tuas_kabel_l', 'sambungan_tuas_kabel L'),
        FormField('sambungan_tuas_kabel_r', 'sambungan_tuas_kabel R'),

        FormField('pipa_selang_l', 'pipa selang L'),
        FormField('pipa_selang_r', 'pipa selang R'),

        FormField('selinder_katup_l', 'selinder katup L'),
        FormField('selinder_katup_r', 'selinder katup R'),

        FormField('teromol_cakram_l', 'teromol cakram L'),
        FormField('teromol_cakram_r', 'teromol cakram R'),

        FormField('perodo_l', 'perodo / pad /pelapis L'),
        FormField('perodo_r', 'perodo / pad /pelapis R'),

        FormField('', 'sistem vacuum', separator=True),
        FormField('sv_fungsi', 'fungsi'),
        FormField('sv_kebocoran', 'kebocoran'),
        FormField('', 'sistem tekanan angin', separator=True),
        FormField('sta_kebocoran', 'kebocoran'),
        FormField('sta_waktu_pengisian', 'waktu pengisian'),

        FormField('sta_penggerak_rem_l', 'penggerak rem L'),
        FormField('sta_penggerak_rem_r', 'penggerak rem R'),

        FormField('sta_pengisian_kereta_gandengan', 'pengisian kereta gandengan'),
        FormField('sta_tekanan_angin', 'tekanan angin'),
        FormField('', 'rem parkir', separator=True),
        FormField('rp_tuas_tangan_pedal', 'tuas tangan pedal'),
        FormField('rp_speling_tuas_tangan_pedal', 'speling tuas tangan pedal'),
        FormField('rp_kebocoran_kelemahan', 'kebocoran, kelemahan'),

        FormField('rp_sambungan_tuas_kabel_l', 'sambungan tuas kabel L'),
        FormField('rp_sambungan_tuas_kabel_r', 'sambungan tuas kabel R'),

        FormField('', 'sistem rem gas buang', separator=True),
        FormField('srgb_fungsi', 'fungsi'),
        FormField('srgb_efisiensi_rem', 'efisiensi rem'),
        FormField('er_rem_utama', 'rem utama'),
        FormField('er_perbedaan_depan', 'perbedaan depan'),
        FormField('er_perbedaan_belakang', 'perbedaan belakang'),
        FormField('er_rem_parkir', 'rem parkir')
    ]),
    FormGroup('mesin_transmisi', 'mesin dan transmisi', [
        FormField('dudukan_mesin', 'dudukan mesin'),
        FormField('kondisi_mesin', 'kondisi mesin'),
        FormField('transmisi', 'transmisi'),
        FormField('sistem_gas_buang', 'sistem gas buang'),
        FormField('emisi_asap', 'emisi asap'),
        FormField('emisi_co', 'emisi co'),
    ]),
    FormGroup('lain', 'lain - lain', [
        FormField('sistem_bahan_bakar', 'sistem bahan bakar'),
        FormField('sistem_kelistrikan', 'sistem kelistrikan')
    ])
]

meta_form__component_keys = []
for group in meta_form__data_uji_kendaraan:
    for field in group.components:
        if field.separator:
            continue
        meta_form__component_keys.append(field.name)

status_form_options = [
    { 'value': 'DR', 'label': 'draft' },
    { 'value': 'LU', 'label': 'lulus' },
    { 'value': 'TL', 'label': 'tidak lulus' }
]
