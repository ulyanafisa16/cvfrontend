from django.shortcuts import render
import requests
import json
from django.http import JsonResponse

# def home(request):
#     return render(request, 'portfolio/index.html')
BASE_API_URL = "http://127.0.0.1:8001/api"

def service_detail(request):
    return render(request, 'portfolio/service-details.html')

def portfolio_list(request):
    try:
        # Ambil data dari API
        portfolios = requests.get(f"{BASE_API_URL}/portfolios/").json()
        profile = requests.get(f"{BASE_API_URL}/profile/").json()
        skills = requests.get(f"{BASE_API_URL}/skills/").json()

        categories = sorted(list({p["category"] for p in portfolios if p.get("category")}))
    except requests.exceptions.RequestException:
        portfolios = []
        profile = {}
        skills = []

    context = {
        "profile": profile,
        "skills": skills,
        "portfolios": portfolios,
        "categories": categories
    }
    return render(request, "portfolio/index.html", context)

def portfolio_detail(request, id):
    try:
        response = requests.get(f'http://127.0.0.1:8001/api/portfolios/{id}/')
        portfolio = response.json() if response.status_code == 200 else {}
    except requests.exceptions.RequestException:
        portfolio = {}
    
    return render(request, 'portfolio/portfolio-details.html', {'portfolio': portfolio})