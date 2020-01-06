from django.db import models
from django.conf import settings
from datetime import datetime
from django.contrib.auth.models import User



class Opgaver(models.Model):
    kunde_navn = models.CharField(max_length=30)  # Når man bruger char skal man have en max længde
    ansvarlig = models.ForeignKey(  # Man kan vælge mellem oprettede medarbejdere
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE, )
    opgave_beskrivelse = models.TextField(blank=True, null=True)
    noter = models.TextField(blank=True, null=True)
    tid_brugt = models.FloatField()
    status = models.IntegerField(choices=((1, ("Ikke angivet")),
                                          (2, ("Startet")),
                                          (3, ("Halvvejs")),
                                          (4, ("Sidste Detaljer")),
                                          (5, ("Færdig"))), default=1)
    prioritet = models.IntegerField(choices=((1, ("Højeste")),
                                             (2, ("Mellem")),
                                             (3, ("Laveste"))), default=3)
    deadline = models.DateField(default=datetime.now)

    class Meta:
        ordering = ('prioritet', 'deadline')  # So rterer først efter prioritering og derefter deadline

    def __str__(self):  # viser objectets navn i stedet for nr. i admin
        return str(self.kunde_navn)



class Kunder(models.Model):
    kunde_id = models.CharField(max_length=4, unique=True)
    kunde_navn = models.CharField(max_length=30)
    kunde_installation = models.TextField(blank=True, null=True)
    kunde_adresse = models.TextField(blank=True, null=True, help_text="Gadenavn, nr., Postnummer og By")
    kontaktperson = models.CharField(max_length=30)
    kontakt_tlf = models.CharField(max_length=10)
    kontakt_mail = models.EmailField(max_length=254)

    class Meta:
        ordering = ('kunde_navn',)  # Sorterer efter kunde navn

    def __str__(self):  # viser objectets navn i stedet for nr. i admin
        return str(self.kunde_navn)

