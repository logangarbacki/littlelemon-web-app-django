from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0004_menuitem_description_menuitem_ordering_booking_user_booking_status_booking_created_at'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_number', models.IntegerField(unique=True)),
                ('items', models.JSONField(default=list)),
                ('subtotal', models.DecimalField(decimal_places=2, max_digits=8)),
                ('delivery_fee', models.DecimalField(decimal_places=2, default=3.99, max_digits=6)),
                ('tip', models.DecimalField(decimal_places=2, default=0, max_digits=6)),
                ('discount', models.DecimalField(decimal_places=2, default=0, max_digits=6)),
                ('total', models.DecimalField(decimal_places=2, max_digits=8)),
                ('address', models.CharField(max_length=500)),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('status', models.CharField(
                    choices=[('preparing', 'Preparing'), ('on_the_way', 'On the Way'), ('delivered', 'Delivered')],
                    default='preparing',
                    max_length=20,
                )),
                ('eta', models.IntegerField(default=30)),
                ('placed_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE,
                    related_name='orders',
                    to=settings.AUTH_USER_MODEL,
                )),
            ],
            options={'ordering': ['-placed_at']},
        ),
    ]
