# classes for output formatting

class RecipeFormatter :
	def __init__(self) :
		self.headers = ['Recipes', 'Ingredients']
		self.content = []

	
	def format(self, headers, components, categories) :
		# print headers (recipe names)
		# print components (ingredients)
		# create a string of headers
		recipenames = ''
		for i, header in enumerate(headers) :
			recipenames += ('{0}. {1}\n'.format(i+1, header))
		
		self.content.append(recipenames)
		
		
		# create a string of components
		
		# todo group ingredients by category
		# ingredients = ''

		# group ingredients by category
		ingredients = ''
		catcopy = categories.copy()
		compcopy = components.copy();
		for category in categories:
			# add intersection of category and components to ingredients
			#print "debug before:"
			#print catcopy[category]
			catcopy[category].intersection_update(components)
			#print "debug after:"
			#print catcopy[category]
			# remove the categorized components
			compcopy -= catcopy[category]
			if len(catcopy[category]) > 0 :
				ingredients += category + ' :\n'
				for ingredient in catcopy[category] :
					ingredients += ingredient + ', '
				ingredients += '\n\n'

		ingredients += '\n'
		# add uncategorized:
		for ingredient in compcopy :
			ingredients += ('* {0}\n'.format(ingredient))


		self.content.append(ingredients)
	
