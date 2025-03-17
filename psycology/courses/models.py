from django.utils import timezone
from django.db import models
from django.conf import settings


class AuthorCoursesChange(models.TextChoices):
    TERAPIA = "Paula Serrano – Terapeuta Ocupacional", "Paula Serrano – Terapeuta Ocupacional"
    MASTER = "Paula Serrano – Mestre em Terapia Ocupacional, especialização em Integração Sensorial","Paula Serrano – Mestre em Terapia Ocupacional, especialização em Integração Sensorial"


class Courses(models.Model):
    class Meta:
        verbose_name = "Course"
        verbose_name_plural = "Courses"

    title = models.CharField(max_length=256)
    author = models.CharField(
        max_length=255,  # Добавляем max_length
        choices=AuthorCoursesChange.choices,
        default=AuthorCoursesChange.TERAPIA
    )
    duration = models.IntegerField()
    recipient = models.CharField(
        editable=False, max_length=100,
        default="Terapeutas ocupacionais com formação pós graduada em Integração Sensorial"
    )
    objectives = models.TextField()
    methodology = models.CharField(
        max_length=255, editable=False,
        default="As sessões de trabalho serão on line, teóricas e com analise de vídeos de casos clínicos."
    )
    content = models.TextField()
    fmw = models.TextField()  # enquadramentos в ING Framework
    price = models.DecimalField(max_digits=5, decimal_places=2)
    cover = models.ImageField(upload_to='img/courses/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def average_rating(self):
        ratings = self.course_ratings.all()
        if ratings:
            return sum(rating.rating for rating in ratings) / len(ratings)
        return 0

    def rating_list(self):
        return self.course_ratings.all()

    def __str__(self):
        return f"Course {self.title}"


class CourseRating(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    course = models.ForeignKey(Courses, on_delete=models.CASCADE, related_name="course_ratings")
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)], null=True, blank=True)
    published_at = models.DateTimeField("Published date", default=timezone.now)

    class Meta:
        unique_together = ['user', 'course']

    def __str__(self):
        return f'{self.user} - {self.course} - {self.rating}'


class Comment(models.Model):
    class Meta:
        verbose_name = "Comment"
        verbose_name_plural = "Comments"

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="user_course_comment")
    course = models.ForeignKey(Courses, on_delete=models.CASCADE, related_name="course_comment")
    text_comment = models.TextField()
    published_at = models.DateTimeField("Published date", auto_now_add=True)

    def __str__(self):
        return f"{self.user}-{self.course}"
