from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import DataUjiKendaraan
from .meta_form import meta_form__data_uji_kendaraan, status_form_options
from . import utils
from datetime import date, datetime
from . import compute

# Create your views here.
def index(request):
    return render(request, 'app/base.html')

def list_data_uji_kendaraan(request):
    all_data = DataUjiKendaraan.objects.all()
    context = {
        'title': 'daftar data uji kendaraan',
        'items': all_data
    }
    return render(request, 'app/data/list.html', context)

def remove_data(request, id):
    item = DataUjiKendaraan.objects.get(id=id)
    item.delete()
    return redirect('list_data')

def add_data(request):
    if request.POST:
        data = request.POST.dict()
        # extract main data
        main_keys = ['nomor_kendaraan', 'nama_pemilik', 'tanggal_pemeriksaan']
        main_data = { k: data[k] for k in main_keys }

        # Convert date value
        k = 'tanggal_pemeriksaan'
        tgl = main_data[k]
        main_data[k] = datetime.strptime(tgl, '%Y-%m-%d').date()

        # Remove csrf token and main keys
        del data['csrfmiddlewaretoken']
        for k in main_keys:
            del data[k]

        # extract selected components
        components = { k: False for k in data.keys() }

        # merge all data
        main_data.update(components)

        obj = DataUjiKendaraan(**main_data)

        # Handle files
        file_keys = ['bukti_image', 'kendaraan_image']
        files = request.FILES
        new_random_name = utils.random_name()
        bukti_name = utils.file_random_name(files['bukti_image'], new_random_name, '01')
        kendaraan_name = utils.file_random_name(files['kendaraan_image'], new_random_name, '02')

        obj.bukti_image.save(bukti_name, files['bukti_image'])
        obj.kendaraan_image.save(kendaraan_name, files['kendaraan_image'])

        # and save it
        obj.save()

        return redirect('list_data')
    else:
        context = {
            'title': 'tambah data uji kendaraan',
            'forms': meta_form__data_uji_kendaraan
        }
        return render(request, 'app/data/add.html', context)

def edit_data(request, id):
    if request.POST:
        if request.POST['action'] == 'classify':
            item = DataUjiKendaraan.objects.get(id=id)
            data = request.POST.dict()
            exclude_keys = {
                'action',
                'nomor_kendaraan', 
                'nama_pemilik', 
                'tanggal_pemeriksaan', 
                'csrfmiddlewaretoken',
                'kendaraan_image', 
                'bukti_image'}
            components_arr = []
            for group in meta_form__data_uji_kendaraan:
                for comp in group.components:
                    if comp.separator:
                        continue
                    components_arr.append(1 if getattr(item, comp.name) else 0)
            class_result = compute.random_forest(components_arr)
        return HttpResponse('OK')
    else:
        item = DataUjiKendaraan.objects.get(id=id)
        forms = []
        for group in meta_form__data_uji_kendaraan:
            components = []
            group_item = { 
                'name': group.name,
                'title': group.title
            }
            for comp in group.components:
                if comp.separator:
                    components.append({
                        'name': comp.name,
                        'label': comp.label,
                        'separator': True
                    })
                else:
                    components.append({
                        'name': comp.name,
                        'label': comp.label,
                        'value': getattr(item, comp.name)
                    })
            group_item['components'] = components
            forms.append(group_item)
        context = {
            'title': 'edit data uji kendaraan',
            'forms': forms,
            'item': item,
            'status_form_options': status_form_options
        }
        return render(request, 'app/data/edit.html', context)

def classify_data(request, id):
    item = DataUjiKendaraan.objects.get(id=id)
    components_arr = []
    for group in meta_form__data_uji_kendaraan:
        for comp in group.components:
            if comp.separator:
                continue
            components_arr.append(1 if getattr(item, comp.name) else 0)
    class_result = compute.random_forest(components_arr)
    context = {
        'item': item,
        'class_result': class_result
    }
    return render(request, 'app/data/classification-result.html', context)