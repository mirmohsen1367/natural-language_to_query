from django.db import models
from pgvector.django import VectorField
# Create your models here.
 
class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    embedding = VectorField(dimensions=384, blank=True, null=True)
    can_delete = models.BooleanField(default=False, help_text="Use in jupyter notebooks")
    

    def get_embedding_text_raw(self):
        return self.content