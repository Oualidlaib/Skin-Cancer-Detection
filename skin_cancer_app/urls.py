from django.urls import path
from . import views
app_name = 'skin_cancer_app'
urlpatterns = [
    path('test/', views.testSkinCancer),
    path('history/', views.history),
    path('my-info/', views.user_informations),
]
