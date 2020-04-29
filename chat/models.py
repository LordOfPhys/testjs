from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Room(models.Model):
    name = models.TextField()
    label = models.SlugField(unique=True)

class Message(models.Model):
    room = models.ForeignKey(Room, related_name='messages', on_delete='default')
    message = models.TextField()
    def get_Text(self):
        return self.message

class GameRoom(models.Model):
    user_one = models.ForeignKey(User, related_name='user_one', on_delete='default')
    user_two = models.ForeignKey(User, related_name='user_two', on_delete='default')
    label = models.SlugField(unique=True)
    name = models.TextField()


class GameMessage(models.Model):
    user = models.ForeignKey(User, related_name='user', on_delete='default')
    room = models.ForeignKey(GameRoom, related_name='room', on_delete='default')
    u_m_x = models.CharField(max_length=100, default='0')
    u_m_y = models.CharField(max_length=100, default='0')
    u_x = models.CharField(max_length=100, default='0')
    u_y = models.CharField(max_length=100, default='0')

    def get_room(self):
        return self.room

    def get_user(self):
        return self.user

    def set_u_m_x(self, u_m_x):
        self.u_m_x = u_m_x
        self.save()

    def get_u_m_x(self):
        return self.u_m_x

    def set_u_m_y(self, u_m_y):
        sefl.u_m_y = u_m_y
        self.save()

    def get_u_m_y(self):
        return self.u_m_y

    def set_u_x(self, u_x):
        self.u_x = u_x
        self.save()

    def get_u_x(self):
        return self.u_x

    def set_u_y(self, u_y):
        self.u_y = u_y
        self.save()

    def get_u_y(self):
        return self.u_y



