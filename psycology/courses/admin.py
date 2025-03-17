from django.contrib import admin
from .models import Courses, Comment, CourseRating

class CoursesAdmin(admin.ModelAdmin):
    model=Courses
    list_display=['title', 'author', 'duration', 'price']

class CoursesComment(admin.ModelAdmin):
    model = Comment
    list_display=['user','course','published_at']

class CoursesRatingAdmin(admin.ModelAdmin):
    model = CourseRating
    list_display = ['user', 'course', 'rating', 'published_at']

admin.site.register(Courses, CoursesAdmin)
admin.site.register(Comment, CoursesComment)
admin.site.register(CourseRating, CoursesRatingAdmin)

