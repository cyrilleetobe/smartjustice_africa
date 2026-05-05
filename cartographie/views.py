import folium
from django.shortcuts import render
from .models import Tribunal


def carte_tribunaux(request):
    carte = folium.Map(
        location=[4.5, 11.5],
        zoom_start=6,
        tiles='CartoDB positron'
    )

    tribunaux = Tribunal.objects.all()

    for t in tribunaux:
        taux = t.taux_traitement()
        if taux < 40:
            couleur = 'red'
        elif taux < 70:
            couleur = 'orange'
        else:
            couleur = 'green'

        popup_html = f"""
        <div style="font-family:Arial;min-width:200px">
            <h4 style="color:#1a1a2e;margin:0 0 8px">{t.nom}</h4>
            <b>Ville :</b> {t.ville}<br>
            <b>Dossiers total :</b> {t.dossiers_total}<br>
            <b>En attente :</b> {t.dossiers_en_attente}<br>
            <b>Traites :</b> {t.dossiers_traites}<br>
            <b>Magistrats :</b> {t.magistrats}<br>
            <hr>
            <b>Taux de traitement :</b> {taux}%
        </div>
        """

        folium.Marker(
            location=[t.latitude, t.longitude],
            popup=folium.Popup(popup_html, max_width=250),
            tooltip=t.nom,
            icon=folium.Icon(color=couleur, icon='info-sign')
        ).add_to(carte)

    carte_html = carte._repr_html_()

    context = {
        'carte_html': carte_html,
        'tribunaux': tribunaux,
    }
    return render(request, 'cartographie/carte.html', context)