from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import generics
from rest_framework import status
from django.db.models import Avg
from .models import Movie, Review,Director
from .serializers import DirectorSerializer, MovieSerializer, ReviewSerializer

class DirectorListView(generics.ListAPIView):
    queryset = Director.objects.all()
    serializer_class = DirectorSerializer

class DirectorDetailView(generics.RetrieveAPIView):
    queryset = Director.objects.all()
    serializer_class = DirectorSerializer

class MovieListView(generics.ListAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

class MovieDetailView(generics.RetrieveAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

class ReviewListView(generics.ListAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

class ReviewDetailView(generics.RetrieveAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer



@api_view(['GET'])
def movie_reviews(request):
    movies = Movie.objects.all()
    serializer = MovieSerializer(movies, many=True)

    # Рассчитываем средний балл для каждого фильма
    for movie_data in serializer.data:
        reviews = movie_data['reviews']
        if reviews:
            avg_rating = sum(review['stars'] for review in reviews) / len(reviews)
            movie_data['rating'] = round(avg_rating, 2)
        else:
            movie_data['rating'] = None

    return Response(serializer.data)