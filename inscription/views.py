from django.shortcuts import render, redirect
from django.core.mail import send_mail
from .forms import EtudiantForm
from django.conf import settings
from django.utils.html import strip_tags
from django.template.loader import render_to_string

def inscription_etudiant(request):
    if request.method == 'POST':
        form = EtudiantForm(request.POST)
        if form.is_valid():
            etudiant = form.save()

            # Charger le template msg.html avec les données de l'étudiant
            message_html = render_to_string('inscription/msg.html', {'etudiant': etudiant})

            send_mail(
                subject="Bienvenue ! Votre inscription est confirmée",
                message=strip_tags(message_html),  # version texte simple
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[etudiant.email],
                html_message=message_html
            )

            return render(request, 'inscription/succes.html')
    else:
        form = EtudiantForm()
    return render(request, 'inscription/inscription.html', {'form': form})


def accueil(request):
    return render(request, 'inscription/accueil.html')
