from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator
from django.core.validators import validate_email
import logging

#ref: Sobre validações com Django: https://docs.djangoproject.com/en/3.0/ref/validators/
#https://docs.djangoproject.com/en/3.0/ref/models/fields/#genericipaddressfield

#LEVELS = ['CRITICAL', 'DEBUG', 'ERROR', 'WARNING', 'INFO']
CRITICAL = 50
FATAL = CRITICAL
ERROR = 40
WARNING = 30
WARN = WARNING
INFO = 20
DEBUG = 10
NOTSET = 0

_levelToName = {
    CRITICAL: 'CRITICAL',
    ERROR: 'ERROR',
    WARNING: 'WARNING',
    INFO: 'INFO',
    DEBUG: 'DEBUG',
    NOTSET: 'NOTSET',
}
logger = logging.getLogger(__name__)
validate_password = MinValueValidator(8)


class User(models.Model):
    name = models.CharField(max_length=50)
    last_login = models.DateTimeField(auto_now=True)
    email = models.CharField(max_length=254, validators=[validate_email])
    password = models.CharField(max_length=50, validators=[validate_password])

class Agent(models.Model):
    name = models.CharField(max_length=50)
    status = models.BooleanField(default=False)
    env = models.CharField( max_length=20)
    version = models.CharField(max_length=5)
    address = models.GenericIPAddressField(protocol='IPv4', max_length=39)

def getLevelName(level):
    result = _levelToName.get(level)
    if result is not None:
        return result
    result = _levelToName.get(level)
    return "Level %s" % level

class Event(models.Model):
    _levelToName = [(level, level) for level in _levelToName]
    level = models.CharField(max_length=20, choices=_levelToName)
    data = models.TextField()
    arquivado = models.BooleanField(default=False)
    date = models.DateField(auto_now=True)
    user = models.ForeignKey(
        User,
        on_delete=models.deletion.DO_NOTHING,
        
    )

    agent = models.ForeignKey(
        Agent,
        on_delete=models.deletion.DO_NOTHING,
        
    )

class Group(models.Model):
    name = models.CharField(max_length=50)


class GroupUser(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.deletion.DO_NOTHING,
        
    )

    group = models.ForeignKey(
        Group,
        on_delete=models.deletion.DO_NOTHING,
    
    )