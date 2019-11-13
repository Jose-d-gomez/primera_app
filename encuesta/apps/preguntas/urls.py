from django.urls import path
from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from apps.preguntas.views import index, encuesta_view, testview, listar_encuesta, editar_encuesta, eliminar_encuesta, EncuestaList, EncuestaCreate, EncuestaUpdate, EncuestaDelete
app_name ="preguntas"

urlpatterns = [
    url(r'^nuevo$',login_required(EncuestaCreate.as_view()) ,name='formulario'),
    url(r'^error$',testview ,name='error'),
    url(r'^listar$',login_required(EncuestaList.as_view()), name='listar_encuestas'),
    url(r'^editar/(?P<pk>\d+)/$',login_required(EncuestaUpdate.as_view()) ,name='editar_encuestas'),
    url(r'^eliminar/(?P<pk>\d+)/$',login_required(EncuestaDelete.as_view()) ,name='eliminar_encuestas'),
]
