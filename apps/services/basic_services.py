# Django
from django.shortcuts import get_object_or_404

def list_objects(objects):
    return objects.all()

def list_objects_by_select_related(objects, select_related_obj):
    return objects.all().select_related(select_related_obj)

def list_objects_by_prefetch_related(objects, prefetch_related_obj):
    return objects.all().prefetch_related(prefetch_related_obj)

def get_object_by_id_or_404(model, pk):
    return get_object_or_404(model, pk=pk)
