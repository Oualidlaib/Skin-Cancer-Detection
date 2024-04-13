from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from django.contrib.auth import login, authenticate
from .forms import RegistrationForm


@csrf_exempt
@api_view(['POST'])
def signup(request):
    form = RegistrationForm(request.POST)
    if form.is_valid():
        form.save()
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password1")
        account = authenticate(email=email, password=password)
        login(request, account)
        return JsonResponse({"Success": "Account created successfully go and login"})

    return JsonResponse({"error": "Enter valid informations"})
