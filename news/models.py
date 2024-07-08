from django.db import models

class SearchResult(models.Model):
    keyword = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    url = models.URLField()
    published_at = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
