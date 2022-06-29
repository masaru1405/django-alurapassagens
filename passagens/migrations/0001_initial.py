# Generated by Django 4.0.5 on 2022-06-29 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Passagem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('origem', models.CharField(max_length=100)),
                ('destino', models.CharField(max_length=100)),
                ('data_ida', models.DateField()),
                ('data_volta', models.DateField()),
                ('data_pesquisa', models.DateField()),
                ('classe_viagem', models.TextField(choices=[('ECONOMICA', 'Econômica'), ('EXECUTIVA', 'Executiva'), ('PRIMEIRA_CLASSE', 'Primeira classe')], default=0, max_length=15)),
                ('informacoes', models.TextField(blank=True, max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Pessoa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]
