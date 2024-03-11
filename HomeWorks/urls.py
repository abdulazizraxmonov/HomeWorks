from django.urls import path
from Themes.views import theme_list
from Pupils.views import pupil_list, pupil_detail

urlpatterns = [
    path('themes/', theme_list, name='theme_list'),
    path('pupils/', pupil_list, name='pupil_list'),
    path('pupils/<int:id>/', pupil_detail, name='pupil_detail'),
    path('', theme_list, name='theme_list'),
]