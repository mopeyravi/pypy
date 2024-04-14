from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    # image = models.CharField(max_length=255)
    # category = models.IntegerField()
    # tag = models.IntegerField()
    # author = models.IntegerField()
    counted_views = models.IntegerField(default=0)
    status = models.BooleanField(default=False)
    published_date = models.DateTimeField(null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    
    class Meta: # class e Meta  ---> in general hast va dige marbut be panel e admin nist...maslan baraye 'ordering' behtare inja taghir bedim
                                    # vali khob vaghti dar admin.py taghir midim faghat marbut be panel e admine 
        ordering = ['-created_date'] 

# show id,title instead of object_name in admin panel
    def __str__(self):
        return " {} - {}".format(self.id,self.title)