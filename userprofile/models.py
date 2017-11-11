from django.db import models
from django.contrib.auth.admin import User
from vaktliste.views import vakt_filter

class Skill(models.Model):
    title = models.CharField(max_length=30)
    icon = models.ImageField(upload_to="skillicons")
    description = models.TextField()

    def __str__(self):
        return self.title


"""
class Group(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title

"""
class DutyTime(models.Model):
    MONDAY = 'MO'
    TUESDAY = 'TU'
    WEDNESDAY = 'WE'
    THURSDAY = 'TH'
    FRIDAY = 'FR'

    DUTYDAYS_CHOICES = (
        (MONDAY, 'Mandag'),
        (TUESDAY, 'Tirsdag'),
        (WEDNESDAY, 'Onsdag'),
        (THURSDAY, 'Torsdag'),
        (FRIDAY, 'Fredag')
    )

    day = models.CharField(max_length=2, choices=DUTYDAYS_CHOICES, default=MONDAY)
    start_time = models.TimeField()
    end_time = models.TimeField()

    def shorten_time(self,time):
        return ":".join(str(time).split(":")[:2])
    def dutyday(self):
        return [duty[1] for duty in self.DUTYDAYS_CHOICES if duty[0]==self.day][0]

    def dutytime(self):
        return self.shorten_time(self.start_time) + " - " + self.shorten_time(self.end_time)

    def __str__(self):
        return self.day + " " + str(self.start_time) + "-" + str(self.end_time)


class Profile(models.Model):
    user = models.OneToOneField(User, related_name='profile')
    #group = models.ManyToManyField(Group, related_name="groups")
    name = models.CharField(max_length=30, null=True, blank=True)
    image = models.ImageField(upload_to="website/static/img/profilepictures")
    email = models.CharField(max_length=30, null=True, blank=True)
    
    access_card = models.CharField(max_length=20, null=True, blank=True)
    study = models.TextField(null=True, blank=True)
    skills = models.ManyToManyField(Skill, related_name="skills")
    duty = models.ManyToManyField(DutyTime, related_name="duty")

    def update(self):
        self.name = self.user.first_name + " " + self.user.last_name
        self.email = self.user.username+"@stud.ntnu.no"
       # self.get_dutytime()
        self.save()

    
    def get_dutytime(self):
        result = vakt_filter(persons=str(self))
        for day in result:
            for time in result[day]:
                self.dutytime = (day,time)
                break

    def __str__(self):
        return self.name
