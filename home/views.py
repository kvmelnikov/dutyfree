from django.shortcuts import render
from django.views import View

class HomeView(View):
    def get(self, request):
        context = {'hello': 'Добро пожаловать'}
        return render(request, 'home/main.html', context)

