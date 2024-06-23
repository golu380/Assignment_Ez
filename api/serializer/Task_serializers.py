from rest_framework import serializers
# from User_auth.models import *
from django.contrib.auth.models import User
from User_auth.models import Document


# myapp/serializers.py



class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = '__all__'
        read_only_fields = ('uploaded_at', 'uploaded_by')

    def validate_file(self, value):
        allowed_types = ['application/pdf', 'application/vnd.ms-excel', 'application/msword', 'application/vnd.openxmlformats-officedocument.wordprocessingml.document']
        if value.content_type not in allowed_types:
            raise serializers.ValidationError("Unsupported file type.")
        return value
