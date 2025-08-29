import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "aide_alim.settings")
django.setup()

from django.contrib.auth.models import User

# Remplace par les informations de ton nouveau superuser
username = "adminn"
email = "nouveladmin@example.com"
password = "nv123"

if User.objects.filter(username=username).exists():
    print(f"L'utilisateur {username} existe déjà.")
else:
    User.objects.create_superuser(username=username, email=email, password=password)
    print(f"Superuser {username} créé !")
