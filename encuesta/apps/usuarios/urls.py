from django.conf.urls import url
from apps.usuarios.views import RegistroUsuario
app_name ="usuarios"

urlpatterns = [
    url(r'^registrar', RegistroUsuario.as_view(), name="registrar"),

]