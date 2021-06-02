from django.shortcuts import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def message(request):
    return HttpResponse("Djangoを使って文字を表示することができました！")
