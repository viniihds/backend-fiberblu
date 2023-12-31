# Generated by Django 4.2.4 on 2023-09-27 14:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("fiberblu", "0008_remove_itenscompra_compra_remove_itenscompra_produto_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="pedido",
            name="status",
            field=models.IntegerField(
                choices=[(1, "Carrinho"), (2, "Realizado"), (3, "Pago"), (4, "Entregue")], default=1
            ),
        ),
        migrations.AddField(
            model_name="pedido",
            name="usuario",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="compras",
                to=settings.AUTH_USER_MODEL,
            ),
            preserve_default=False,
        ),
    ]
