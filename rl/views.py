from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from .models import *
from .forms import *
from django.contrib import messages

def sky(request):
    #Loc.objects.all().delete()
    if request.session['logged']=='false':
        messages.error(request,'Log in required')
        return HttpResponseRedirect('/signup_contrib')


    if request.method == 'POST':
        form = AddStartup(request.POST)
        if form.is_valid():
            db_obj=Loc()
            print("yaha")
            name=request.POST.get('name')
            lon=request.POST.get('flon')
            lat=request.POST.get('flat')
            dat=request.POST.get('date')
            link=request.POST.get('link')
            db_obj.name=name
            db_obj.date=dat
            db_obj.lat=lat
            db_obj.lon=lon
            db_obj.link=link
            db_obj.status='false'
            db_obj.save()
            print name,lon,link,dat
            form = AddStartup()
            star = Loc.objects.filter(status='true')
            return HttpResponseRedirect('/sky')
            #return render(request, 'sky.html', {'form': form, 'stp': star})

    else:
        form = AddStartup()
        forum=TimeForm()
        star = Loc.objects.filter(status='true')
        return render(request, 'sky.html', {'form': form, 'stp': star,'for':forum})






def serch(request, template_name='sky.html'):

    if request.method=='POST':
        print("yaha")
        featured_filter = request.POST.get('dat')
        listings = Loc.objects.filter(date=featured_filter,status='true')
        if not listings:
            return HttpResponseRedirect('/sky')

        form = AddStartup()
        fr = TimeForm()
        context_dict = {'stp': listings, 'form': form, 'for': fr}
        return render(request, template_name, context_dict)
    else:
        return HttpResponseRedirect('/sky')

def unlog_serch(request, template_name='new_sky.html'):

    if request.method=='POST':
        print("yaha")
        featured_filter = request.POST.get('dat')
        listings = Loc.objects.filter(date=featured_filter,status='true')
        if not listings:
            return HttpResponseRedirect('/unlog_serch')

        fr = TimeForm()
        context_dict = {'stp': listings,  'for': fr}
        return render(request, template_name, context_dict)

    listings = Loc.objects.filter(status='true')
    fr = TimeForm()
    context_dict = {'stp': listings, 'for': fr}
    return render(request, template_name,context_dict)



def signup_contrib(request):
    if request.method=='POST':
        form=JoinForm(request.POST)
        if form.is_valid():
            db_obj=adder()
            db_obj.fname=request.POST.get('fname')
            db_obj.sname=request.POST.get('sname')
            ps1=request.POST.get('password')
            ps2=request.POST.get('cpswd')
            listings = adder.objects.filter(email=request.POST.get('mail'))
            if ps1!=ps2 or listings :
                messages.error(request,'Password mismatch or mail already in use')
                return render(request,'Join.html')
            else:
                db_obj.email=request.POST.get('mail')
                db_obj.pswd=ps1
                db_obj.save()
                messages.success(request, 'Successful signup..Please login')
                return HttpResponseRedirect('/signup_contrib')
    request.session['logged'] = 'false'
    return render(request,'Join.html')



def login_contrib(request):
    if request.method=='POST':
        form=JoinLog(request.POST)
        if form.is_valid():
            mai=request.POST.get('mail')
            psw=request.POST.get('pswd')
            listings = adder.objects.filter(email=mai,pswd=psw)
            if not listings:
                messages.error(request, 'Invalid Credential')
                request.session['logged'] = 'false'
                return HttpResponseRedirect('/signup_contrib')
            else:
                request.session['logged'] = 'true'
                return HttpResponseRedirect('/sky')

        else:
            messages.error(request, 'Invalid Form')
            request.session['logged'] = 'false'
            return  HttpResponseRedirect('/signup_contrib')







def leave(request):
    request.session['logged'] = 'false'
    return HttpResponseRedirect('/unlog_serch')

from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth import logout

def logt(request):
    logout(request)
    return HttpResponseRedirect('/unlog_serch')


@user_passes_test(lambda u: u.is_superuser)
def adm(request,):
    stp=Loc.objects.filter(status='false')
    return render(request,'admin.html',{'stp':stp})

def rem(request,prodname):
    Loc.objects.filter(name=prodname).delete()
    return HttpResponseRedirect('/adm')

def verif(request,prodname):
    t = Loc.objects.get(name=prodname)
    t.status = 'true'  # change field
    t.save()
    return HttpResponseRedirect('/adm')
