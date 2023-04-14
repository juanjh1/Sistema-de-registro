from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.


def index(request):

    context = {

        'user': request.user
     
    }
    
    return render(request, "index.html", context)

@login_required
def view_clinte (request):return  render(request,"clienteview.html")

@login_required
def profile (request): return render( request, 'profile.html')