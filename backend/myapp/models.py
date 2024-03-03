from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
# Create your models here.


class Documents(models.Model):
    owner            = models.ForeignKey(User, verbose_name=_("Owner"), on_delete=models.RESTRICT)
    name             = models.CharField(_("Name"), max_length=50)
    document_content = models.TextField(_("Content"))
    created_at       = models.DateTimeField(_("Created At"), auto_now=False, auto_now_add=False)
    updated_at       = models.DateTimeField(_("Updated At"), auto_now=False, auto_now_add=False)
    

class Collaborators(models.Model):
    class UserAccess(models.TextChoices):
        RO = ('Read Only', 'Read Only')
        RW = ('Read/Write', 'Read/Write')
    
    user      = models.ForeignKey(User, verbose_name=_(""), on_delete=models.RESTRICT)
    access_level = models.CharField(_("Access Level"), max_length=50, choices=UserAccess.choices)
    joined_at    = models.DateTimeField(_("Joined At"), auto_now=False, auto_now_add=False)
    left_at      = models.DateTimeField(_("Left At"), auto_now=False, auto_now_add=False)


class Edits(models.Model):
    document = models.ForeignKey(Documents, verbose_name=_("Documents"), on_delete=models.RESTRICT)
    user = models.ForeignKey(User, verbose_name=_("User"), on_delete=models.RESTRICT)
    timestamp = models.DateTimeField(_("Time Stamp"), auto_now=False, auto_now_add=False)
    changes_made = models.JSONField(null=True)