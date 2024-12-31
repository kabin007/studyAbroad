from django.db import models

#django model for storing the information related to Priority Tasks

class PriorityTask(models.Model):
    title=models.CharField(max_length=200)
    due_date=models.DateTimeField()
    info=models.CharField(max_length=300)



    def __str__(self):
        return self.title

#django model for storing the information related to the recent updates

class  RecentUpdates(models.Model):
    title=models.CharField(max_length=200)
    updateTime=models.DateTimeField()


    def __str__(self):
        return self.title

    
class ApplicationStages(models.Model):
	label=models.CharField(max_length=200)
	count=models.IntegerField()

	def __str__(self):
		return self.label
