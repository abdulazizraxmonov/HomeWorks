from django.shortcuts import render

def pupil_list(request):
    pupils = [
        {'id': 1, 'name': 'Inomjon Qurbonov', 'bir': '3,  5,  2', 'iki': '5, 10, 5', 'uch': '5, 5', 'jami': '37'},
        {'id': 2, 'name': 'Muhammadyusuf Abdulayev', 'bir': '2,  4,  1', 'iki': '5, 10, 5', 'uch': '5, 5', 'jami': '37'},
        {'id': 3, 'name': 'Shohruhbek Turdaliyev', 'bir': '3,  5,  2', 'iki': '4, 10, 4', 'uch': '5, 3', 'jami': '36'},
        {'id': 4, 'name': 'Zafarbek Olimboyev', 'bir': '3,  5,  2', 'iki': '3, 10, 1', 'uch': '5, 3', 'jami': '39'},
        {'id': 5, 'name': 'Samariddin Baxtiyorov', 'bir': '2,  5,  2', 'iki': '3, 10, 1', 'uch': '5, 3', 'jami': '36'},
    ]
    return render(request, 'pupils/pupil_list.html', {'pupils': pupils})

def pupil_detail(request, id):
    pupils = [
        {'id': 1, 'name': 'Inomjon Qurbonov', 'bir': '3,  5,  2', 'iki': '5, 10, 5', 'uch': '5, 5', 'jami': '37'},
        {'id': 2, 'name': 'Muhammadyusuf Abdulayev', 'bir': '2,  4,  1', 'iki': '5, 10, 5', 'uch': '5, 5', 'jami': '37'},
        {'id': 3, 'name': 'Shohruhbek Turdaliyev', 'bir': '3,  5,  2', 'iki': '4, 10, 4', 'uch': '5, 3', 'jami': '36'},
        {'id': 4, 'name': 'Zafarbek Olimboyev', 'bir': '3,  5,  2', 'iki': '3, 10, 1', 'uch': '5, 3', 'jami': '39'},
        {'id': 5, 'name': 'Samariddin Baxtiyorov', 'bir': '2,  5,  2', 'iki': '3, 10, 1', 'uch': '5, 3', 'jami': '36'},
    ]
    pupil = next((p for p in pupils if p['id'] == id), None)
    return render(request, 'pupils/pupil_detail.html', {'pupil': pupil})