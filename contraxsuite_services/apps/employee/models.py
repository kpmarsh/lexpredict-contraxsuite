from django.db import models
from apps.document.models import Document
from apps.extract.models import Usage



class Employer(models.Model):

    name = models.CharField(max_length=1024, db_index=True)

class EmployerUsage(Usage):

    employer= models.ForeignKey(Employer, db_index=True)

    class Meta:
        ordering=['-count']

class Employee(models.Model):

    document = models.ForeignKey(Document, db_index=True)
    name= models.CharField(max_length=1024, db_index=True)
    employer=models.ForeignKey(Employer, db_index=True, blank=True, null=True)
    annual_salary= models.FloatField(blank=True, null=True)
    salary_currency= models.CharField(max_length=10, blank=True, null=True)
    effective_date= models.DateField(blank=True, null=True)


    class Meta:
        unique_together=(("name", "document"),)
        verbose_name_plural='Employees'
        ordering = ('name',)


    def __str__(self):
        return "Employee (" \
               "doc_id= {0}," \
               "name={0}," \
               "salary={2})" \
            .format(self.document.id, self.name, self.salary)



class Noncompete_Provision:

    text_unit= models.TextField(max_length=16384)
    similarity=models.DecimalField(max_digits=5, decimal_places=2)
    employee = models.ForeignKey(Employee)
    document=models.ForeignKey(Document)
