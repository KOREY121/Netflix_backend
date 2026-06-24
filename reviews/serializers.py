from rest_framework import serializers
from .models import Review, MyList, Recomendation

class ReviewSerializer(serializers.ModelSerializer):
    profile_name = serializers.CharField(source='profile.name', read_only= True)
    content_title = serializers.CharField(source = 'content.title', read_only=True)

    class Meta:
        model = Review
        fields = ['id', 'profile','profile_name','content', 'content_title', 'rating', 'review_text', 'created_at']
        read_only_fields = ['id', 'created_at']

    
class MyListSerializer(serializers.ModelSerializer):
    content_title = serializers.CharField(source= 'content.title', read_only =True)
    content_type = serializers.CharField(source= 'content.type', read_only = True)
    thumbnail_url = serializers.URLField(source = 'content.thumbnail_url', read_only= True)


    class Meta:
        model = MyList
        fields= ['id', 'profile', 'content', 'content_title','content_type', 'thumbnail_url', 'added_at']
        read_only_fields = ['id', 'added_at']
        

class RecomendationSerializer(serializers.ModelSerializer):
    content_title = serializers.CharField(source='content.title', read_only= True)
    thumbnail_url =serializers.URLField(source= 'content.thumbnail_url', read_only= True)

    class Meta:
        models = Recomendation
        fields = ['id', 'content', 'content_title', 'thumbnail_url', 'score', 'generated_at']