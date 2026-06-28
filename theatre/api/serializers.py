from rest_framework import serializers
from theatre.models import Category, Cast, Movie, Series


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class CastSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cast
        fields = '__all__'


class MovieSerializer(serializers.ModelSerializer):
    categories = CategorySerializer(many=True, read_only=True)
    casts = CastSerializer(many=True, read_only=True)

    category_ids = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(),
        many=True,
        write_only=True,
        source='categories',
    )
    cast_ids = serializers.PrimaryKeyRelatedField(
        queryset=Cast.objects.all(),
        many=True,
        write_only=True,
        source='casts',
    )

    class Meta:
        model = Movie
        fields = [
            'id',
            'title',
            'description',
            'release_date',
            'duration_minutes',
            'poster_image',
            'categories',
            'casts',
            'category_ids',
            'cast_ids',
        ]

    def create(self, validated_data):
        categories = validated_data.pop('categories', [])
        casts = validated_data.pop('casts', [])
        movie = Movie.objects.create(**validated_data)
        movie.categories.set(categories)
        movie.casts.set(casts)
        return movie

    def update(self, instance, validated_data):
        categories = validated_data.pop('categories', None)
        casts = validated_data.pop('casts', None)

        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()

        if categories is not None:
            instance.categories.set(categories)
        if casts is not None:
            instance.casts.set(casts)

        return instance


class SeriesSerializer(serializers.ModelSerializer):
    categories = CategorySerializer(many=True, read_only=True)
    casts = CastSerializer(many=True, read_only=True)

    category_ids = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(),
        many=True,
        write_only=True,
        source='categories',
    )
    cast_ids = serializers.PrimaryKeyRelatedField(
        queryset=Cast.objects.all(),
        many=True,
        write_only=True,
        source='casts',
    )

    class Meta:
        model = Series
        fields = [
            'id',
            'title',
            'description',
            'release_date',
            'seasons',
            'episodes_per_season',
            'poster_image',
            'categories',
            'casts',
            'category_ids',
            'cast_ids',
        ]