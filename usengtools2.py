#!/usr/bin/env python
# import module as alt_name
from ng.west import ngtools as nt
import ng

print(ng.MAX_VOLTAGE)

nt.find_feeder()
nt.fix_outage()



