from celery import shared_task
from diver.models import Diver

@shared_task
def rename_diver(diver_id, name):
    w = Diver.objects.get(id=diver_id)
    w.name = name
    w.save()