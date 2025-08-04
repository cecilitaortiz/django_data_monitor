from django.shortcuts import render

# Create your views here.
def home(request):
    """
    Vista principal del dashboard que renderiza base.html
    """
    context = {
        'title': 'Dashboard Principal',
        'debug': 'Template renderizado correctamente'
    }
    return render(request, 'dashboard/base.html', context)
