from django import forms


class SignalementForm(forms.Form):
    TYPE_CHOICES = [
        ('', '-- Choisir le type --'),
        ('corruption', 'Corruption judiciaire'),
        ('violation', 'Violation de droits'),
        ('fuite', 'Fuite de donnees'),
    ]
    TRIBUNAL_CHOICES = [
        ('', '-- Choisir le tribunal --'),
        ('TGI Yaounde', 'Tribunal de Grande Instance de Yaounde'),
        ('TGI Douala', 'Tribunal de Grande Instance de Douala'),
        ('TGI Bafoussam', 'Tribunal de Grande Instance de Bafoussam'),
    ]
    type_signalement = forms.ChoiceField(
        choices=TYPE_CHOICES,
        label='Type de signalement',
        widget=forms.Select(attrs={'class': 'form-select'})
    )
    tribunal_concerne = forms.ChoiceField(
        choices=TRIBUNAL_CHOICES,
        label='Tribunal concerne',
        widget=forms.Select(attrs={'class': 'form-select'})
    )
    date_incident = forms.DateField(
        label="Date de l'incident",
        widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'})
    )
    description = forms.CharField(
        label='Description des faits',
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'rows': 6,
            'placeholder': 'Decrivez les faits de maniere precise. Aucune donnee personnelle ne sera conservee.'
        })
    )
    preuves = forms.CharField(
        label='Elements de preuve (optionnel)',
        required=False,
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'rows': 3,
            'placeholder': 'References de documents, dates, lieux...'
        })
    )
    confirmation = forms.BooleanField(
        label='Je confirme que ces informations sont exactes et soumises de bonne foi.',
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'})
    )