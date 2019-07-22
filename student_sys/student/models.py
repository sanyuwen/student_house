from django.db import models


class Student(models.Model):
    SEX_ITEMS = [
        (1, 'male'),
        (2, 'girl'),
        (0, 'unknown'),
    ]
    STATUS_ITEMS = [
        (0, 'applicating'),
        (1, 'pass'),
        (2, 'fail'),
    ]
    name = models.CharField(max_length=120, verbose_name='full_name')
    sex = models.IntegerField(choices=SEX_ITEMS, verbose_name='gender')
    profession = models.CharField(max_length=128, verbose_name="profession")
    email = models.EmailField(verbose_name="email")
    qq = models.CharField(max_length=128, verbose_name="qq")
    phone = models.CharField(max_length=128, verbose_name="phone")
    status = models.IntegerField(choices=STATUS_ITEMS, verbose_name="current_status")
    created_time = models.DateTimeField(auto_now_add=True,
                                        editable=False,
                                        verbose_name="created_time")

    def __str__(self):
        return '<Student: {}>'.format(self.name)

    class Meta:
        verbose_name = verbose_name_plural = "student info"
