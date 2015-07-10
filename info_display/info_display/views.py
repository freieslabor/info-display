from django.shortcuts import render


def info_screen(request):
    return render(request, 'info_display/info_screen.html', {})
