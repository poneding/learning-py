# %%
from datetime import datetime, timedelta


class Date:
    def __init__(self, y, m, d):
        self.date = datetime(y, m, d)

    def __str__(self):
        return self.date.strftime("%Y-%m-%d")

    def __add__(self, days):
        new_date = self.date + timedelta(days)
        return Date(new_date.year, new_date.month, new_date.day)

    def __sub__(self, days):
        new_date = self.date - timedelta(days)
        return Date(new_date.year, new_date.month, new_date.day)


date = Date(2023, 10, 1)
date_plus_10 = date + 10
date_minus_5 = date - 5

print(f"Original date: {date}")
print(f"Date after adding 10 days: {date_plus_10}")
print(f"Date after subtracting 5 days: {date_minus_5}")

# %%
