from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers
from .models import NoteToken, CustomUser

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['email'] = user.email
        return token


class NoteTokenSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = NoteToken
        fields = ["id", "description", "owner"]

    
class CustomUserRegistrationSerializer(serializers.ModelSerializer):
    
    class Meta:   
        model=CustomUser
        fields = ['email', 'full_name', 'phone', 'gender', 'country', 'birthday', "username", 'password']

    def create(self, validated_data):
        user = CustomUser(
            email = validated_data['email'],
            full_name = validated_data['full_name'],     
            phone = validated_data['phone'], 
            gender = validated_data['gender'], 
            country = validated_data['country'], 
            birthday = validated_data['birthday'], 
            username = validated_data['username'], 
        )

        user.set_password(validated_data['password'])
        user.save()
        return user