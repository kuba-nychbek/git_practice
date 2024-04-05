from rest_framework import serializers
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    authorization_status = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ['id', 'username', 'authorization_status']

    def get_authorization_status(self, obj):
        if obj.is_superuser:
            return 'admin'
        else:
            return 'user'
