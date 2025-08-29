import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "aide_alim.settings")
django.setup()

from django.contrib.auth.models import User

username = "admin2"           # nom du superuser
email = "chouai.auto@gmail.com"  # email
password = "12345"   # mot de passe

if User.objects.filter(username=username).exists():
    user = User.objects.get(username=username)
    user.set_password(password)
    user.save()
    print(f"Mot de passe de {username} réinitialisé !")
else:
    User.objects.create_superuser(username=username, email, password)
    print(f"Superuser {username} créé !")
