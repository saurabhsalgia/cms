from django.db import models


class YouthBasicDetail(models.Model):

    class Meta:
        abstract = True

    OCCUPATION_CHOICES = (
        ('STUDENT', 'Student'),
        ('JOB', 'Job'),
        ('BUSINESS', 'Business'),
        ('OTHERS', 'Others')
    )

    first_name = models.CharField(max_length=30)
    middle_name = models.CharField(default='', max_length=30)
    last_name = models.CharField(max_length=30)
    phone_number = models.CharField(max_length=20, unique=True, blank=True, null=True)
    address = models.TextField(default='')
    date_of_birth = models.DateField(blank=True, null=True)
    occupation = models.CharField(choices=OCCUPATION_CHOICES, default='OTHERS', max_length=10)



class Youth(YouthBasicDetail):

    class Meta:
        db_table = 'youth'
        ordering = ['first_name']

    WEEKLY_FORUM_STATUS_CHOICES = (
        ('REGULAR', 'Regular'),
        ('IRREGULAR', 'Irregular'),
        ('FRESH', 'Fresh')
    )

    FOLLOW_UP_STATUS_CHOICES = (
        ('NOT STARTED', 'Not Started'),
        ('STARTED', 'Started'),
        ('CONTACTED', 'Contacted')
    )


    referred_by = models.ForeignKey('self', on_delete=models.CASCADE,
                                    related_name='regular_referrals',
                                    blank=True, null=True)

    groups = models.ManyToManyField('Group', blank=True, related_name='youths')

    status = models.CharField(choices=WEEKLY_FORUM_STATUS_CHOICES, default='REGULAR' , max_length=10)

    follow_up_status = models.CharField(choices=FOLLOW_UP_STATUS_CHOICES, default='NA', max_length=15)

    date_of_joining = models.DateField(blank=True, null=True)

    is_karyakarta = models.BooleanField(default=False)

    followers = models.ManyToManyField('self', blank=True, related_name='follows_youths', symmetrical=False)

    def __str__(self):
        return f'{self.first_name} {self.middle_name} {self.last_name}'



class Group(models.Model):

    class Meta:
        db_table = 'group'
        ordering = ['name']

    name = models.CharField(max_length=30)
    parent_group = models.ForeignKey('self', on_delete=models.CASCADE,
                                     blank=True, null=True, related_name='child_groups')
    owner = models.ForeignKey(Youth, on_delete=models.CASCADE,
                              related_name='owner_of_groups', blank=True, null=True)

    def __str__(self):
        return self.name

    @property
    def total_youths(self):
        return self.youths.count()



class VIPContact(models.Model):

    class Meta:
        db_table = 'vipcontact'
        ordering = ['name']

    FOLLOW_UP_STATUS_CHOICES = (
        ('NOT_STARTED', 'Not Started'),
        ('STARTED', 'Started'),
        ('CONTACTED', 'Contacted'),
    )

    name = models.CharField(max_length=30)
    phone_number = models.CharField(max_length=24, blank=True, null=True, unique=True)

    home_address = models.TextField(blank=True)
    office_address = models.TextField(blank=True)

    referred_by = models.ForeignKey(Youth, on_delete=models.CASCADE,
                                    related_name='referred_youths')

    followers = models.ManyToManyField(Youth, blank=True, related_name='follows_vip')

    follow_up_status = models.CharField(choices=FOLLOW_UP_STATUS_CHOICES,
                                        max_length=15, default='NOT STARTED')

    is_successful = models.BooleanField(default=False)
    comments = models.CharField(blank=True, max_length=500)

    def __str__(self):
        return self.name



# class FreshContact(YouthBasicDetail):
#
#     class Meta:
#         db_table = 'freshcontact'
#         ordering = ['first_name']
#
#     FOLLOW_UP_STATUS_CHOICES = (
#         ('NOT STARTED', 'Not started'),
#         ('STARTED', 'Started'),
#         ('CONTACTED', 'Contacted')
#     )
#
#     referred_by = models.ForeignKey(Youth, on_delete=models.CASCADE, related_name='fresh_referrals')
#     weekly_forum_joined = models.BooleanField(default=False)
#     follow_up_status = models.CharField(choices=FOLLOW_UP_STATUS_CHOICES, max_length=15)
#     groups = models.ManyToManyField(Group, blank=True, related_name='youths')
#     fresh_youth_follower = models.ManyToManyField(Youth, blank=True, related_name='fresh_followers')