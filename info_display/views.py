from django.shortcuts import HttpResponse, render
from info_display.models import PartkeeprInstance
import requests
import json


def main_screen(request):
    return render(request, 'info_display/main_screen.html', {})

def search_json(request):
    """Returns partkeepr search results as json."""
    search_term = request.GET.get('q', '').strip()
    pkeepr = PartkeeprInstance.objects.first()
    if not pkeepr:
        raise Exception('No partkeepr instance configured')
    if not search_term:
        return HttpResponse(json.dumps([]), content_type='application/json')

    url = pkeepr.api_url + '/parts?page=1&start=0&itemsPerPage=50&group=%7B%22property%22%3A%22categoryPath%22%2C%22direction%22%3A%22ASC%22%7D&order=%5B%7B%22property%22%3A%22category.categoryPath%22%2C%22direction%22%3A%22ASC%22%7D%2C%7B%22property%22%3A%22name%22%2C%22direction%22%3A%22ASC%22%7D%5D&filter=%5B%7B%22property%22%3A%22name%22%2C%22value%22%3A%22%25' + search_term + '%25%22%2C%22operator%22%3A%22like%22%7D%5D'
    basic_auth = requests.auth.HTTPBasicAuth(pkeepr.user, pkeepr.password)
    results = requests.get(url, auth=basic_auth)
    results = json.loads(results.text)['hydra:member']
    results = json.dumps(results)
    return HttpResponse(results, content_type='application/json')

def proxy_image(request, img_id):
    """Returns partkeepr images."""
    pkeepr = PartkeeprInstance.objects.first()
    if not pkeepr:
        raise Exception('No partkeepr instance configured')

    url = pkeepr.api_url + '/part_attachments/' + img_id + '/getFile'
    basic_auth = requests.auth.HTTPBasicAuth(pkeepr.user, pkeepr.password)
    img = requests.get(url, auth=basic_auth)
    return HttpResponse(img, content_type='image/jpeg')

