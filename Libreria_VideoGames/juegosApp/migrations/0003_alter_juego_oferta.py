# Generated by Django 5.1 on 2024-11-08 21:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('juegosApp', '0002_alter_juego_oferta'),
    ]

    operations = [
        migrations.AlterField(
            model_name='juego',
            name='oferta',
            field=models.IntegerField(choices=[('0', '0%'), ('5', '5%'), ('10', '10%'), ('15', '15%'), ('20', '20%'), ('25', '25%'), ('30', '30%'), ('35', '35%'), ('40', '40%'), ('45', '45%'), ('50', '50%'), ('55', '55%'), ('60', '60%'), ('65', '65%'), ('70', '70%'), ('75', '75%'), ('80', '80%'), ('85', '85%'), ('90', '90%')]),
        ),
    ]
