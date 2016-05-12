# randomize recipes
#
# ArgChecker checks the arguments given to the program
#
# InputParser parses the validated arguments given to this program
#
# LineRandomizer takes the parsed input, opens the files and extracts the randomized lines, while
#   excluding the previously used lines
#
# RecipeFormatter formats the output from the line randomizer
#
# TextOutput outputs the formatted strings to text
#

import math
import sys
from linerandomizer import LineRandomizer
from inputparser import InputParser
from argchecker import ArgChecker
from outputformatter import RecipeFormatter
from textoutput import TextOutput

# check arguments
argcheck = ArgChecker()
ok = argcheck.check(sys.argv)
# parse input
if ok != -1 : 
	parser = InputParser()
	# print argcheck.fileliststr
	ok = parser.parse (argcheck.fileliststr, argcheck.linenumberstr, argcheck.excludestr, argcheck.catstr)
	
	if ok != -1 :
		# process input
		processor = LineRandomizer()
		# print parser.files
		ok = processor.process(	parser.files, parser.numlines, parser.excludelines)
		if ok != -1 :
			# format output
			formatter = RecipeFormatter()
			formatter.headers = ['Oppskrifter', 'Ingredienser']
			# print processor.headers
			ok = formatter.format(processor.headers, processor.components, parser.categories)
			if ok != -1 :
				# output text
				printer = TextOutput()
				printer.output(formatter.headers, formatter.content)
