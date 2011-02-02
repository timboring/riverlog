from django.http import Http404
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response

from riverlog import forms
from riverlog import upload_runs
from riverlog import models


def home(request):
	return render_to_response('index.html')


def rivers(request):
	runs = models.Run.objects.order_by('-date')
	return render_to_response('rivers.html', {'rivers': runs})


def river(request, run_id):
	run = models.Run.objects.get(id=run_id)
	return render_to_response('river.html', {'river': run})


def add(request):
	if request.method == 'POST':
		form = forms.AddRunForm(request.POST)
		if form.is_valid():
			data = form.cleaned_data
			object = models.Run(date=data.get('date'),
													put_on_time=data.get('put_on_time', None),
													take_out_time=data.get('take_out_time', None),
													river=data.get('river'),
													section=data.get('section', None),
													usgs_level=data.get('usgs_level', None),
													bridge_gauge=data.get('bridge_gauge', None),
													notes=data.get('notes', None))

			object.save()
		else:
			errors = form.errors
			data = form.data
			return render_to_response('add.html', {'form': form, 'errors': errors})
		return HttpResponseRedirect('/river/')
	elif request.method == 'GET':
		form = forms.AddRunForm()
		return render_to_response('add.html', {'form': form,})
	else:
		raise Http404


def delete(request):
	raise Http404


def importruns(request):
	if request.method == 'POST':
		form = forms.UploadFileForm(request.POST, request.FILES)
		if form.is_valid():
			results = upload_runs.process_file(request.FILES['filename'])
			return render_to_response('results.html', {'results': results})
	elif request.method == 'GET':
		return render_to_response('import.html')
	else:
		return Http404


def search(request):
	pass
