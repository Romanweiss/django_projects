from django.shortcuts import render
from django.views import View
from django.http import HttpResponse


class PageHome(View):
    template_home = 'appSite/index.html'

    def get(self, request):  # переход по сайту
        return render(request, self.template_home)

    def post(self, request):  # отправка данных на сервер
        print(request.POST)
        return HttpResponse('Ваш запрос принят')

