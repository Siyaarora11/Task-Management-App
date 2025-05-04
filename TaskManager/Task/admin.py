from django.contrib import admin
from Task.models import Register,AddTask,Page
# Register your models here.
class RegisterAdmin(admin.ModelAdmin):
    list_display=['username','password','confirm_password']


class AddAdmin(admin.ModelAdmin):
    list_display=['title','description','deadline']


admin.site.register(Register,RegisterAdmin)
admin.site.register(AddTask,AddAdmin)
admin.site.register(Page)