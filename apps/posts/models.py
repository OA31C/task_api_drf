from django.contrib.auth.models import User
from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=120, blank=False)
    link = models.URLField(max_length=128, db_index=True, unique=True, blank=False)
    creation_date = models.DateTimeField(auto_now_add=True)
    amount_of_upvotes = models.ManyToManyField(
        User, through="Vote", related_name="votes"
    )
    author = models.ForeignKey(User, on_delete=models.CASCADE, blank=False)

    @property
    def show_user_name(self):
        return self.author.username

    @property
    def count_votes(self):
        count_votes = len(self.amount_of_upvotes.all())
        return count_votes

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    author = models.ForeignKey(User, on_delete=models.CASCADE, blank=False)
    content = models.TextField(blank=False)
    creation_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.content} | to post "{self.post.title}"'


class Vote(models.Model):
    VALUE_CHOICES = ((0, "No Vote"), (1, "Vote"))

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    value = models.IntegerField(choices=VALUE_CHOICES)
    vote = models.PositiveIntegerField(default=1)
    date_when_voted = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = (("user", "post"),)

    def __str__(self):
        return f"Post {self.post.title} | Vote user: {self.user.username}"
