from django.contrib import admin

# Register your models here.
from .models import Opgaver, Kunder

admin.site.register(Opgaver)
admin.site.register(Kunder)