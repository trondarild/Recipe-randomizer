#!/usr/bin/python
# -*- coding: latin-1 -*-

#
# unit tests for list processor
#

import unittest
import math
from linerandomizer import LineRandomizer
from inputparser import InputParser
from argchecker import ArgChecker
from outputformatter import RecipeFormatter
from textoutput import TextOutput

class TestRecipeRandomizer(unittest.TestCase):

        def setUp(self):
            # add some setup code here
            self.args = ['a.txt,b.txt,c.txt', '1,2,3', 'exclude.txt']

            # simulates already read files
            file1 = ['1zero;a,b,c','1one;a,b,c', '1two;a,b,c', '1three;a,b,c', '1four;a,b,c']
            file2 = ['2zero;a,b,c','2one;a,b,c', '2two;a,b,c', '2three;a,b,c', '2four;a,b,c']
            file3 = ['3zero;a,b,c','3one;a,b,c', '3two;a,b,c', '3three;a,b,c', '3four;a,b,c']

            self.files = [file1, file2, file3]

            # number of lines to use per file
            num1 = 2
            num2 = 2
            num3 = 1

            self.nums = [num1, num2, num3]
            self.noexcl = []

            # lines to exclude per file
            excl1 = [0, 1]
            excl2 = [2, 3]
            excl3 = [1, 2, 3]

            self.excl = [excl1, excl2, excl3]


            # collect excluded headers
            self.exclheaders = []
            for i in range(len(self.excl)) :
                for j in range(len(self.excl[i])) :
                    # get header of the excluded line
                    excllinenum = self.excl[i][j]
                    # print 'excllinenum={0}'.format(excllinenum)
                    exclline = self.files[i][excllinenum]
                    # print 'exclline=' + exclline
                    header = exclline.split(';')[0]
                    self.exclheaders.append(header)
        # end setUp

        def test_process(self) :
            print 'function test_process'
            # first give in a normal
            linerand = LineRandomizer()

            # todo valid cases
            # 1) exclude nothing
            retval = linerand.process(self.files, self.nums, self.noexcl)
            self.assertEqual(retval, 0)


            retval = linerand.process(self.files, self.nums, self.excl)
            self.assertEqual(retval, 0)
            # get the result
            headers = linerand.headers
            print headers
            components = linerand.components
            print components
            # headers should contain sum of nums
            self.assertEqual(len(headers), sum(self.nums))
            # headers should not contain anything from the exclusion
            # list
            for hdr in self.exclheaders :
                print 'exclheader=' + hdr
                self.assertTrue(not hdr in headers)

            # check that components set is not empty
            self.assertTrue(len(components) != 0)

            # todo error cases
            # 1) exclude more than are available
            # 2) exclude equal to available

        # end test_process

	def test_parse(self) :
		print 'function test_parse'
		# create test data
		filenames = ['file1.txt', 'file2.txt', 'file3.txt']
		#filenames = ['oppskrifter kjøtt.txt', 'oppskrifter fisk.txt', 'oppskrifter kylling.txt']

		# write all files to disk
		for i, filename in enumerate(filenames) :
			file = open(filename, 'w')
			for line in self.files[i] :
				# write all lines to file
				# print 'writing to file ' + filenames[i] + ' line : ' + line
				file.write(line + '\n')
			file.close()

		# write the exclude file
		exclfilename = 'testexclude.txt'
		file = open(exclfilename, 'w')
		for line in self.excl :
			file.write(','.join(map(str, line)) + '\n')
		file.close()

		# normal input
		# filenames = ['oppskrifter kjøtt.txt', 'oppskrifter fisk.txt', 'oppskrifter kylling.txt']

		fileliststr = ','.join(filenames)
		print 'fileliststr :' + fileliststr
		numliststr = ','.join(map(str, self.nums))

		parser = InputParser()
		retval = parser.parse(fileliststr, numliststr, exclfilename)
		self.assertEqual(retval, 0)
		files = parser.files
		numlines = parser.numlines
		excllines = parser.excludelines

		print 'files {0}'.format(files)
		print 'numlines {0}'.format(numlines)
		print 'excllines {0}'.format(excllines)

		self.assertEqual(files, self.files)
		self.assertEqual(numlines, self.nums)
		self.assertEqual(excllines, self.excl)

		# todo : error conditions
		# 1 some files dont exist
		# 2 files contain wrong format
		# 3 line nums does not correspond with file content
		# (referencing too many lines, or invalid line numbers)
	# end test_parse

	def test_argchecker(self) :
		print 'function test_argchecker'
		# valid args
		testfileliststr = 'file1.txt,file2.txt,file3.txt'
		testnumstr = '2,2,3'
		testexcludename = 'exclude.txt'
		testargs = ['foo.py', '-f', testfileliststr, '-n', testnumstr, '-exclude', testexcludename]
		argch = ArgChecker()
		retval = argch.check(testargs)
		self.assertEqual(retval, 0)

		fileliststr = argch.fileliststr
		self.assertEqual(fileliststr, testfileliststr)
		numstr = argch.linenumberstr
		self.assertEqual(numstr, testnumstr)
		exclname = argch.excludestr
		self.assertEqual(exclname, testexcludename)

		# todo: alternative ordering
		testargs = ['foo.py', '-n', testnumstr, '-exclude', testexcludename, '-f', testfileliststr]
		retval = argch.check(testargs)
		self.assertEqual(retval, 0)

		fileliststr = argch.fileliststr
		self.assertEqual(fileliststr, testfileliststr)
		numstr = argch.linenumberstr
		self.assertEqual(numstr, testnumstr)
		exclname = argch.excludestr
		self.assertEqual(exclname, testexcludename)

		# alternative ordering 2
		testargs = ['foo.py', '-exclude', testexcludename, '-f', testfileliststr, '-n', testnumstr]
		retval = argch.check(testargs)
		self.assertEqual(retval, 0)

		fileliststr = argch.fileliststr
		self.assertEqual(fileliststr, testfileliststr)
		numstr = argch.linenumberstr
		self.assertEqual(numstr, testnumstr)
		exclname = argch.excludestr
		self.assertEqual(exclname, testexcludename)

		# todo error condtions
		# 1 missing testfiles
		testargs = ['foo.py', '-exclude', testexcludename, '-n', testnumstr]
		retval = argch.check(testargs)
		self.assertEqual(retval, -1)

		# 2 missing numbers
		testargs = ['foo.py', '-exclude', testexcludename, '-f', testfileliststr]
		retval = argch.check(testargs)
		self.assertEqual(retval, -1)
		# 3 missing both testfiles and numbers
		testargs = ['foo.py', '-exclude', testexcludename, ]
		retval = argch.check(testargs)
		self.assertEqual(retval, -1)

		# 4 missing exclude file
		testargs = ['foo.py', '-exclude', '-f', testfileliststr, '-n', testnumstr]
		retval = argch.check(testargs)
		self.assertEqual(retval, -1)



	def test_formatter(self) :
		print 'function test_formatter'
		names = ['pizza', 'nachos', 'komle']
		components = ['kjøttdeig', 'mel', 'nachochips', 'tomater', 'poteter']
		formatter = RecipeFormatter()
		formatter.headers = ['Oppskrift', 'Ingredienser']
		formatter.format(names, components)
		self.assertTrue(len(formatter.headers) > 0)
		self.assertTrue(len(formatter.content) > 0)

		# test text output
		printer = TextOutput()
		printer.output(formatter.headers, formatter.content)


# run tests
if __name__ == '__main__':
    unittest.main()
