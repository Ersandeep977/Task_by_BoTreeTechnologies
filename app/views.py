
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from app.models import Category, Codeeditor
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect

from app.forms import SignUpForm, CodeForm

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'MyApp/signup.html', {'form': form})
@login_required
def home(request):
    return render(request, 'MyApp/show_data.html')
from django.contrib import messages
def search(request):
    if request.method=='POST':
        srch=request.POST['search']

        if srch:
            match=Category.objects.filter(Q(name__istartswith=srch))
            if match:
                return render(request,'search.html',{'sr':match})
            else:
                messages.error(request, 'no result found')
        else:
            return HttpResponseRedirect('/search/')
    return render(request,'search.html')

def add(request):
    form = CodeForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect('show_add_form')
    else:
        context = {"form": form}
        return render(request, 'MyApp/home.html', context)

def show_add_form(request):
    if request.method == 'GET':
        data = Codeeditor.objects.all()

        # for mydata in data:
        ctx = {'data': data}
        return render(request, 'MyApp/show_data.html', ctx)