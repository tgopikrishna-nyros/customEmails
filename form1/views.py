# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Trashmail, Nform

# Create your views here.
def index(request):
	form1 = Nform.objects.all()[:20]
	context = {
		'form1':form1
	}
	# return HttpResponse("Hello")
	return render(request, 'index.html', context)


def details(request, id):
	smail = Nform.objects.get(id=id)
	context = {
		'smail':smail
	}
	return render(request, 'details.html', context)
	
def compose(request):
	if(request.method == 'POST'):
		to = request.POST['to']
		subject = request.POST['subject']
		body = request.POST['body']
		
		smail = Nform(to=to, subject=subject, body=body)
		smail.save()
		
		return redirect('/form1')
	else:
		return render(request, 'compose.html')
		
def sent(request):
	form1 = Nform.objects.all()[:20]
	context = {
		'form1':form1
	}
	# return HttpResponse("Hello")
	return render(request, 'sent.html', context)

def trash(request):
	form1 = Trashmail.objects.all()[:20]
	context = {
		'form1':form1
	}
	# return HttpResponse("Hello")
	return render(request, 'trash.html', context)
	
def trashdetails(request, id):
	tmail = Trashmail.objects.get(id=id)
	context = {
		'tmail':tmail
	}
	return render(request, 'trashdetails.html', context)

def deletemail(request, id):
	smail = Nform.objects.get(id=id)
	context = {
		'smail':smail
	}
	return render(request, 'deletemail.html', context)

def deleted_insert(request):
	if(request.method == 'POST'):
		remove_id = request.POST['id']
		mail = request.POST['mail']
		subject = request.POST['subject']
		body = request.POST['body']
		
		smail = Trashmail(remove_id=remove_id, mail=mail, subject=subject, body=body)
		smail.save()
		
		Nform.objects.filter(id=remove_id).delete()
	
		return redirect('/form1')
		
	else:
		return render(request, 'compose.html')

