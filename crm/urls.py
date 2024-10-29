from django.contrib import admin
from django.urls import path

from leads.views import lead_list

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', lead_list),
]
