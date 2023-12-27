from django.shortcuts import render
from django.views import View
from django.http import HttpResponse


class PageHome(View):
    template_home = 'appSite/index.html'

    def get(self, request):  # переход по сайту
        # ses = request.session.get('hist', False)
        # if ses:
        #     return HttpResponse('Сессия есть')
        # else:
        #     request.session['hist'] = 'ok'
        #     return HttpResponse('сессии нет')
        return render(request, self.template_home)

    def post(self, request):  # отправка данных на сервер
        print(request.POST['number'])
        print(request.POST['email'])
        return HttpResponse('Ваш запрос принят')

