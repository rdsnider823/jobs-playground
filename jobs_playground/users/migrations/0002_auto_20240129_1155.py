from django.contrib.auth.hashers import make_password
from django.db import migrations


def create_users(apps, schema_editor):
    User = apps.get_model("users", "User")

    User(
        name="Super User",
        email="super@example.com",
        is_staff=True,
        is_superuser=True,
        password=make_password("123"),  # You should choose a secure password.
    ).save()

    User(
        name="Jane Doe",
        email="jane.doe@example.com",
        is_staff=False,
        is_superuser=False,
        password=make_password("123"),  # You should choose a secure password.
    ).save()


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.RunPython(create_users, migrations.RunPython.noop),
    ]
