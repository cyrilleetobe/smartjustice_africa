from .models import AuditTrail, AlerteSecurite


def enregistrer_action(utilisateur, action, description, request=None, tribunal=''):
    adresse_ip = None
    if request:
        x_forwarded = request.META.get('HTTP_X_FORWARDED_FOR')
        adresse_ip = x_forwarded.split(',')[0] if x_forwarded else request.META.get('REMOTE_ADDR')

    AuditTrail.objects.create(
        utilisateur=utilisateur,
        action=action,
        tribunal=tribunal,
        description=description,
        adresse_ip=adresse_ip,
    )


def creer_alerte(niveau, titre, description, tribunal=''):
    AlerteSecurite.objects.create(
        niveau=niveau,
        titre=titre,
        description=description,
        tribunal=tribunal,
    )


def verifier_integrite(audit_id):
    import hashlib
    try:
        audit = AuditTrail.objects.get(id=audit_id)
        contenu = f"{audit.utilisateur}{audit.action}{audit.description}{audit.adresse_ip}"
        checksum_actuel = hashlib.sha256(contenu.encode()).hexdigest()
        return checksum_actuel == audit.checksum
    except AuditTrail.DoesNotExist:
        return False