from .models import PriorityTask,RecentUpdates,ApplicationStages
from rest_framework import serializers



#serializing the PriorityTask Model
class PriorityTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model=PriorityTask
        fields=['title','due_date','info']


#serializing the RecentUpdates model
class RecentUpdatesSerializer(serializers.ModelSerializer):
    class Meta:
        model=RecentUpdates
        fields=['title','updateTime']


#serializing the application stages model
class ApplicationStagesSerializer(serializers.ModelSerializer):
	class Meta:
		model=ApplicationStages
		fields=['label','count']
