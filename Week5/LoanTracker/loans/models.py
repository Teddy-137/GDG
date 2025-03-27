from django.db import models
from django.core.validators import MaxValueValidator


class Loan(models.Model):
    name = models.CharField(max_length = 50)
    loan_amount = models.DecimalField(max_digits=10, decimal_places=2, validators=[MaxValueValidator(10000)])
    interest_rate = models.DecimalField(max_digits=5, decimal_places=2)
    due_date = models.DateField()
    is_paid = models.BooleanField(default=False)
    
    
    @property
    def total_repayment(self):
        return self.loan_amount * (1 + self.interest_rate / 100)

    def __str__(self):
        return f'{self.name} ${self.loan_amount}'


