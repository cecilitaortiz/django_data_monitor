from django.shortcuts import render
import requests
from django.conf import settings
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
def home(request):
    response = requests.get(settings.API_URL)  # URL de la API
    posts = response.json()  # Convertir la respuesta a JSON

    # Número total de respuestas
    total_responses = len(posts)
    
    # Contar votos por producto
    product1_votes = 0
    product2_votes = 0
    
    for post in posts:
        if post.get('productID') == 'product1':
            product1_votes += 1
        elif post.get('productID') == 'product2':
            product2_votes += 1
    
    # Determinar el ganador actual
    if product1_votes > product2_votes:
        current_winner = "Product 1"
    elif product2_votes > product1_votes:
        current_winner = "Product 2"
    else:
        current_winner = "Empate"
    
    data = {
        'title': "Landing Page Dashboard :3",
        'debug': 'Template renderizado correctamente',
        'total_responses': total_responses,
        'product1_votes': product1_votes,
        'product2_votes': product2_votes,
        'current_winner': current_winner,

    }
    return render(request, 'dashboard/index.html', data)
