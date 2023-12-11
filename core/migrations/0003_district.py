# Generated by Django 4.2.7 on 2023-12-11 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_choleradatabase_cured'),
    ]

    operations = [
        migrations.CreateModel(
            name='District',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('Balaka', 'Balaka'), ('Blantyre', 'Blantyre'), ('Chikwawa', 'Chikwawa'), ('Chiradzulu', 'Chiradzulu'), ('Chitipa', 'Chitipa'), ('Dedza', 'Dedza'), ('Dowa', 'Dowa'), ('Karonga', 'Karonga'), ('Kasungu', 'Kasungu'), ('Likoma', 'Likoma'), ('Lilongwe', 'Lilongwe'), ('Machinga', 'Machinga'), ('Mangochi', 'Mangochi'), ('Mchinji', 'Mchinji'), ('Mulanje', 'Mulanje'), ('Mwanza', 'Mwanza'), ('Mzimba', 'Mzimba'), ('Nkhata Bay', 'Nkhata Bay'), ('Nkhotakota', 'Nkhotakota'), ('Nsanje', 'Nsanje'), ('Ntcheu', 'Ntcheu'), ('Ntchisi', 'Ntchisi'), ('Phalombe', 'Phalombe'), ('Rumphi', 'Rumphi'), ('Salima', 'Salima'), ('Thyolo', 'Thyolo'), ('Zomba', 'Zomba')], max_length=100)),
                ('latitude', models.FloatField(blank=True, null=True)),
                ('longitude', models.FloatField(blank=True, null=True)),
            ],
        ),
    ]
