from django.db import models

class UserInfo(models.Model):
    slack_name = models.CharField(max_length=100)
    utc_now = models.DateTimeField()
    track = models.CharField(max_length=100)
    github_file_url = models.URLField()
    github_repo_url = models.URLField()
