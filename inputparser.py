# class InputParser

class InputParser :
	def __init__(self) :
		self.files = []
		self.numlines = []
		self.excludelines = []
		self.categories = dict()
	# end __input__

	def parse(self, fileliststr, numliststr, excludefilename, categoryfilename) :
		# parse file list
		filelist = fileliststr.split(',')
		if(len(filelist) == 0) :
			print 'No files in file list'
			return -1
		# open and read files
		# print 'filelist:'
		# print filelist
		for filename in filelist :
			# self.files.append([])
			file = open(filename, 'r')
			# print 'opened ' + filename
			lines = file.readlines()
			for i, line in enumerate(lines) :
				lines[i] = line.rstrip('\n')
			# print lines	
			if(len(lines) == 0) :
				print 'file ' + filename + ' is empty'
				return -1
			self.files.append(lines)
			file.close()
		
		# parse line number list
		numlines = numliststr.split(',')
		for i, val in enumerate(numlines) :
			numlines[i] = int(val)
		if(len(numlines) == 0) :
			print 'did not recognize any line numbers in line number string (use comma do delimit)'
			return -1
		self.numlines = numlines
		
		if len(self.numlines) != len(self.files) :
			print 'number of given files does not match with number of given line numbers'
			return -1
		
		# open exclude file
		file = open(excludefilename, 'r')
		lines = file.readlines()
		for line in lines :
			excludenums = line.split(',')
			for i, num in enumerate(excludenums) :
				excludenums[i] = int(num)
			self.excludelines.append(excludenums)
		file.close()

		# open categoryfile
		file = open(categoryfilename, 'r')
		categorylines = file.readlines()
		# insert into a dictionary of headers and a set of ingredients
		for line in range(len(categorylines)) :
			splitline = categorylines[line].split(';')
			if len(splitline) == 2 :
				# replace ', ' with ',', and remove newline
				splitline[1] = splitline[1].rstrip('\n').replace(', ', ',')
				self.categories[splitline[0]] = set(splitline[1].split(','))

		return 0
