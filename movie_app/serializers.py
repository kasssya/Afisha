from rest_framework import serializers
from movie_app.models import Director, Movie, Review
from rest_framework.exceptions import ValidationError


class DirectorSerializers(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = 'id name count_movies'.split()


class ReviewSerializers(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = 'text stars movie'.split()

class MovieSerializers(serializers.ModelSerializer):
    director = DirectorSerializers()
    reviews = ReviewSerializers(many=True)
    class Meta:
        model = Movie
        fields = 'id title description duration director reviews rating'.split()




class DirectorCountSerializer(serializers.ModelSerializer):
    movie_count = serializers.SerializerMethodField()

    class Meta:
        model = Director
        fields = 'movie_count'.split()

    def get_movie_count(self, movie):
        return movie.all().count()



class DirectorValidateSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=30, min_length=5)

    def velidate_director_id(self, director_id):
        if Director.objects.filter(id=director_id).count() == 0:
            raise ValidationError(f'Director with id={director_id} not found!')
        return director_id

class MovieValidateSerializer(serializers.Serializer):
    title = serializers.CharField()
    description = serializers.CharField()
    duration = serializers.IntegerField()
    director = serializers.IntegerField()

    def validate_movie_id(self, movie_id):
        if Movie.objects.filter(id=movie_id).count() == 0:
            raise ValidationError(f'Movie with id={movie_id} not found!')
        return movie_id


class ReviewValidateCreateUpdateSerializer(serializers.Serializer):
    text = serializers.CharField()
    movie = serializers.IntegerField()
    stars = serializers.IntegerField()

    def validate_reviews_id(self, reviews_id):
        if Review.objects.filter(id=reviews_id).count() == 0:
            raise ValidationError(f'Reviews with id={reviews_id} not found!')
        return

