from django.shortcuts import render

def alunos(request):
	return render(request, '../alunos/templates')