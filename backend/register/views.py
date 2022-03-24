from django.shortcuts import redirect, render
from .forms import RegisterForm
from register.serializers import RegisterSerializer 
from rest_framework import viewsets
from rest_framework.response import Response 
from rest_framework.views import APIView     
from register.models import Register   


# Create your views here.
def register(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            form.save()
        return redirect("/")
    else:     
        form = RegisterForm()
    return render(response, "register/register.html", {'form': form})

class RegisterView(viewsets.ModelViewSet):  
    serializer_class = RegisterSerializer 
    queryset = Register.objects.all()


