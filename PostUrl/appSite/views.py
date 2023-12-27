from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponse
from .models import FormUser



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
        # print(request.POST['number'])
        # print(request.POST['email'])
        # return HttpResponse('Ваш запрос принят')

        user_name = request.POST['last_name']  # получаем из пост запроса данные (имена находятся в html файла)
        user_email = request.POST['email']  # получаем из пост запроса данные (имена находятся в html файла)
        method = request.POST['method']

        if method == 'create':  # определяем какой метод (метод из html) - обновить или перезаписать
            user_age = request.POST['age']  # получаем из пост запроса данные (имена находятся в html файла)
            try:
                FormUser.objects.create(  # создание объекта в бд
                    name = user_name,  # Берётся из models переменная и ей присваивается значение переменной выше
                    email = user_email, # Берётся из models переменная и ей присваивается значение переменной выше
                    age = user_age # Берётся из models переменная и ей присваивается значение переменной выше
                ) 
            except:
                pass 
        elif method == "update":
            pass


        # проверка пользователя на наличие первый способ
        #data = FormUser.objects.filter(
            #name=user_name,  # поиски по колонкам на наличие через фильтрацию!
            #email= user_email  # поиски по колонкам на наличие через фильтрацию! 
        #) # если пользователь уже есть - он будет найден 
        #print(data) # вывод в консоль - найден, либо нет

        #----------------------------------------------------

        #if not data:  # если пользователь не найден, то создаётся объект
        # try:
        #     FormUser.objects.create(  # создание объекта в бд
        #         name = user_name,  # Берётся из models переменная и ей присваивается значение переменной выше
        #         email = user_email, # Берётся из models переменная и ей присваивается значение переменной выше
        #         age = user_age # Берётся из models переменная и ей присваивается значение переменной выше
        #     ) 
        # except:
        #     pass 
        return redirect('urlPageHome') # после создания объекта возвращаемся на страницу - urlPageHome

