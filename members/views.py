from django.shortcuts import render, redirect
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

def gu(req):
    num = req.GET.get('num','')
    return HttpResponse(f"<h1> {num}단 </h1> <br /> <h2> {num_gugu(num)} </h2>")

def num_gugu(num):
    str = ""
    for i in range(9):
        str += f"{int(num)} * {i+1} = {int(num) * (i + 1)} <br />"
    return str

def login(req):
    #print(dir(req))
    if req.method == 'GET':
        return render(req, 'login.html')
    elif req.method == 'POST':
        return redirect('/')