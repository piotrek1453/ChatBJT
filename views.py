from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import QueryDict



def home_view(*args, **kwargs):
    return HttpResponse('''
                            <form action="/send/" method="get">
                                <input type="text" id="message" name="message">
                            </form>                       
                        ''')


def get_mess(request):
    print(request.GET['message'])
    return HttpResponseRedirect('/')
