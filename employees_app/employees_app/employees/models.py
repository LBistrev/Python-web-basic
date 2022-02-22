from django.db import models
from django.urls import reverse


class AuditEntity(models.Model):
    created_on = models.DateTimeField(
        auto_now_add=True,  # при създаване го добави автоматично
    )
    update_on = models.DateTimeField(
        auto_now=True,  # при промяна го update
    )

    class Meta:
        abstract = True,


class Department(AuditEntity):
    name = models.CharField(
        max_length=20,
    )

    def get_absolute_url(self):
        return reverse('department details', kwargs={
            'id': self.id
        })

    def __str__(self):
        return self.name


class Employee(models.Model):
    SOFTWARE_DEVELOPER = 1
    QA_ENGINEER = 2
    DEVOPS_SPECIALIST = 3

    SOFT_UNI = 'SoftUni'
    GOOGLE = 'Google'
    FACEBOOK = 'Facebook'
    AUDI = 'Audi'
    BMW = 'BMW'
    COMPANIES = (SOFT_UNI, GOOGLE, FACEBOOK, AUDI, BMW)

    JANUARY = 'January'
    FEBRUARY = 'February'
    MARCH = 'March'
    APRIL = 'April'
    MAY = 'May'
    JUN = 'Jun'
    JULY = 'July'
    AUGUST = 'August'
    SEPTEMBER = 'September'
    OCTOBER = 'October'
    NOVEMBER = 'November'
    DECEMBER = 'December'

    MONTHS = (
        JANUARY, FEBRUARY, MARCH, APRIL, MAY, JUN, JULY, AUGUST, SEPTEMBER, OCTOBER, NOVEMBER, DECEMBER
    )

    first_name = models.CharField(
        max_length=30,
    )
    last_name = models.CharField(
        max_length=40,
        null=True,
        blank=True,
        default='NO NAME',
    )

    egn = models.CharField(
        max_length=10,
        unique=True,
        verbose_name='EGN'
    )

    job_title = models.IntegerField(
        choices=(
            (SOFTWARE_DEVELOPER, 'Software Developer'),
            (QA_ENGINEER, 'QA Engineer'),
            (DEVOPS_SPECIALIST, 'DevOps Specialist'),
        )
    )

    company = models.CharField(
        max_length=max(len(c) for c in [SOFT_UNI, GOOGLE, FACEBOOK]),
        choices=((c, c) for c in COMPANIES),
    )

    month_of_employment = models.CharField(
        max_length=max(len(m) for m in MONTHS),
        null=True,
        blank=True,
        choices=((m, m) for m in MONTHS),
    )

    # one to many
    department = models.ForeignKey(
        Department,
        on_delete=models.CASCADE,
    )

    image = models.ImageField(
        null=True,
        blank=True,
        upload_to='profiles',
    )

    class Meta:
        ordering = ('company', 'first_name')


class User(models.Model):
    email = models.EmailField()

    # one to one
    employee = models.OneToOneField(
        Employee,
        on_delete=models.CASCADE,
        primary_key=True,
    )


class Project(models.Model):
    name = models.CharField(
        max_length=30,
    )

    dead_line = models.DateField(
        null=True,
        blank=True,
    )

    # one to many
    employees = models.ManyToManyField(
        to=Employee
    )
