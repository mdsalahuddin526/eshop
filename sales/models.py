from django.db import models

class ProductName(models.Model):
    pr_name = models.CharField(max_length=200)
    
   
    def __str__(self):
        return self.pr_name

    def __unicode__(self):
        return 

class ProductDetail(models.Model):
    desc = models.TextField()
    price = models.CharField(max_length=200)
   

    pr_desc = models.ForeignKey('ProductName', related_name='ProductName', on_delete=models.CASCADE)

    def __str__(self):
        return self.desc

    def __unicode__(self):
        return 
    

