from django.contrib import admin
from .models import PriorityTask,ApplicationStages,RecentUpdates
# Register your models here.
admin.site.register(PriorityTask)
admin.site.register(RecentUpdates)
admin.site.register(ApplicationStages)
