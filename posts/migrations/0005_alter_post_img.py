# ~~~~~
from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_post_img'),
    ]
    operations = [
        migrations.AlterField(
            model_name='post',
            name='img',
            field=models.ImageField(upload_to='images'),
        ),
    ]
