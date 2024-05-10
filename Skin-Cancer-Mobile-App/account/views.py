from .serializers import PasswordResetRequestSerializer
from rest_framework.status import HTTP_202_ACCEPTED
from rest_framework.response import Response
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from skin_cancer_app.models import Account
from django.shortcuts import render
from django.http import JsonResponse
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework_simplejwt.authentication import JWTAuthentication
from .forms import RegistrationForm
from rest_framework.permissions import IsAuthenticated
from django.core.exceptions import ValidationError
from django.db import IntegrityError
from django.core.mail import send_mail
from django.core.validators import validate_email


@csrf_exempt
@api_view(['POST'])
def signup(request):

    form = RegistrationForm(request.POST)

    if form.is_valid():
        form.save()
        return JsonResponse({"Success": "Account created successfully go and login"})
    return JsonResponse({"error": "Enter valid informations"})


@csrf_exempt
@api_view(['POST'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def change_email(request):
    user = request.user
    try:
        validate_email(request.POST['email'])
        user.email = request.POST['email']
        user.save()
        return JsonResponse({'Success': 'Email updated successfully'})
    except ValidationError as e:
        return JsonResponse({"Bad email, details:": e.message})
    except IntegrityError:
        return JsonResponse({"Error": "This email is in use"})


@csrf_exempt
@api_view(['POST'])
def reset_password(request):
    serializer = PasswordResetRequestSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    email = serializer.validated_data['email']
    user = Account.objects.filter(email=email).first()
    if user:
        token_generator = PasswordResetTokenGenerator()
        password_reset_token = token_generator.make_token(user)
        uidb64 = urlsafe_base64_encode(force_bytes(user.pk))
        subject = 'Password Reset Request'
        reset_password_url = f'http://127.0.0.1:8000/account/password-reset-confirm/{uidb64}/{password_reset_token}/'
        message = f'You requested a password reset for your account. Please click the link below to set a new password:\n{reset_password_url}'
        html_message = render(request, 'reset_password.html', {
            'username': user.username,
            'reset_link': reset_password_url,
        }).content.decode()
        send_mail(subject, '', 'laiboualid2003@gmail.com', [
                  user.email], html_message=html_message)
        return Response({'status': 'Success', 'message': 'Password reset link sent.'}, status=HTTP_202_ACCEPTED)

    return Response({'status': 'Error', 'message': 'Email not found.'})


@csrf_exempt
@api_view(['POST'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def change_username(request):
    user = request.user
    try:
        user.username = request.POST['username']
        user.save()
        return JsonResponse({'success': 'username updated successfully'})
    except ValidationError as e:
        return JsonResponse({"bad username, details:": e})
