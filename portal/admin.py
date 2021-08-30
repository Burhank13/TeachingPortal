from django.contrib import admin
from .models import Test, Assignment, Person

# Register your models here.
admin.site.register(Test)
admin.site.register(Assignment)
admin.site.register(Person)