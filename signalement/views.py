from django.shortcuts import render, redirect
from django.utils import timezone
from .forms import SignalementForm
from .models import Signalement
from .encryption import chiffrer, calculer_checksum, sauvegarder_json


def formulaire_signalement(request):
    if request.method == 'POST':
        form = SignalementForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            description_chiffree = chiffrer(data['description'])
            preuves_chiffrees = chiffrer(data['preuves']) if data['preuves'] else ''
            checksum = calculer_checksum(data['description'])
            signalement = Signalement.objects.create(
                type_signalement=data['type_signalement'],
                tribunal_concerne=data['tribunal_concerne'],
                date_incident=data['date_incident'],
                description_chiffree=description_chiffree,
                preuves_chiffrees=preuves_chiffrees,
                checksum=checksum,
            )
            json_data = {
                'code_anonyme': signalement.code_anonyme,
                'type': data['type_signalement'],
                'tribunal': data['tribunal_concerne'],
                'date_incident': str(data['date_incident']),
                'description_chiffree': description_chiffree,
                'preuves_chiffrees': preuves_chiffrees,
                'checksum': checksum,
                'date_soumission': str(timezone.now()),
            }
            sauvegarder_json(json_data, signalement.code_anonyme)
            return redirect('confirmation_signalement', code=signalement.code_anonyme)
    else:
        form = SignalementForm()
    return render(request, 'signalement/formulaire.html', {'form': form})


def confirmation_signalement(request, code):
    try:
        signalement = Signalement.objects.get(code_anonyme=code)
    except Signalement.DoesNotExist:
        return redirect('formulaire_signalement')
    return render(request, 'signalement/confirmation.html', {
        'code': signalement.code_anonyme,
        'type': signalement.get_type_signalement_display(),
        'date': signalement.date_soumission,
        'statut': signalement.get_statut_display(),
    })


def suivi_signalement(request):
    code = None
    signalement = None
    erreur = None
    if request.method == 'POST':
        code = request.POST.get('code', '').strip().upper()
        try:
            signalement = Signalement.objects.get(code_anonyme=code)
        except Signalement.DoesNotExist:
            erreur = 'Code introuvable. Verifiez votre code de suivi.'
    return render(request, 'signalement/suivi.html', {
        'signalement': signalement,
        'erreur': erreur,
        'code': code,
    })