from rest_framework.decorators import api_view
from rest_framework.response import Response
from cartographie.models import Tribunal
from signalement.models import Signalement
from securite.models import AuditTrail


@api_view(['GET'])
def api_tribunaux(request):
    tribunaux = Tribunal.objects.all()
    data = []
    for t in tribunaux:
        data.append({
            'id': t.id,
            'nom': t.nom,
            'ville': t.ville,
            'latitude': t.latitude,
            'longitude': t.longitude,
            'dossiers_total': t.dossiers_total,
            'dossiers_en_attente': t.dossiers_en_attente,
            'dossiers_traites': t.dossiers_traites,
            'magistrats': t.magistrats,
            'taux_traitement': t.taux_traitement(),
        })
    return Response({'tribunaux': data, 'total': len(data)})


@api_view(['GET'])
def api_stats(request):
    tribunaux = Tribunal.objects.all()
    total_dossiers = sum(t.dossiers_total for t in tribunaux)
    total_attente = sum(t.dossiers_en_attente for t in tribunaux)
    total_traites = sum(t.dossiers_traites for t in tribunaux)
    taux_global = round((total_traites / total_dossiers * 100), 1) if total_dossiers > 0 else 0

    return Response({
        'dossiers': {
            'total': total_dossiers,
            'en_attente': total_attente,
            'traites': total_traites,
            'taux_global': taux_global,
        },
        'signalements': {
            'total': Signalement.objects.count(),
            'corruption': Signalement.objects.filter(type_signalement='corruption').count(),
            'violation': Signalement.objects.filter(type_signalement='violation').count(),
            'fuite': Signalement.objects.filter(type_signalement='fuite').count(),
        },
        'securite': {
            'total_audits': AuditTrail.objects.count(),
        }
    })


@api_view(['GET'])
def api_signalements(request):
    signalements = Signalement.objects.order_by('-date_soumission')[:20]
    data = []
    for s in signalements:
        data.append({
            'code_anonyme': s.code_anonyme,
            'type': s.get_type_signalement_display(),
            'tribunal': s.tribunal_concerne,
            'statut': s.get_statut_display(),
            'date_soumission': s.date_soumission.strftime('%d/%m/%Y %H:%M'),
        })
    return Response({'signalements': data, 'total': len(data)})