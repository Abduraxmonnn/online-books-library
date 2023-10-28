# Django
from django.shortcuts import get_object_or_404


def get_object(objects, pk):
    return objects.get(pk=pk)


def get_object_by_id_or_404(model, pk):
    return get_object_or_404(model, pk=pk)


def get_object_by_id_or_404_and_by_prefetch_related(objects, pk, *prefetch_related_obj):
    return get_object_by_id_or_404(objects.prefetch_related(*prefetch_related_obj), pk=pk)
