from rest_framework import serializers
from rest_framework.fields import Field, ListField, SerializerMethodField
from .models import Product, Tag

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = TagModel
        fields = ['title', 'slug', 'product']


class ProductSerializer(serializers.HyperlinkedModelSerializer):
    tag_list = TagSerializer(many=True, read_only=True)

    class Meta:
        model = ProductModel
        fields = ['id', 'image', 'title', 'slug',
                  'featured', 'description', 'original_price', 'price', "tag_list"]

    def create(self, validated_data):
        users_data = validated_data.pop('params')
        validated = ProductModel.objects.create(**validated_data)
        for user_data in users_data:
            TagModel.objects.create(validated=validated, **user_data)
        return validated
      