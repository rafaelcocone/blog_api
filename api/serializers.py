from rest_framework import serializers
from .models import Post, Comment

class PostSerializers(serializers.ModelSerializer):
    class Meta:
        model =  Post
        fields = ('id','title','text','id_author','active','created_at','updated_at' )
        read_only_fields = ('id','created_at','updated_at')

class CommentSerializers(serializers.ModelSerializer):
    
    class Meta:
        model =  Comment
        fields = ('id','post','content','id_author','active','created_at','updated_at' )
        read_only_fields = ('id','created_at','updated_at')

