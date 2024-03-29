# Generated by Django 3.0.3 on 2021-04-21 16:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AssetsModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('asset_name', models.CharField(default='asset', max_length=100)),
                ('asset_type', models.CharField(default='asset', max_length=100)),
                ('asset_price', models.DecimalField(decimal_places=2, default=0.0, max_digits=9, null=True)),
                ('quantity', models.DecimalField(decimal_places=1, default=0, max_digits=3, null=True)),
                ('total_price', models.DecimalField(decimal_places=2, default=0.0, max_digits=9, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(default='Name of Customer', max_length=100)),
                ('phone_number', models.CharField(default='Number is not set', max_length=100)),
                ('customer_discount', models.IntegerField(default=0)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Package',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('package_name', models.CharField(default='package', max_length=100)),
                ('package_specification', models.CharField(default='package', max_length=250)),
                ('package_price', models.DecimalField(decimal_places=2, default='0', max_digits=8)),
            ],
        ),
        migrations.CreateModel(
            name='StoreExpensesModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, default=0.0, max_digits=9, null=True)),
                ('expense_type', models.CharField(choices=[('المأكولات والمنثورات', 'المأكولات والمنثورات'), ('احتياجات', 'احتياجات الورشه'), ('مدفوعات مقدمه', 'مدفوعات مقدمه'), ('رواتب', 'رواتب'), ('اخرى', 'اخرى')], default='Food', max_length=20)),
                ('description', models.TextField(blank=True, default='')),
            ],
        ),
        migrations.CreateModel(
            name='Vehicles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('make', models.CharField(default='make', max_length=100)),
                ('model', models.CharField(default='model', max_length=100)),
                ('plate_num', models.CharField(default='plate number', max_length=100)),
                ('color', models.CharField(default='color', max_length=100)),
                ('mileage', models.CharField(default='mi', max_length=100)),
                ('customer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='customer', to='store.Customer')),
            ],
        ),
        migrations.CreateModel(
            name='PurchasesModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now=True)),
                ('bookings', models.DateField()),
                ('payments', models.DecimalField(decimal_places=2, default=0.0, max_digits=6, null=True)),
                ('payable', models.DecimalField(decimal_places=2, default=0.0, max_digits=6, null=True)),
                ('package', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='store.Package')),
                ('vehicle', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='store.Vehicles')),
            ],
        ),
    ]
