from django.apps import apps
from django.shortcuts import redirect

def index(request):
	return redirect('compare:compare_list')