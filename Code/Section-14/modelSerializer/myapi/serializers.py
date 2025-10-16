from rest_framework import serializers
from .models import Student

#ModelSerializer & Validators

class StudentSerializer(serializers.ModelSerializer):
    def start_with_f(value):
        if value[0].lower() != 'f':
            raise serializers.ValidationError('Name should start with F!')
    name = serializers.CharField(validators=[start_with_f])

    # name = serializers.CharField(read_only=True)    # By default read-only is false.
    class Meta:
        model = Student
        fields = ['name', 'roll', 'city']
        # read_only_fields = ['name', 'roll']     #if there are multiple fields then we can go with this approach

    #Field level validation:
    def validate_roll(self, value):
        if value >= 200:
            raise serializers.ValidationError('Seat Full')
        return value
    
    #Object Level Validation
    def validate(self, data):
        name = data.get('name')
        city = data.get('city')
        if name.lower() == 'freak' and city.lower() != 'strawberyy':
            raise serializers.ValidationError('City must be Strawberry')
        return data
    
