from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Review, MyList, Recommendation
from .serializers import ReviewSerializer, MyListSerializer, RecommendationSerializer


class ReviewListCreateView(generics.ListCreateAPIView):
    serializer_class   = ReviewSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        content_id = self.request.query_params.get('content')
        qs = Review.objects.filter(profile__user=self.request.user)
        if content_id:
            qs = qs.filter(content_id=content_id)
        return qs


class ReviewDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class   = ReviewSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Review.objects.filter(profile__user=self.request.user)


class MyListView(generics.ListAPIView):
    serializer_class   = MyListSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        profile_id = self.request.query_params.get('profile')
        qs = MyList.objects.filter(profile__user=self.request.user)
        if profile_id:
            qs = qs.filter(profile_id=profile_id)
        return qs


class ToggleMyListView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        profile_id = request.data.get('profile')
        content_id = request.data.get('content')

        obj, created = MyList.objects.get_or_create(
            profile_id=profile_id, content_id=content_id
        )
        if not created:
            obj.delete()
            return Response({'in_list': False, 'detail': 'Removed from My List.'})

        return Response({'in_list': True, 'detail': 'Added to My List.'}, status=201)


class RecommendationListView(generics.ListAPIView):
    serializer_class   = RecommendationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        profile_id = self.request.query_params.get('profile')
        qs = Recommendation.objects.filter(profile__user=self.request.user)
        if profile_id:
            qs = qs.filter(profile_id=profile_id)
        return qs.order_by('-score')[:20]