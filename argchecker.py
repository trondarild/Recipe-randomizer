import operator

# class ArgChecker

class ArgChecker :
	def __init__(self) :
		self.fileliststr = ''
		self.linenumberstr = ''
		self.excludestr = ''
		self.catstr = ''
		self.filearg = '-f'
		self.numberarg = '-n'
		self.exclarg = '-exclude'
		self.catarg = '-category'	
		self.arglist = [self.filearg, self.numberarg, self.exclarg, self.catarg]

	def check(self, args) :
		# find filestring
		argval = self._get_arg(args, self.filearg)
		if argval == -1 :
			return argval
		self.fileliststr = argval
		# find numberstring
		argval = self._get_arg(args, self.numberarg)
		if argval == -1 :
			return argval
		self.linenumberstr = argval
		
		# find exclude name
		argval = self._get_arg(args, self.exclarg)
		if argval == -1 :
			return argval
		self.excludestr = argval
	
		# find category name
		argval = self._get_arg(args, self.catarg)
		if argval == -1:
			return argval
		self.catstr = argval	
		return 0


	def _get_arg(self, args, argname) :
		if not argname in args :
			print 'given arguments do not contain files argument {0}. Please supply it'.format(argname)
			return -1
		ix = operator.indexOf(args, argname)
		if args[ix+1] in self.arglist :
			print 'invalid argument value given for argument {0}'.format(argname)
			return -1
		return args[ix+1]
