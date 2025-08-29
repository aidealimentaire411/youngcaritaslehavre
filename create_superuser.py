import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'votre_projet.settings')
django.setup()

from django.contrib.auth import get_user_model

User = get_user_model()
if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser('admin2', 'h7c@hotmail.com', 'Mosta27000@')
    print("Superutilisateur créé avec succès!")
else:
    print("L'utilisateur admin existe déjà.")
