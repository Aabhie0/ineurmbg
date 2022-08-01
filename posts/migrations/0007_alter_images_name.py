# ~~~~~

from django.db import migrations, models
class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0006_images'),
    ]

    operations = [
        migrations.AlterField(
            model_name='images',
            name='name',
            field=models.CharField(default='Undefined', max_length=40),
        ),
    ]