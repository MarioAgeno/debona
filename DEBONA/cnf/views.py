#-- Vistas Comunes o Generales del Proyecto

from django.shortcuts import render

from datetime import date

# =====================================================================================================================
def inicio(request):
	return render(request, 'inicio.html', {'fecha': date.today()})

