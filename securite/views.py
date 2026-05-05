from django.shortcuts import render
from django.contrib.admin.views.decorators import staff_member_required
from .models import AuditTrail, AlerteSecurite, JuridictionRole
from signalement.models import Signalement


@staff_member_required
def tableau_securite(request):
    audits = AuditTrail.objects.all()[:50]
    alertes = AlerteSecurite.objects.filter(resolue=False)
    alertes_critiques = alertes.filter(niveau='critical').count()
    alertes_warning = alertes.filter(niveau='warning').count()
    alertes_info = alertes.filter(niveau='info').count()
    total_signalements = Signalement.objects.count()
    signalements_recents = Signalement.objects.order_by('-date_soumission')[:5]
    roles = JuridictionRole.objects.filter(actif=True)

    context = {
        'audits': audits,
        'alertes': alertes,
        'alertes_critiques': alertes_critiques,
        'alertes_warning': alertes_warning,
        'alertes_info': alertes_info,
        'total_signalements': total_signalements,
        'signalements_recents': signalements_recents,
        'roles': roles,
    }
    return render(request, 'securite/tableau.html', context)


def conformite(request):
    total_audits = AuditTrail.objects.count()
    acces_refuses = AuditTrail.objects.filter(action='acces_refuse').count()
    exports = AuditTrail.objects.filter(action='export').count()
    alertes_non_resolues = AlerteSecurite.objects.filter(resolue=False).count()

    context = {
        'total_audits': total_audits,
        'acces_refuses': acces_refuses,
        'exports': exports,
        'alertes_non_resolues': alertes_non_resolues,
    }
    return render(request, 'securite/conformite.html', context)