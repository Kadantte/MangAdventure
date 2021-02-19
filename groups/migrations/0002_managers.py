from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('groups', '0001_squashed'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='manager',
            field=models.ForeignKey(
                help_text='The person who manages this group.',
                blank=False, null=True, on_delete=models.SET_DEFAULT,
                to=settings.AUTH_USER_MODEL, limit_choices_to=models.Q(
                    ('is_superuser', True),
                    ('groups__name', 'Scanlator'),
                    _connector='OR'
                ),
            ),
        ),
        migrations.AlterModelOptions(
            name='role', options={'verbose_name': 'role'},
        ),
    ]
