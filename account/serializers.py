from skin_cancer_app.models import Account
from rest_framework import serializers


class PasswordResetRequestSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)

    def validate_email(self, value):
        user = Account.objects.filter(email=value).exists()
        if not user:
            raise serializers.ValidationError('Email not found.')
        return value
