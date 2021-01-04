from rest_framework import serializers

from .models import Hero, Prodect

class HeroSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Prodect
        fields = ('PRDName', 'PRDcatogre','ImageProdect')