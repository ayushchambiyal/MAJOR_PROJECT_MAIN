from django.contrib import admin

from home.models import Signup,Item,cont_me
# Register your models here.
class Indexing(admin.ModelAdmin):
    readonly_fields=('id',)
admin.site.register(Signup,Indexing)
admin.site.register(Item,Indexing)
admin.site.register(cont_me,Indexing)