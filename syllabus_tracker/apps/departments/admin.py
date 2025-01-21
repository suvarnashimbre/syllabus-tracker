from django.contrib import admin
from django.apps import apps

[admin.site.register(model) for model in apps.get_app_config('departments').get_models()]
