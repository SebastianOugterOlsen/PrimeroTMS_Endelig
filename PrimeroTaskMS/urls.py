from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView

from opgaver.views import home_view, opgaver_detail_view, opgaver_opret_view, opgaver_rediger_view, opgaver_slet_view, kunder_detail_view, kunder_opret_view, kunder_rediger_view, kunder_slet_view, opgaver_inaktive_view

urlpatterns = [
    path('', home_view, name='home'),
    path('home/', home_view),
    path('opgaver/', opgaver_detail_view, name='opgaver_detail'),
    path('opgaver_opret/', opgaver_opret_view),
    path('opgaver_rediger/<str:pk>/', opgaver_rediger_view, name="opgaver_rediger"),
    path('opgaver_slet/<str:pk>/', opgaver_slet_view, name="opgaver_slet"),
    path('kunder/', kunder_detail_view, name='opgaver_detail'),
    path('kunder_opret/', kunder_opret_view),
    path('kunder_rediger/<str:pk>/', kunder_rediger_view, name="rediger_kunde"),
    path('kunder_slet/<str:pk>/', kunder_slet_view, name="slet_kunde"),
    path('admin/', admin.site.urls),
    path('home/', include('django.contrib.auth.urls')),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),

    path('opgaver_inaktive/', opgaver_inaktive_view, name="inaktive_opgaver"),
]
