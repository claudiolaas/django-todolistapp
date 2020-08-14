from django.contrib import admin
from .models import Todo

# Register your models here.
class TodoAdmin(admin.ModelAdmin): 
    '''
    customizes what the admin interface looks like 
    for a particular model
    '''
    readonly_fields = ('created',)


admin.site.register(Todo,TodoAdmin)





