from django.db import models
from django.conf import settings
from django.contrib.auth.models import User


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL)
    date_of_birth = models.DateField(blank=True, null=True)
    photo = models.ImageField(upload_to='users/%Y/%m%d', blank=True)

#    PROFILE_TYPE_CHOICES = ((ChildminderUser, 'Childminder'), (ParentUser, 'Parent'))
#    profile_type = models.Model(choices=PROFILE_TYPE_CHOICES, default=ChildminderUser)

    def __str__(self):
        return 'Profile for user {}'.format(self.user.username)


#class ChildminderUser(models.Model):
#    profile = models.OneToOneField(Profile, on_delete=models.CASCADE)
#    ofsted_no = models.CharField(max_length=10)

#    class Meta:
#        db_table = 'childminder_users'


#class ParentUser(models.Model):
#    profile = models.OneToOneField(Profile, on_delete=models.CASCADE)
#    # replace this with Child, once you have decided where child will live
#    child = models.CharField(max_length=10)

#    class Meta:
#        db_table = 'parent_users'