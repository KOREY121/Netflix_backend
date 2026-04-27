from rest_framework import serializers
from .models import Profile

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['id', 'name', 'avatar_url', 'maturity_level', 'is_default', 'created_at']
        read_only_fields = ['id', 'created_at']

        def validate(self, attrs):
            user = self.context['requests'].user
            if not self.instance:
                if Profile.objects.filter(user=user).count() >= 4:
                    raise serializers.ValidationError('Maximum of 4 profiles allowed.')
                return attrs
            

        def create(self, validated_data):
            user = self.context['request'].user
            if not Profile.objects.filter(user=user).exists():
                validated_data['is_default'] = True
                return Profile.objects.create(user=user, **validated_data)