from rest_framework import serializers 
from .models import List, Board, Item

class BoardSerializer(serializers.ModelSerializer): # serializers.ModelSerializer just tells django to convert sql to JSON
    class Meta:
        model = Board # tell django which model to use
        fields = ('title', 'description',) # tell django which fields to include

class ListSerializer(serializers.ModelSerializer): # serializers.ModelSerializer just tells django to convert sql to JSON
    class Meta:
        model = List # tell django which model to use
        fields = ('board', 'title',) # tell django which fields to include

class ItemSerializer(serializers.ModelSerializer): # serializers.ModelSerializer just tells django to convert sql to JSON
    class Meta:
        model = Item # tell django which model to use
        fields = ('list', 'title', 'description',) # tell django which fields to include