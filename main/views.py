from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse, HttpResponseNotFound, JsonResponse
from django.core import serializers
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from main.forms import RelicForm
from django.urls import reverse
from main.models import Relic
import datetime
import json


# Create your views here.
@login_required(login_url='/login')
def show_main(request):
    relics = Relic.objects.filter(user=request.user)

    context = {
        'name': request.user.username,
        'class': 'PBP B',
        'relics' : relics,
        'last_login' : request.COOKIES['last_login']
    }

    return render(request, "main.html", context)

@csrf_exempt
def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)

@csrf_exempt
def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            response = HttpResponseRedirect(reverse("main:show_main")) 
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
        else:
            messages.info(request, 'Sorry, incorrect username or password. Please try again.')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return redirect('main:login')

def create_relic(request):
    form = RelicForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        product = form.save(commit=False)
        product.user = request.user
        product.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "create_relic.html", context)

def edit_Relic(request, id):
    relic = Relic.objects.get(pk = id)
    form = RelicForm(request.POST or None, instance=relic)

    if form.is_valid() and request.method == "POST":
        form.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "edit_relic.html", context)

def delete_relic(request, id):
    relic = Relic.objects.get(pk = id)
    relic.delete()
    return HttpResponseRedirect(reverse('main:show_main'))

def delete_relic_ajax(request, name):
    relic = get_object_or_404(Relic, name=name)
    relic.delete()
    return HttpResponseRedirect(reverse('main:show_main'))

def get_relic_json(request):
    relic_item = Relic.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize('json', relic_item))

@csrf_exempt
def add_relic_ajax(request):
    if request.method == 'POST':
        name = request.POST.get("name")
        amount = request.POST.get("amount")
        description = request.POST.get("description")
        best_rarity = request.POST.get("best_rarity")
        ideal_main_stat = request.POST.get("ideal_main_stat")
        ideal_variant_amount = request.POST.get("ideal_variant_amount")
        user = request.user

        new_relic = Relic(name=name, amount=amount, description=description, best_rarity=best_rarity, ideal_main_stat=ideal_main_stat, ideal_variant_amount=ideal_variant_amount, user=user)
        new_relic.save()

        return HttpResponse(b"CREATED", status=201)

    return HttpResponseNotFound()

def show_xml(request):
    data = Relic.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = Relic.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_json_by_id(request, id):
    data = Relic.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = Relic.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

@csrf_exempt
def create_product_flutter(request):
    if request.method == 'POST':
        
        data = json.loads(request.body)

        new_product = Relic.objects.create(
            user = request.user,
            name = data["name"],
            price = int(data["price"]),
            description = data["description"]
        )

        new_product.save()

        return JsonResponse({"status": "success"}, status=200)
    else:
        return JsonResponse({"status": "error"}, status=401)