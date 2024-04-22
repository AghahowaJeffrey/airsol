from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework import status


# Create your views here.
@api_view(['GET', 'POST'])
def index(request):
    """
    Returns the home page and sends address to the backend.
    """
    if request.method == 'POST':
        return None
    
    else: 
        return render(request, 'index.html')