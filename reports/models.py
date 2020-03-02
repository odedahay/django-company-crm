from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from products.models import Product
from categories.models import Category
from areas.models import ProductionLine
from django.urls import reverse
import random

# hours = (
#     ("1", "1"),
#     ("1", "2"),
#     ("1", "3"),
#     ...
# )

hours = (
    [(str(x), str(x)) for x in range(1, 25)]
)
# random code generator characters
el = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
      'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

class Report(models.Model):
    day = models.DateField(default=timezone.now)
    start_hour = models.CharField(max_length=2, choices=hours)
    end_hour = models.CharField(max_length=2, choices=hours)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    plan = models.PositiveIntegerField()
    execution = models.PositiveIntegerField()
    production_line = models.ForeignKey(ProductionLine, on_delete=models.CASCADE)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def get_day(self):
        return self.day.strftime('%d/%m/%Y')
    
    def get_absolute_url(self):
        return reverse('reports:update-view', kwargs={'production_line':self.production_line,'pk':self.pk})

    def __str__(self):
        return "{}-{}-{}".format(self.start_hour, self.end_hour, self.production_line)

    class Meta:
        ordering = ('-created',)

# random code generator function
def random_code():
    random.shuffle(el)
    code = [str(x) for x in el[:12]]
    str_code = ''.join(code)

    return str_code

class ProblemReported(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.TextField()
    problem_id = models.CharField(max_length=12, unique=True, blank=True, default=random_code)
    breakdown = models.PositiveIntegerField()
    public = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    report = models.ForeignKey(Report, on_delete=models.CASCADE)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{}-{}".format(self.category.name, self.description[:20])

    class Meta:
        verbose_name = "Problem Reported"
        verbose_name_plural = "Problems Reported"