from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from rest_framework.validators import UniqueValidator
from .models import Task


class RegisterSerializer(serializers.ModelSerializer):
    #validators used to ensure that the email provided during registration is unique
    email = serializers.EmailField(required=True, 
    validators=[UniqueValidator(queryset=User.objects.all())] )
    password = serializers.CharField(write_only=True, required=True,validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('username','email','password','password2')
        
    #check the passwords are same
    def validate(self, data):
        if data['password'] != data['password2']:
            raise serializers.ValidationError({"password": "Passwords do not match."})
        return data
    
    def create(self, validated_data):
        user = User.objects.create(
            username= validated_data['username'],
            email= validated_data['email'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id','title','description','status','created_at','updated_at']
        read_only_fields = ['id','created_at','updated_at']
    
    def validate_title(self, value):
        if not value:
            raise serializers.ValidationError("Title cannot be empty")
        return value

