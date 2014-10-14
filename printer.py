#!/usr/bin/env python
import urllib2
from datetime import datetime
from lxml import html

response = urllib2.urlopen('https://cardenalprinter.stanford.edu/hp/device/this.LCDispatcher')

tree = html.fromstring(response.read())
status = tree.xpath("//span[@id='Text17']/text()")
# status = parsed_html.body.find('span', attrs={'id':'Text17'}).text
status = status[0]

if status.find('Empty') >= 0:
  raise Exception('%s: Printer tray is empty' % datetime.now())
elif status.find('OK') >= 0:
  print '%s: Printer is fine' % datetime.now()
else:
  raise Exception('%s: Unknown printer status: %s' % (datetime.now(), status))

