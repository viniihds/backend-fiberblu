# Generated by Django 4.2.4 on 2023-08-09 14:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fiberblu', '0002_linhaproduto'),
    ]

    operations = [
        migrations.CreateModel(
            name='GrupoProduto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cor', models.CharField(max_length=100)),
                ('volume', models.CharField(max_length=100)),
                ('codigo', models.IntegerField()),
                ('preco', models.DecimalField(decimal_places=2, max_digits=8)),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='produtos', to='fiberblu.categoriaproduto')),
                ('grupo', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='produtos', to='fiberblu.grupoproduto')),
                ('linha', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='produtos', to='fiberblu.linhaproduto')),
            ],
        ),
    ]