# Generated by Django 4.0.3 on 2022-03-30 19:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0008_alter_author_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='books_img', to='books.author'),
        ),
    ]
