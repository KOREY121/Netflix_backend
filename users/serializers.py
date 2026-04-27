from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers


User = get_user_model()


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, label='Confirm Password')

    class Meta:
        model = User
        fields = ['id', 'email', 'name', 'password', 'password2']

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({'password': 'Passwords do not match'})
        return attrs
    
    def create (self, validated_data):
        validated_data.pop('password2')
        return User.objects.create_user(**validated_data)
    

class UserSerializer(serializers.ModelSerializer):
    subscription_plan = serializers.CharField(
        source = 'subscription.plan_name', read_only=True
    )

    class Meta:
        model = User
        field = ['id', 'email', 'name', 'subscription_plan', 'created_at']
        read_only_fields = ['id', 'email', 'created_at']


class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(write_only= True)
    new_password = serializers.CharField(write_only= True, validators=[validate_password])

    def validate_old_password(self, value):
        if not self.context['request'].user.check_password(value):
            raise serializers.ValidationError('Old password is Incorrect')
        return value
    
    def save(self, **kwargs):
        user = self.context['request'].user
        user.set_password(self.validated_data['new_password'])
        user.save()
