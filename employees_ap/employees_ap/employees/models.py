from django.db import models

# Create your models here.


class Department(models.Model):
    name = models.CharField(
        max_length=20,
    )


class Employee(models.Model):
    SOFTWARE_DEVELOPER = 1
    QA_ENGINEER = 2
    DEVOPS_SPECIALIST = 3

    SOFT_UNI = "SoftUni"
    GOOGLE = 'Google'
    FACEBOOK = "Facebook"
    BMW = "BMW"
    COMPANIES = (
        SOFT_UNI, GOOGLE, FACEBOOK, BMW,
    )

    first_name = models.CharField(
        max_length=30,
    )

    last_name = models.CharField(
        max_length=40,
        null=True,
        blank=True,
    )
    egn = models.CharField(
        max_length=10,
        unique=True,
        verbose_name='EGN',
    )
    job_title = models.IntegerField(
        choices=(
            (SOFTWARE_DEVELOPER, 'Software Developer'),
            (QA_ENGINEER, 'QA Engineer'),
            (DEVOPS_SPECIALIST, 'DevOps Specialist'),
        )
    )
    # Verbose name – this option show us how to look the first column, for an example in our case first_name,
    # last_nam, egn ...
    company = models.CharField(
        max_length=max(len(c) for c in COMPANIES),
        choices=((c, c) for c in COMPANIES),
    )

    department = models.ForeignKey(
        Department,
        on_delete=models.CASCADE,
    )


class User(models.Model):
    email = models.EmailField()

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

    employees = models.ManyToManyField(
        to=Employee
    )
