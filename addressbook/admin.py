from django.contrib import admin
from django.apps import apps
from django.contrib.admin.sites import AlreadyRegistered

for model in apps.get_app_config('addressbook').get_models():
    try:
        admin.site.register(model)
    except AlreadyRegistered as e:
        pass

