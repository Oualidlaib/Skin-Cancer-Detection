from django.http import HttpResponseBadRequest, JsonResponse
from .models import SkinImage, Account
import json
from django.views.decorators.csrf import csrf_exempt
import numpy as np
import os
import tensorflow as tf
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework_simplejwt.authentication import JWTAuthentication


@csrf_exempt
@api_view(['POST'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def testSkinCancer(request):

    # model = tf.keras.models.load_model(
    #     os.getcwd()+r'\media\skin_cancer_model2.keras', safe_mode=False)

    # if not request.FILES:
    #     return HttpResponseBadRequest(json.dumps({'error': 'No image uploaded'}))

    uploaded_image = request.FILES['image']
    username = request.POST['username']
    user = Account.objects.get(username=username)

    image_model = SkinImage.objects.create(user=user, image=uploaded_image)
    return JsonResponse(request.user.username, safe=False)
    # img_path = r'images\{0}'.format(uploaded_image)

    # img = tf.keras.image.load_img(
    #     r'media\{0}'.format(img_path), target_size=(160, 160))

    # img_array = tf.keras.image.img_to_array(img)
    # img_array_expanded_dims = np.expand_dims(img_array, axis=0)
    # preprocessed_image = tf.keras.applications.mobilenet.preprocess_input(
    #     img_array_expanded_dims
    # )
    # predictions = model.predict(preprocessed_image)
    # predictions = predictions.tolist()
    # pre = predictions[0][0]-0.1

    # result = ""
    # if pre > 0.5:
    #     result = "Malignant"
    # else:
    #     result = "Benign"
    # response_data = {"Classification Result": "result",
    #                  'Prediction': "None"}
    # return JsonResponse(response_data)


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
