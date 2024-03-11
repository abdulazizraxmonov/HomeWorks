import os
from django.shortcuts import render

def theme_list(request):
    file_path = os.path.join(os.path.dirname(__file__), 'Lessons.txt')
    
    with open(file_path, 'r') as file:
        lessons = file.readlines()
    
    return render(request, 'themes/theme_list.html', {'lessons': lessons})