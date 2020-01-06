from django import forms

from .models import Opgaver
from .models import Kunder

class DateInput(forms.DateInput):
    input_type = 'date'

class OpgaverForm(forms.ModelForm):
    class Meta:
        model = Opgaver
        fields = [
            'kunde_navn',
            'ansvarlig',
            'opgave_beskrivelse',
            'noter',
            'tid_brugt',
            'status',
            'deadline',
            'prioritet'
            ]

class KunderForm(forms.ModelForm):
    class Meta:
        model = Kunder
        fields = [
            'kunde_id',
            'kunde_navn',
            'kunde_installation',
            'kunde_adresse',
            'kontaktperson',
            'kontakt_tlf',
            'kontakt_mail']