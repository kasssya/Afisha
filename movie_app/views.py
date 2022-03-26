from rest_framework.decorators import api_view
from rest_framework.response import Response
from movie_app.serializers import DirectorSerializers, MovieSerializers, ReviewSerializers
from movie_app.models import Director, Movie, Review
from rest_framework import status


@api_view(['GET'])
def directors_list_view(request):
    directors = Director.objects.all()
    serializer = DirectorSerializers(directors, many=True)
    return Response(data=serializer.data)

@api_view(['GET'])
def director_item_view(request, id):
    try:
        director = Director.objects.get(id=id)
    except Director.DoesNotExist:
        return Response(data={'error': 'Director not Found!!!'},
                        status=status.HTTP_404_NOT_FOUND)
    serializer = DirectorSerializers(director)
    return Response(data=serializer.data)

@api_view(['GET'])
def movies_list_view(request):
    movies = Movie.objects.all()
    serializer = MovieSerializers(movies, many=True)
    return Response(data=serializer.data)

@api_view(['GET'])
def movie_item_view(request, id):
    try:
        movie = Movie.objects.get(id=id)
    except Movie.DoesNotExist:
        return Response(data={'error':'Movie not Found!!!'},
                        status=status.HTTP_404_NOT_FOUND)

    serializer = MovieSerializers(movie)
    return Response(data=serializer.data)

@api_view(['GET'])
def reviews_list_view(request):
    reviews = Review.objects.all()
    serializer = ReviewSerializers(reviews, many=True)
    return Response(data=serializer.data)

@api_view(['GET'])
def review_item_view(request, id):
    try:
        review = Review.objects.get(id=id)
    except Movie.DoesNotExist:
        return Response(data={'error':'Review not Found!!!'},
                        status=status.HTTP_404_NOT_FOUND)
    serializer = ReviewSerializers(review)
    return Response(data=serializer.data)


@api_view(['GET'])
def movies_reviews_view(request):
    movie_reviews = Movie.objects.all()
    data = MovieSerializers(movie_reviews, many=True).data
    return Response(data=data)