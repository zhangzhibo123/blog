
from django.conf.urls import url
from django.contrib import admin


from account import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^test/', views.index),
]
