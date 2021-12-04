from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.db.models import Count, Q
from django.shortcuts import render, redirect
# import requests
from .models import (
    DataUjiKendaraan, 
    StatusPengujian
)
from .meta_form import (
    meta_form__data_uji_kendaraan, 
    status_form_options, 
    meta_form__component_keys
)
from . import utils
from datetime import date, datetime
from . import compute

# Create your views here.
@login_required
def index(request):
    return render(request, 'app/index.html', {
        'title': 'Home',
        'active_tab': 'home'
    })

@login_required
def list_data_uji_kendaraan(request):
    keyword = request.GET.get('keyword', '')
    query = Q()
    if keyword:
        query = query | Q(nomor_kendaraan__icontains=keyword)
        query = query | Q(user_token__icontains=keyword)
        query = query | Q(nama_pemilik__icontains=keyword)

    all_data = DataUjiKendaraan.objects\
        .filter(query).all()
    total_data = DataUjiKendaraan.objects.filter(query).count()

    context = {
        'title': 'data uji kendaraan',
        'subtitle': f'total data {total_data}',
        'items': all_data,
        'total_data': total_data,
        'active_tab': 'data',
        'keyword': keyword
    }
    return render(request, 'app/data/list.html', context)

@login_required
def remove_data(request, id):
    item = DataUjiKendaraan.objects.get(id=id)
    item.delete()
    return redirect('list_data')

@login_required
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

        # Add user_token
        main_data['user_token'] = utils.random_name(n=10)

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
            'forms': meta_form__data_uji_kendaraan,
            'active_tab': 'data'
        }
        return render(request, 'app/data/add.html', context)

@login_required
def edit_data(request, id):
    item = DataUjiKendaraan.objects.get(id=id)
    if request.POST:
        exclude_keys = {
            'nomor_kendaraan',
            'nama_pemilik',
            'tanggal_pemeriksaan',
            'status',
            'bukti_name',
            'kendaraan_image',
            'csrfmiddlewaretoken'
        }
        data = request.POST.dict()
        item.nomor_kendaraan = data['nomor_kendaraan']
        item.nama_pemilik = data['nama_pemilik']

        k = 'tanggal_pemeriksaan'
        tgl = data[k]
        item.tanggal_pemeriksaan = datetime.strptime(tgl, '%Y-%m-%d').date()
        item.status = StatusPengujian(data['status'])

        file_keys = ['bukti_image', 'kendaraan_image']
        files = request.FILES
        new_random_name = utils.random_name()
        for i, fk in enumerate(file_keys):
            if fk not in files:
                continue
            updated_name = utils.file_random_name(files.get(fk), new_random_name, f'0{i + 1}')
            file = getattr(item, fk)
            file.save(updated_name, files[fk])

        for k in meta_form__component_keys:
            value =  not (k in data)
            setattr(item, k, value)

        item.save()
        return redirect('list_data')
    else:
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
            'status_form_options': status_form_options,
            'active_tab': 'data'
        }
        return render(request, 'app/data/edit.html', context)

@login_required
def classify_data(request, id):
    item = DataUjiKendaraan.objects.get(id=id)
    components_arr = []
    for group in meta_form__data_uji_kendaraan:
        for comp in group.components:
            if comp.separator:
                continue
            components_arr.append(1 if getattr(item, comp.name) else 0)
    class_result = compute.mult_nb(components_arr)
    context = {
        'item': item,
        'class_result': class_result,
        'active_tab': 'data'
    }
    return render(request, 'app/data/classification-result.html', context)

@login_required
def update_status(request, id):
    item = DataUjiKendaraan.objects.get(id=id)
    if not request.POST:
        return redirect('edit_data', args=(id,))
    data = request.POST
    item.status = StatusPengujian(data['status'])
    item.save()
    return redirect('edit_data', args=(id,))

@login_required
def statistik(request):
    aggregate = [
        { 'value': 'DR', 'label': 'draft', 'color': '#f59f00' },
        { 'value': 'TL', 'label': 'tidak lulus', 'color': '#d63939' },
        { 'value': 'LU', 'label': 'lulus', 'color': '#206bc4' }
    ]
    aggregate_result = list( DataUjiKendaraan.objects\
        .values('status').annotate(total=Count('id')) )
    aggregate_keys = { row['status'] for row in aggregate_result }

    for item in aggregate:
        agg_item = next(filter( lambda row: row['status'] == item['value'], aggregate_result ), { 'total': 0 })
        item['total'] = agg_item['total']
    context = {
        'title': "Statistik Data Kendaraan",
        'aggregate': aggregate,
        'active_tab': 'stat'
    }
    return render(request, 'app/statistik.html', context)

@login_required
def method_testing(request):
    context = {
        'active_tab': 'method_testing',
        'title': 'Pengujian Metode'
    }
    test_size = int(request.GET.get('test_size', 30))
    n_iteration = int(request.GET.get('n_iteration', 10))
    test_result = compute.test_method(
        test_size=test_size / 100.0,
        n_iteration=n_iteration
    )

    context.update(test_result)
    context['n_iteration'] = n_iteration
    context['test_size'] = test_size
    context['mean_acc'] = context['mean_acc'] * 100
    context['mean_err_rate'] = context['mean_err_rate'] * 100

    return render(request, 'app/method-testing.html', context)

@login_required
def method_testing_rev_1(request):
    context = {
        'active_tab': 'method_testing',
        'title': 'Pengujian Metode'
    }
    test_ratio = int(request.GET.get('test_ratio', 30))
    results = compute.test_method_rev_1(test_ratio=test_ratio)

    context['test_ratio'] = test_ratio
    # format the results for display
    _results = []
    for r in results:
        new_r = {
            **r,
            'acc': r['acc'] * 100,
            'err_rate': r['acc'] * 100
        }
        _results.append(new_r)
    context['results'] = _results

    # format total test and train for display
    context['display'] = {
        'n_test': test_ratio,
        'n_train': 100 - test_ratio
    }
    return render(request, 'app/method-testing-rev-1.html', context)

def test_report(request):
    url = "https://script.google.com/macros/s/1yAoLTR-MdSa-JqcUZr0h2NOHQXGkDIYk3y3sj_p_7mBvAF_20-X97soU/exec?name={}"
    name = request.GET['name']
    response = requests.get(url.format(name))
    response = requests.get(response.content)
    invoice_ids = ["", "456", "789"]
    with open("name_{name}.pdf", "wb") as f:
        f.write(response.content)
    return 'OK'
