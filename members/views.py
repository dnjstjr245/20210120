from django.shortcuts import render
from django.http.response import HttpResponse
from .models import Members

# Create your views here.

def index(request):
    return HttpResponse("<h1>version 1 : dynamic page<h1>")

def test(request):
    return HttpResponse("<h2>Test<h2>")

def signup(req):
    if req.method == 'POST' :
        username = req.POST['username']
        email = req.POST['email']

        member = Members(
            username = username,
            useremail = email
        )

        member.save()

        res_data ={}
        res_data['res'] = '등록성공'

        return render(req, 'index.html', res_data)
    return render(req, 'index.html')

def git(req):
    return HttpResponse("<h2>git version</h2>")