from django.db import models

# Create your models here.
class Enrollinfo(models.Model):
	from_sch = models.CharField(max_length = 30)
	stu_num = models.CharField(max_length = 30)
	stu_name = models.CharField(max_length = 30)
	into_sch = models.CharField(max_length = 30)
	
	def __str__(self):
		#retu = "{} {} {} {}".format(from_sch,stu_num,stu_name,into_sch)
		return self.stu_name


class enroll(models.Model):
	from_sch = models.CharField(max_length = 30)
	stu_num = models.CharField(max_length = 30)
	stu_name = models.CharField(max_length = 30)
	into_sch = models.CharField(max_length = 30)
	
	def __str__(self):
		#retu = "{} {} {} {}".format(from_sch,stu_num,stu_name,into_sch)
		return self.stu_name

class ScrapyModel(models.Model):
	seqnum = models.CharField(max_length = 30)
	stu_num = models.CharField(max_length = 30)
	stu_name = models.CharField(max_length = 30)
	
	def __str__(self):
		#retu = "{} {} {} {}".format(from_sch,stu_num,stu_name,into_sch)
		return self.stu_name