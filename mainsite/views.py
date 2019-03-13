import io
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpResponse, FileResponse
from reportlab.pdfgen import canvas
from .models import User
from mainsite import models, forms

def some_view(request):
    if request.method == 'POST':
        buffer = io.BytesIO()
        p = canvas.Canvas(buffer)
        p.drawString(100, 100, "Hello world.")
        p.showPage()
        p.save()
    return FileResponse(buffer, as_attachment=True, filename='hello.pdf')

# def item(request):
#     items = Item.objects.all()
#     return render(request, 'index.html', locals())
# Create your views here.

def showitem(request, slug):
    try:
        item = Item.objects.get(slug = slug)
        if item != None:
            return render(request, 'item.html', locals())
    except:
        return redirect('/')

def contact(request):
    form = forms.ContactForm(request.POST)
    if form.is_valid():
        user_name = form.cleaned_data['user_name']

    return render(request,'contact.html',locals())

def login(request):
    if request.method == 'POST':
        login_form = forms.LoginForm(request.POST)
        if login_form.is_valid():
            login_name = request.POST['username'].strip()
            login_password = request.POST['password']
            user = authenticate(username = login_name, password = login_password)
            if user is not None:
                if user.is_active:
                    auth.login(request, user)
                    messages.add_message(request, messages.SUCCESS, '成功登入')
                    return redirect('/')
                else:
                    messages.add_message(request, messages.WARNING, '帳號尚未啟用')
            else:
                messages.add_message(request, messages.WARNING, '登入失敗')
        else:
            messages.add_message(request, messages.INFO, '請檢查內容')
    else:
        login_form = forms.LoginForm()

    return render(request,'login.html',locals())

def sign_up(request):
    if 'username' in request.session:
        username = request.session['username']
        
    form = forms.ContactForm(request.POST)
    if form.is_valid():
        message = '感謝來信'
        user_name = form.cleaned_data['user_name']
        user_item = form.cleaned_data['user_item']
        user_group = form.cleaned_data['user_group']
    else:
        message = '請檢查'

    return render(request,'sign_up.html',locals())

def index(request, pid = None, del_pass = None):
    if request.user.is_authenticated:
        username = request.user.username
    messages.get_messages(request)
    return render(request, 'index.html', locals())

def logout(request):
    auth.logout(request)
    messages.add_message(request, messages.INFO,'成功登出')
    return redirect('/')

def ppdf(request):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="somefilename.pdf"'
    p = canvas.Canvas(response)
    p.drawString(100, 100,'1')
    p.showPage()
    p.save()
    return response

@login_required(login_url = '/login/')
def userinfo(request):
    if request.user.is_authenticated:
        username = request.user.username
    try:
        userinfo = User.objects.get(username = username)
    except:
        pass
    return render (request, "userinfo.html", locals())
    