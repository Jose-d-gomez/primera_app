"""encuesta URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from django.contrib.auth.views import LoginView, PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView, logout_then_login
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy


urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^preguntas/', include ('apps.preguntas.urls', namespace="pregunta")),

    url(r'^usuarios/', include ('apps.usuarios.urls', namespace="usuarios")),

    url(r'^accounts/login/', LoginView.as_view(template_name='index.html'), name="login"),

    url(r'^logout/',logout_then_login, name='logout'),

    path('reset/password_reset', PasswordResetView.as_view(email_template_name="registration/password_reset_email.html"), name = 'password_reset'),

    path('reset/password_reset_done', PasswordResetDoneView.as_view(), name = 'password_reset_done'),

    path('reset/<uidb64>/<token>', PasswordResetConfirmView.as_view(), name = 'password_reset_confirm'),

    path('reset/done',PasswordResetCompleteView.as_view() , name = 'password_reset_complete'),
 
]

