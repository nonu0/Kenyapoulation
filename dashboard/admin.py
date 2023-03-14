from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register([County,Population,Provinces,Central,Coast,RValley,Nyanza,Eastern,NEastern,Western])