from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='app_index'),
    path('data', views.list_data_uji_kendaraan, name='list_data'),
    path('data/tambah', views.add_data, name='add_data'),
    path('data/<int:id>/remove', views.remove_data, name='remove_data'),
    path('data/<int:id>/edit', views.edit_data, name='edit_data'),
    path('data/<int:id>/classify', views.classify_data, name='classify_data'),
    path('statistik', views.statistik, name='statistik'),
    path('method-testing', views.method_testing, name='method_testing'),
    path('method-testing-rev-1', views.method_testing_rev_1, name='method_testing_rev_1')
]
