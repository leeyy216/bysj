from django.db import models

# Create your models here.
class User(models.Model):
	username = models.CharField(max_length=50)
	password = models.CharField(max_length=50)
	email = models.EmailField()

	def __str__(self):
	#retu = "{} {} {} {}".format(from_sch,stu_num,stu_name,into_sch)
		return self.username