from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from rango.models import Category, Page

# Using forms
from rango.forms import CategoryForm, PageForm

def index(request):
	context_dict = {}
	# Query the database for a list of ALL categories currently stored.
	# Order the categories by no. likes in descending order.
	# Retrieve the top 5 only - or all if less than 5.
	# Place the list in our context_dict dictionary that will be passed to the template engine.
	category_list = Category.objects.order_by('-likes')[:5]
	context_dict['category'] = category_list

	# Retrive the top 5 views - or all if less than 5.
	# Place the list in our context_dict dictionary that will be passed to the template engine.
	pages = Page.objects.all()[:5]
	context_dict['pages'] = pages
	# Render the response and send it back.
	return render(request, 'rango/index.html',context_dict)

def about(request):
	return HttpResponse('Rango says here is the about page')

def show_category(request, category_name_slug):
	'''@category_name_slug stores the encoded category name from URL in browsers.'''
	
	#Create a context dictionary which we can pass to the template rendering engine.
	context_dict = {}

	try:
		# Can we find a category name slug with the given name?
		# If we can't, the .get() method raises a DoesNotExist excephion.
		# So the .get() method returns one model instance or raises an exception.
		category = Category.objects.get(slug=category_name_slug)
		
		# Retrieve all of the associated pages.
		# Notes that filter() will return a list of page objects or an empty list.
		pages = Page.objects.filter(Category=category)

		# Adds our results list to the template context under name pages.
		context_dict['pages'] = pages
		# We also add the category object from the database to the context dictionary.
		# We'll use this in the template to verify that the category exists.
		context_dict['category'] = category

	except Category.DoesNotExist:
		# We get here if we didn't find the specified category.
		# Don't do anything - the template will display the "no category" message for us.
		context_dict['category'] = None
		context_dict['pages'] = None

	# Go render the response and return it to the client.
	#print(Category.objects.all)
	return render(request, 'rango/category.html', context_dict)

def create_category(request):
	form = CategoryForm()

	# A HTTP POST?
	if request.method == 'POST':
		form = CategoryForm(request.POST)

		# Have we been provided with a valid form?
		if form.is_valid():
			# Save the new category to the database.
			form.save(commit=True)
			# Now that the category is saved
			# We could give a confirmation message
			# But since the most recent category added is on the index page
			# Then we can direct the user back to the index page.
			return index(request)
		else:
			# The suppiled form contained errors - 
			# just print them to the termial
			print(form.errors)

	# Will handle the bad form, new form, or no form suppiled cases.
	# Render the form with error message (if any).
	return render(request, 'rango/create_category.html', {'form':form})


def create_page(request, category_name_slug):
	'''Add a new page entry from /rango/category/category-name/page/create/,
	this method add a page under a category.'''
	try:
		category = Category.objects.get(slug=category_name_slug)
	except Category.DoesNotExist:
		category = None
	form = PageForm()
	if request.method == 'POST':
		form = PageForm(request.POST)

		if form.is_valid():
			if category:
				page = form.save(commit=False)
				page.Category = category
				page.views = 0
				page.save()
			return show_category(request, category_name_slug)
		else:
			print(form.errors)

	context_dict = {'category':category, 'form':form}
	return render(request, 'rango/create_page.html', context_dict)
		