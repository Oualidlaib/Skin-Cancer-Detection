from django.shortcuts import render, redirect
from django.http import HttpResponseBadRequest, JsonResponse
from django.views import View
from .models import SkinImage
import json
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User


@csrf_exempt
def testSkinCancer(request):
    if not request.FILES:
        return HttpResponseBadRequest(json.dumps({'error': 'No image uploaded'}))

    # Access the uploaded image directly
    uploaded_image = request.FILES['image']
    username = request.POST['username']
    user = User.objects.get(username=username)
    # Save the image to the database
    image_model = SkinImage.objects.create(user=user, image=uploaded_image)

    # You can perform additional processing here (e.g., resize, convert format)

    # Optionally, return a response to the client
    response_data = {'message': 'Image uploaded successfully'}
    return JsonResponse(response_data)
