from rest_framework import serializers
from movies.models import Movie  # <--- CHANGE THIS LINE
import base64
from django.core.files.base import ContentFile

class MovieSerializer(serializers.ModelSerializer):
    picture = serializers.CharField(required=True, allow_blank=False)
    
    class Meta:
        model = Movie
        fields = '__all__' # Or specify the fields you want to expose
        
        def validate_picture(self, value):
            if  value:
                try:
                    format, imgstr = value.split(';base64,') 
                    ext = format.split('/')[-1]  # Get the file extension
                    data = ContentFile(base64.b64decode(imgstr), name=f'temp.{ext}')
                except Exception:
                    raise serializers.ValidationError("Invalid image format. Please upload a valid image.")
            return None
