from django.dispatch import receiver
from django.core.mail import send_mail
from django.db.models.signals import post_save

from .models import Vehicle

@receiver(post_save, sender=Vehicle)
def send_vehicle_email(sender, instance, created, **kwargs):
    pass
    #send_mail(
    #    subject='Создание модели Транспорт',
    #    message='Создана модель Транспорт',
    #    from_email='from@example.com',
    #    recipient_list=['recipient@example.com'],
    #)
    
