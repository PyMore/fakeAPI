from django.db import models

# Create your models here.
class Services(models.Model):
    """ Services Model """

    METHOD_TYPE = (
        ('get','GET'),
        ('post','POST'),
        ('delete', 'DELETE'),
        ('patch', 'PATCH'),
        ('put', 'PUT')
    )

    name = models.CharField(max_length=30,blank=False, null=False)
    params = models.CharField(max_length=120,blank=True, null=True)
    description = models.TextField(blank=False,null=False)
    requests = models.TextField(blank=True, null=True)
    response = models.TextField(blank=True, null=True)
    status = models.IntegerField (blank=False, null=False)
        
    type = models.CharField(max_length=8,
        choices=METHOD_TYPE, null=False, blank=False)
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Service'
        verbose_name_plural = 'Services'