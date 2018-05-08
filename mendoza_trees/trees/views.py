from django.shortcuts import render
from .models import Tree
import json
from django.utils.html import mark_safe


def index(request):
    trees = list(Tree.objects.select_related('species').values(
        'latitude', 'longitude', 'species__name'
    )[:100])
    return render(request, 'index.html', {
        'trees': mark_safe(json.dumps(trees)),
    })
