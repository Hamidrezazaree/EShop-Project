# Generated by Django 4.2 on 2023-05-05 16:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('price', models.IntegerField(verbose_name='قیمت')),
                ('short_description', models.CharField(db_index=True, max_length=360, null=True, verbose_name='توضیحات کوتاه')),
                ('description', models.TextField(db_index=True, verbose_name='توضیحات اصلی ')),
                ('is_active', models.BooleanField(default=False, max_length=300, verbose_name='فعال/غیرفعال')),
                ('slug', models.SlugField(blank=True, default='')),
                ('is_delete', models.BooleanField(verbose_name='حذف شده/ نشده')),
            ],
            options={
                'verbose_name': 'محصول',
                'verbose_name_plural': 'محصولات',
            },
        ),
        migrations.CreateModel(
            name='ProductCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=360, verbose_name='عنوان')),
                ('url_title', models.CharField(db_index=True, max_length=360, verbose_name='عنوان در  url')),
                ('is_active', models.BooleanField(verbose_name='فعال/غیرفعال')),
                ('is_delete', models.BooleanField(verbose_name='حذف شده/نشده')),
            ],
            options={
                'verbose_name': 'دسته بندی',
                'verbose_name_plural': 'دسته بندی ها',
            },
        ),
        migrations.CreateModel(
            name='ProductTag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('caption', models.CharField(db_index=True, max_length=300, verbose_name='عنوان')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product_module.product', verbose_name='product_tags')),
            ],
            options={
                'verbose_name': 'تگ محصول',
                'verbose_name_plural': ' تگ های محصولات',
            },
        ),
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.ManyToManyField(related_name='product_categories', to='product_module.productcategory', verbose_name='دسته بندی'),
        ),
    ]
