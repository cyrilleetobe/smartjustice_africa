from django.shortcuts import render
from cartographie.models import Tribunal
from signalement.models import Signalement
from securite.models import AuditTrail, AlerteSecurite


def dashboard_principal(request):
    # Stats tribunaux
    tribunaux = Tribunal.objects.all()
    total_dossiers = sum(t.dossiers_total for t in tribunaux)
    total_attente = sum(t.dossiers_en_attente for t in tribunaux)
    total_traites = sum(t.dossiers_traites for t in tribunaux)
    total_magistrats = sum(t.magistrats for t in tribunaux)

    # Stats signalements
    total_signalements = Signalement.objects.count()
    signalements_recents = Signalement.objects.order_by('-date_soumission')[:5]
    sig_corruption = Signalement.objects.filter(type_signalement='corruption').count()
    sig_violation = Signalement.objects.filter(type_signalement='violation').count()
    sig_fuite = Signalement.objects.filter(type_signalement='fuite').count()

    # Stats securite
    alertes_actives = AlerteSecurite.objects.filter(resolue=False).count()
    derniers_audits = AuditTrail.objects.order_by('-horodatage')[:5]

    # Taux global
    taux_global = round((total_traites / total_dossiers * 100), 1) if total_dossiers > 0 else 0

    context = {
        'tribunaux': tribunaux,
        'total_dossiers': total_dossiers,
        'total_attente': total_attente,
        'total_traites': total_traites,
        'total_magistrats': total_magistrats,
        'taux_global': taux_global,
        'total_signalements': total_signalements,
        'signalements_recents': signalements_recents,
        'sig_corruption': sig_corruption,
        'sig_violation': sig_violation,
        'sig_fuite': sig_fuite,
        'alertes_actives': alertes_actives,
        'derniers_audits': derniers_audits,
    }
    return render(request, 'dashboard/dashboard.html', context)


def accueil(request):
    from cartographie.models import Tribunal
    from signalement.models import Signalement
    tribunaux = Tribunal.objects.all()
    total_dossiers = sum(t.dossiers_total for t in tribunaux)
    total_signalements = Signalement.objects.count()
    return render(request, 'dashboard/accueil.html', {
        'total_dossiers': total_dossiers,
        'total_signalements': total_signalements,
        'nb_tribunaux': tribunaux.count(),
    })