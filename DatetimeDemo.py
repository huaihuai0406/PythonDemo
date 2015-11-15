#!/usr/bin/env python
# encoding: utf-8

import datetime

d1 = datetime.date(2009, 05, 31)
d2 = datetime.date(2009, 02, 01)
print d1 - d2
print d1.isocalendar()
d = datetime.timedelta(weeks=20)
print d1 + d
print d1 - d
