from django.shortcuts import render


def main_screen(request):
    return render(request, 'info_display/main_screen.html', {})
