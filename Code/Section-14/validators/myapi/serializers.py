from rest_framework import serializers
from .models import Student

# Example to perform deserialization
class StudentSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    roll = serializers.IntegerField()
    city = serializers.CharField(max_length=50)

    def create(self, validated_data):
        return Student.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.roll = validated_data.get('roll', instance.roll)
        instance.city = validated_data.get('city', instance.city)
        instance.save()
        return instance
    
    #Field Level Validation on roll field
    def validate_roll(self, value):
        if value >= 200:
            raise serializers.ValidationError('No empty seat!!')
        return value
    

    # Object Level Validation on multiple field.
    def validate(self, data):
        name = data.get('name')
        city = data.get('city')
        if name.lower() == 'harry' and city.lower() != 'los angeles':
            raise serializers.ValidationError('City must be Los Angeles')
        return data