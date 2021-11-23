from django.http import HttpResponse
from django.shortcuts import render
from app import models
from app.meta_form import meta_form__data_uji_kendaraan

# Create your views here.
def landing(request):
    return render(request, 'landing/index.html')

def get_info(request):
    token = request.GET['token']
    item = models.DataUjiKendaraan.objects.filter(user_token=token).get()
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
        'item': item,
        'forms': forms
    }
    return render(request, 'landing/info.html', context)
