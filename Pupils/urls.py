from django.urls import path
from . import views

app_name = 'pupils'

urlpatterns = [
    path('', views.pupil_list, name='pupil_list'),
    path('<int:id>/', views.pupil_detail, name='pupil_detail'),
]