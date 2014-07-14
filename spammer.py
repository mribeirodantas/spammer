#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright (©) 2014 Marcel Ribeiro Dantas
#
# mribeirodantas at fedoraproject.org
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.


from pygoogle import pygoogle
import urllib2
import re

search_string = raw_input("Key word: ")
g = pygoogle(search_string)
print '%s results were found.' % (g.get_result_count())

# Opening file to save encountered e-mails.
f = open('emails.txt', 'a')

for url in g.get_urls():
    print "Looking for e-mail addresses into %s..." % url
    #response = urllib2.urlopen(url)
    opener = urllib2.build_opener()
    response = urllib2.Request(url)
    response.add_header('Accept-Language', 'en')
    response = opener.open(response)
    reading = response.read()

    # Filtering
    emails = re.findall(r'[\w\-][\w\-\.]+@[\w\-][\w\-\.]+[a-zA-Z]{1,4}',
                        reading)
    print "Results:\n"
    for email in emails:
        print email
        f.write(email)
        f.write("\n")

f.close()
