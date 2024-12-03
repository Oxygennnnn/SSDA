from django.db import models
import random
import secrets
from django.utils import timezone
from django.contrib.auth.models import User

class Poll(models.Model):
    poll_id = models.TextField(unique=True, blank=True)
    text = models.TextField()
    pub_date = models.DateTimeField(default=timezone.now)
    active = models.BooleanField(default=True)


    def user_can_vote(self, user):
        user_votes = user.vote_set.all()
        qs = user_votes.filter(poll=self)
        return not qs.exists()
    
    @property
    def get_vote_count(self):
        return self.vote_set.count()

    def __str__(self):
        return self.text 

    def get_result_dict(self):
        res = []
        for choice in self.choice_set.all():
            d = {}
            alert_class = ['primary', 'secondary', 'success',
                           'danger', 'dark', 'warning', 'info']
            d['alert_class'] = secrets.choice(alert_class)
            d['text'] = choice.choice_text
            d['num_votes'] = choice.get_vote_count
            if not self.get_vote_count:
                d['percentage'] = 0
            else:
                d['percentage'] = (choice.get_vote_count /
                                   self.get_vote_count) * 100
            res.append(d)
        return res

    def generate_poll_id(self):
        n=6
        id=''
        numbers='1234567890'
        for i in range(6):
            id += numbers[random.randint(0, len(numbers) - 1)]
        return id

    def save(self, *args, **kwargs):
            if not self.poll_id:
                self.poll_id = self.generate_poll_id()
                while Poll.objects.filter(poll_id=self.poll_id).exists():
                    self.poll_id = self.generate_poll_id()
            elif self.poll_id and (not self.poll_id.isdigit() or len(self.poll_id) != 6):
                self.poll_id = self.generate_poll_id()
            super().save(*args, **kwargs)

    def __str__(self):
        return self.poll_id


class Choice(models.Model):
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    
    @property
    def get_vote_count(self):
        return self.vote_set.count()

    def __str__(self):
        return f"{self.poll.text[:25]} - {self.choice_text[:25]}"


class Vote(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE)
    choice = models.ForeignKey(Choice, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.poll.text[:25]} - {self.choice.choice_text[:25]} - {self.user.username}"
