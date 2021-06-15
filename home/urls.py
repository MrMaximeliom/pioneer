
from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('', views.home, name='home-page'),
    path('home/', views.home, name='home-page'),
    path('about/', views.about, name='about-page'),
    path('contactUs/', views.contactUs, name='contactUs-page'),
    path('termsAndConditions/', views.termsAndConditions, name='terms-page'),
    path('test/', views.test, name='test-page'),

]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)