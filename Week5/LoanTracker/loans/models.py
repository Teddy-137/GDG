from django.db import models


class Loan(models.Model):
    name = models.CharField(max_length = 50)
    loan_amount = models.DecimalField(max_digits=10, decimal_places=2)
    interest_rate = models.DecimalField(max_digits=5, decimal_places=2)
    due_date = models.DateField()
    is_paid = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.name} ${self.loan_amount}'


