from rest_framework import serializers
from movie_app.models import Director, Movie, Review


class DirectorSerializers(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = 'id name count_movies'.split()


class ReviewSerializers(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'


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




