from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    html = """
    <!DOCTYPE html>
    <html>
        <head>
        </head>
        <body>
            <a href="https://tvc.mx/" style="text-decoration: none;">
                <button>Visitar TVC.mx</button>
            </a>
        </body>
    </html>
    """
    return HttpResponse(html)