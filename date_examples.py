#!/usr/bin/env python

# 1/6/13

from datetime import datetime, date, timedelta

today = date.today()

print(today)

finnegan_bd = date(2013, 1, 6)

print(finnegan_bd)

delta = today - finnegan_bd

years, days = divmod(delta.days, 365)

print("Finnegan is {} years and {} days old".format(years, days))

x = datetime(2019, 3, 14, 18, 27, 6, 29093)

print(x)

