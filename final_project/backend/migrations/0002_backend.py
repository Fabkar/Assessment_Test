# Generated by Django 3.2 on 2021-04-23 15:31

from django.db import migrations

def create_data(apps, schema_editor):
    Client = apps.get_model('backend', 'Client')
    Client(gov_id="Cos001",
           first_name="Costumer001",
           last_name="Costumer001",
           email="001@email.com",
           company="CostumerINC").save()

class Migration(migrations.Migration):
    dependencies = [
        ('backend', '0001_initial'),
    ]
    operations = [
        migrations.RunPython(create_data),
    ]