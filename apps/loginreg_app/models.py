from __future__ import unicode_literals
from django.db import models
import bcrypt
# import loginreg
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
# Create your models here.
class UserManager(models.Manager):
    def basic_validator(self, postData):
        # print("POST_DATA",postData)
        errors = {}
        emailcheck = Users.objects.all().values_list('email',flat=True)
        # print(emailcheck)
        # print(errors)
        if postData['reg'] == 'new_user':
            if len(postData['first'])<1:
                errors['first']="First name CANNOT be left blank"
            if len(postData['last'])<1:
                errors['last']="Last name CANNOT be left blank"
            if not EMAIL_REGEX.match(postData['email']):
                errors['email_wrong'] = "Please enter a valid email address"
            if postData['email'] in emailcheck:
                errors['email_taken'] = "That email is already registered"
            if postData['pass1'] != postData['pass2']:
                errors['passwrong']="Password confirmation fail"
            if errors:
                # print(errors)
                return errors
            else:
                hash = bcrypt.hashpw(postData['pass1'].encode(), bcrypt.gensalt())
                makeme = Users.objects.create(
                    first_name=postData['first'], 
                    last_name=postData['last'],
                    email=postData['email'],
                    password=hash
                    )
                return makeme

        if postData['reg'] == 'login':
            # filter always returns a list
            challenge = Users.objects.filter(email=postData['email'])
            # print(challenge)
            if len(challenge):
                if bcrypt.checkpw(postData['pw'].encode(), challenge[0].password.encode()):
                    return challenge[0]
            return 'Invalid email & password combination'

class Users(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(blank=False, unique=True,)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()
    
    def __repr__(self):
        return "<Users object: {} {} {}>".format(self.first_name,self.last_name,self.id)

class Messages(models.Model):
    user = models.ForeignKey(Users, related_name='msg')
    message = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __repr__(self):
        return "{}".format(self.message)

class Comments(models.Model):
    message= models.ForeignKey(Messages, related_name='comment')
    user = models.ForeignKey(Users, related_name='comment')
    comment = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __repr__(self):
        return "<Comment: {} | by:{}>".format(self.comment,self.user_id)