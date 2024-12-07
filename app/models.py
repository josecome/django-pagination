from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Post(models.Model):
    LIST_OF_TYPE_POST = (
        ('Private', 'Private'),
        ('Public', 'Public')
    )
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    post_content = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_created = models.DateField()
    date_updated = models.DateField(null=True)

    @property
    def username(self):
        return self.user.username

    class Meta:  
        db_table = "posts"        


class Comment(models.Model):
    id = models.AutoField(primary_key=True)
    comment = models.TextField(default='Without comment')
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_created = models.DateField()
    date_updated = models.DateField(null=True)

    class Meta:  
        db_table = "comments"

#-----------------------------Shared Field--------------------------------------
# class SharedFields(models.Model): # Only shared fields
#     shared_field = models.CharField()

#    class Meta:
#        abstract = True

# class PostWithSharedField(SharedFields):
#    id = models.AutoField(primary_key=True)        
#    ...