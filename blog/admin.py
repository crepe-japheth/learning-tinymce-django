from django.contrib import admin
from .models import Articles
#from .forms import ArticlesForm

# Register your models here.


""" class ArticlesAdmin(admin.ModelAdmin):

    form = ArticlesForm
    list_display = ('title',)
 """

admin.site.register(Articles)