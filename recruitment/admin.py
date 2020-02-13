from django.contrib import admin
from .models import Applicant, Academic_detail, Profession_detail
from .models import Teaching_and_research_detail

admin.site.register(Applicant)
admin.site.register(Academic_detail)
admin.site.register(Profession_detail)
admin.site.register(Teaching_and_research_detail)
