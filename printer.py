#!/usr/bin/env python
import urllib2
import re
from datetime import datetime

response = urllib2.urlopen('https://cardenalprinter.stanford.edu/hp/device/this.LCDispatcher')

html = response.read()
m = re.findall('id=\"Text17\".*?>(.*?)</span>', html)

status = m[0]

if status.find('Empty') >= 0:
  raise Exception('%s: Printer tray is empty' % datetime.now())
elif status.find('OK') >= 0:
  print '%s: Printer is fine' % datetime.now()
else:
  raise Exception('%s: Unknown printer status: %s' % (datetime.now(), status))

