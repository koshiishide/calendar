import datetime
from django.db import models
from django.utils import timezone

ANIMAL_CHOICES = [
    ('1', '午前'),
    ('2', '午後'),
    ('3', '終日'),
]

class Schedule(models.Model):
    """スケジュール"""
    summary = models.CharField('名前', max_length=50)
    description = models.TextField('詳細な説明', blank=True)
    start_time = models.TimeField('開始時間', default=datetime.time(10, 0, 0))
    end_time = models.TimeField('終了時間', default=datetime.time(18, 0, 0))
    date = models.DateField('日付')
    type_name = models.TextField(verbose_name="期間", choices=ANIMAL_CHOICES, blank=True)
    created_at = models.DateTimeField('作成日', default=timezone.now)
    

    def __str__(self):
        return self.summary