from django.contrib import admin
from .models import Tree, Species

admin.site.register(Tree,
    list_display=('species', 'latitude', 'longitude')
)
admin.site.register(Species)
