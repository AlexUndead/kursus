from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.viewsets import ReadOnlyModelViewSet

from .models import Category, Vehicle, Registration
from .utils import change_to_cyrillic
from .exceptions import (
    RegistrationViewValidateExcept,
    ChangeToCyrillicUtilsExcept
)
from .serializers import (
    RegistrationSerializer, VehicleNumberSerializer, CategorySerializer
)


class RegistrationView(APIView):
    def post(self, request, format=None):
        row_number = request.POST.get('vehicle_number', '')
        vehicle = None
        status = 'ERROR'
        message = 'Неизветная ошибка. Попробуйте повторить регистрацию позже.'
        try:
            cyrillic_number = change_to_cyrillic(row_number)
            number, category = cyrillic_number.split('*')
            validate_category = CategorySerializer(data={'name': category})
            if not validate_category.is_valid():
                raise RegistrationViewValidateExcept(
                    validate_category.errors['name']
                )
            category = Category.objects.get(**validate_category.data)
            validate_number = VehicleNumberSerializer(
                data={'number': number, 'category': category.id}
            )
            if not validate_number.is_valid():
                raise RegistrationViewValidateExcept(
                    validate_number.errors['number']
                )
            vehicle, _ = Vehicle.objects.update_or_create(
                number=number, defaults={'category': category}
            )
            status = 'SUCCESS'
            message = 'Данные успешно сохранены'
        except ValueError:
            message = 'Неверный формат номера с категорией! Пример правильного номера: A777AA77*А'
        except (RegistrationViewValidateExcept, ChangeToCyrillicUtilsExcept) as e:
            message = f'Ошибка валидации: {e}'
        finally:
            validate_registration = RegistrationSerializer(
                data={
                    'status': status, 
                    'message': message, 
                    'vehicle': vehicle.id if vehicle else None, 
                    'row_number': row_number
                }
            )
            if not validate_registration.is_valid():
                return Response(validate_registration.errors)

            validate_registration.save()
            return Response(data=validate_registration.data)


class VehicleViewSet(ReadOnlyModelViewSet):
    serializer_class = VehicleNumberSerializer
    queryset = Vehicle.objects.all()
