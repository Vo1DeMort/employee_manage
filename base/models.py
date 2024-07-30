from django.db import models


class Employee(models.Model):
    # i could use uuid
    GENDER = {"m": "male", "f": "female"}
    STATE = {
        "aya": "Ayeyarwady",
        "bgo": "Bago",
        "chn": "Chin",
        "kcn": "Kachin",
        "kyh": "Kayah",
        "kyn": "Kayin",
        "mgy": "Magway",
        "mdy": "Mandalay",
        "mon": "Mon",
        "rke": "Rakhine",
        "sgg": "Sagaing",
        "shn": "Shan",
        "tny": "Tanintharyi",
        "ygn": "Yangon",
    }
    name = models.CharField(max_length=30, null=True, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=1, choices=GENDER)
    email = models.EmailField(max_length=100)
    state = models.CharField(max_length=3, choices=STATE)
    address = models.CharField(max_length=1000)
    skills = models.CharField(max_length=200,null=True, blank=True)  # change this to char field

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return f"{self.name}"


class Education(models.Model):
    edu_type = models.CharField(max_length=100)
    description = models.CharField(max_length=100, null=True, blank=True)
    grad_year = models.CharField(null=True, blank=True, max_length=20)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)

    class Meta:
        ordering = ["description"]

    def __str__(self):
        return f"education background of {self.employee.name}"
