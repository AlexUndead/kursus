import re

from rest_framework import serializers

from .models import Registration, Vehicle, Category

re_compile_expression = '^[АВЕКМНОРСТУХ]\d{3}(?<!000)[АВЕКМНОРСТУХ]{2}\d{2,3}'


class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Registration
        fields = '__all__'


class VehicleNumberSerializer(serializers.ModelSerializer):
    def validate_number(self, value):
        re_vehicle_number_compile = re.compile(re_compile_expression)
        if not re_vehicle_number_compile.findall(value):
            raise serializers.ValidationError(
                'Неверный формат номера! Пример правильного номера: A777AA77'
            )
        return value

    class Meta:
        model = Vehicle
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
