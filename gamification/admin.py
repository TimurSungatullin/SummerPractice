# -*- coding: utf-8 -*-

from django.contrib import admin

# Register your models here.
from gamification.models import (
    GamificationStudent, GamificationDiary,
    GamificationDiaryDay, GamificationPractice,
    GamificationStudentPractice
)

admin.site.register(GamificationStudent)
admin.site.register(GamificationDiary)
admin.site.register(GamificationDiaryDay)
admin.site.register(GamificationPractice)
admin.site.register(GamificationStudentPractice)