#!/bin/python
#
# basketball
# copyright 2010 Chris Thompson (chris@stipes.org)
#
#       This program is free software; you can redistribute it and/or modify
#       it under the terms of the GNU General Public License as published by
#       the Free Software Foundation; either version 2 of the License, or
#       (at your option) any later version.
#
#       This program is distributed in the hope that it will be useful,
#       but WITHOUT ANY WARRANTY; without even the implied warranty of
#       MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#       GNU General Public License for more details.
#
#       You should have received a copy of the GNU General Public License
#       along with this program; if not, write to the Free Software
#       Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#       MA 02110-1301, USA.


from termcolor import colored
from optparse import OptionParser
import re

def main():
	
	COLOR = "red"
	
	usage = "usage: %prog [options] template_file filler_file"
	parser = OptionParser(usage=usage)
	parser.add_option("-n","--new", dest="new", action="store_true",
						default=False, help="Create a new filler file")
	(options, args) = parser.parse_args()
	if len(args) != 2:
		parser.error("bad arguments")
	template_file = args[0]
	filler_file = args[1]
	
	if options.new:
		with open(template_file) as template_f:
			with open(filler_file, 'w') as filler_f:
				script_text = template_f.read()
				segments = script_text.split("\n\n")
				for segment in segments:
					print segment
					slots = re.findall("SLOT\d", segment)
					for slot in slots:
						lol = raw_input(slot + " > ") # actual input :)
						filler_f.write(slot + " " + lol + "\n")
				print "COMPLETE"
	
	else:
		with open(template_file) as template_f:
			with open(filler_file) as filler_f:
				script_text = template_f.read()
				for line in filler_f:
					line = line.strip()
					if line == "": continue
					split_line = line.split(" ")
					script_text = script_text.replace( split_line[0],
										 colored(" ".join(split_line[1:]).strip().upper(), COLOR ) )
				segments = script_text.split("\n\n")
				for segment in segments:
					print segment
					lol = raw_input("> ") # barely an illusion of choice
				print colored("CONGRATULATION", COLOR, attrs=['blink','bold','underline','dark'])

if __name__ == "__main__":
	main()