# class LineRandomizer

import random

class LineRandomizer :

	def __init__(self) :
		self.headers = []
		self.components = set()

	#
	# input:	files - a two dimensional list of strings of the
	#				form '<header>;<component1>,..,<componentn>'
	#			numbers - a list of integers indicating how many lines to use from each of the files
	# 			exclude - a two dimensional list of integers indicating which lines to exclude
	def process(self, files, numbers, exclude) :
		# check that there are file and number lists are same length
		if len(files) != len(numbers) :
			return -1
        # TODO make this a class variable so external process can save
		usedlines = []
		# iterate through files
		for i in range(len(files)) :
			usedlines.append([])
			# create a range equal to length of list corresponding to file
			linerange = range(len(files[i]))
			#print 'linerange='
			#print linerange
			lines = files[i]
			# remove files in exclude list from range
			# dont remove more than is needed to create a valid list
			while (len(linerange) - len(exclude[i])) <= numbers[i] :
				exclude[i].remove(exclude[i][0])
			#print 'exclude='
			#print exclude
			for excl in exclude[i] :
				# print 'removing {0}'.format(excl)
				linerange.remove(excl)
			#print 'linerange='
			#print linerange
			# draw the given number of random lines from the file
			#print 'range={0}'.format(range(numbers[i]))
			for j in range(numbers[i]) :
				linenum = random.choice(linerange)
				linerange.remove(linenum)
				#print 'linenum={0}'.format(linenum)
				# store each number in used list
				#print 'i={0}'.format(i)
				usedlines[i].append(linenum)
				# split the line by ; and ,
				splitline = files[i][linenum].replace('; ',';').split(';')
				# add first split to headers
				# print 'splitline:'
				# print splitline
				self.headers.append(splitline[0])
				# add remainders to components
				comps = splitline[1].replace(', ', ',').split(',')
				self.components = self.components.union(comps)
			# end for
		# end for
		# print usedlines to a file
        # TODO make exclude.txt an argument, or just leave this to outside process
		usedlinefile = open('exclude.txt', 'w')
		for line in usedlines :
			for i in range(len(line)):
				usedlinefile.write('{0}'.format(line[i]))
				if i < len(line)-1 :
					usedlinefile.write(',')
			usedlinefile.write('\n')
		usedlinefile.close()
		return 0
	# end process
