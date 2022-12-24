from rest_framework import serializers
# from rest_framework.validators import UniqueTogetherValidator

from reviews.models import Category, Title, Genre, GenreTitle, Review, Comment


class ReviewSerialiazer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username'
    )

    class Meta:
        fields = '__all__'
        model = Review
        read_only_fields = ('author', 'title', 'text', 'score', 'pub_date')


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username'
    )

    class Meta:
        model = Comment
        fields = ('author', 'text', 'pub_date')


class TitleSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(
        slug_field='slug',
        queryset=Category.objects.all(),
    )
    genre = serializers.SlugRelatedField(
        slug_field='slug',
        queryset=Genre.objects.all(),
        many=True,
    )

    class Meta:
        fields = '__all__'
        model = Title


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        fields = '__all__'
        model = Category


class GenreSerializer(serializers.ModelSerializer):

    class Meta:
        fields = '__all__'
        model = Genre


# class GenreTitleSerializer(serializers.ModelSerializer):
#     genre = serializers.SlugRelatedField(
#         queryset=Genre.objects.all(),
#         slug_field='genre',
#         # default=serializers.CurrentUserDefault(),
#     )

#     title = serializers.SlugRelatedField(
#         queryset=Title.objects.all(),
#         slug_field='title',
#         # default=serializers.CurrentUserDefault(),
#     )

#     class Meta:
#         fields = '__all__'
#         model = GenreTitle
#         validators = [
#             UniqueTogetherValidator(
#                 queryset=GenreTitle.objects.all(),
#                 fields=('genre', 'title'),
#             )
#         ]
# # 1233
