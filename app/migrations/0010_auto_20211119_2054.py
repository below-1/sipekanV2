# Generated by Django 3.2.9 on 2021-11-19 20:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_auto_20211119_1719'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dataujikendaraan',
            name='lulus',
        ),
        migrations.AddField(
            model_name='dataujikendaraan',
            name='status',
            field=models.CharField(choices=[('DR', 'Draft'), ('LU', 'Lulus'), ('TL', 'Tidak Lulus')], default='DR', max_length=2),
        ),
    ]
