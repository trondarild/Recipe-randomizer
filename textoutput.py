# class TextOutput

class TextOutput :
	def output(self, headers, content) :
		if len(headers) != len(content) :
			print 'length of header list and length of content list do not match'
			return -1
	
		for i, header in enumerate(headers) :
			print header
			print content[i]
		return 0
