# Generated by Django 4.2.4 on 2023-09-26 19:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("fiberblu", "0005_pagamento"),
    ]

    operations = [
        migrations.RenameField(
            model_name="pagamento",
            old_name="nome",
            new_name="descricao",
        ),
        migrations.AddField(
            model_name="pedido",
            name="pagamento",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="pagamentos",
                to="fiberblu.pagamento",
            ),
            preserve_default=False,
        ),
    ]
