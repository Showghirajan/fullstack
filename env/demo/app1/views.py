# app1/views.py

from django.shortcuts import render
import requests
from requests.exceptions import RequestException

def index(request):
    drug_name = request.GET.get('search', '')
    uses = None
    
    if drug_name:
        url = f'https://actual-api-domain.com/drugs/{drug_name}/uses'
        
        try:
            response = requests.get(url)
            response.raise_for_status()  # Raise HTTPError for bad responses
            
            if response.status_code == 200:
                try:
                    data = response.json()  # Attempt to parse response as JSON
                    uses = data.get('uses', 'No information available.')
                    print(f"Uses fetched from API: {uses}")  # Debug print statement
                except ValueError:
                    uses = f"Non-JSON response received from API for {drug_name}."
                    print(f"Non-JSON response received from API for {drug_name}. Response content: {response.text}")  # Debug print statement
        
        except RequestException as e:
            print(f"Error fetching data from API: {e}")
            uses = f"Error fetching data for {drug_name}. Please try again later."
    
    context = {
        'drug_name': drug_name,
        'uses': uses,
    }
    
    return render(request, 'index.html', context)

   


