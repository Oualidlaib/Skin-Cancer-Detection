from django.http import HttpResponseBadRequest, JsonResponse
from .models import SkinImage, Account
import json
from django.views.decorators.csrf import csrf_exempt
import numpy as np
import os
import tensorflow as tf
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.conf import settings


@csrf_exempt
@api_view(['POST'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def testSkinCancer(request):
    if request.method != 'POST':
        return HttpResponseBadRequest(json.dumps({'error': 'Only POST requests are allowed'}))

    if 'image' not in request.FILES or 'username' not in request.POST:
        return HttpResponseBadRequest(json.dumps({'error': 'Image and username required'}))

    uploaded_image = request.FILES['image']
    username = request.POST['username']

    try:
        user = Account.objects.get(username=username)
    except Account.DoesNotExist:
        return HttpResponseBadRequest(json.dumps({'error': 'User not found'}))

    image_model = SkinImage.objects.create(user=user, image=uploaded_image)

    model_path = os.path.join(settings.BASE_DIR, 'media', 'skin-cancer-predictor.keras')
    model = tf.keras.models.load_model(model_path, safe_mode=False)

    image_path = image_model.image.path
    img = tf.keras.utils.load_img(image_path, target_size=(224, 224))  
    img_array = tf.keras.utils.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    preprocessed_img = tf.keras.applications.resnet50.preprocess_input(img_array)

    predictions = model.predict(preprocessed_img)
    predicted_value = predictions[0][0]  
    result = "Malignant" if predicted_value > 0.5 else "Benign"

    response_data = {
        "username": username,
        "classification": result,
        "prediction_score": float(predicted_value)
    }

    return JsonResponse(response_data)


@csrf_exempt
@api_view(['GET'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def history(request):
    results = SkinImage.objects.filter(user=request.user)
    data = list(results.values())
    return JsonResponse(data, safe=False)


@csrf_exempt
@api_view(['GET'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def user_informations(request):
    result = Account.objects.filter(pk=request.user.pk).first()
    data = {
        'username': result.username,
        'email': result.email,
        'date_joined': result.date_joined,
        'last_login': result.last_login,
    }
    return JsonResponse(data, safe=False)
