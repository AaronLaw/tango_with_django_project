from django.shortcuts import render, redirect

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout # for user_login()
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from rango.models import Category, Page, UserProfile

# Using forms
from rango.forms import CategoryForm, PageForm, UserForm, UserProfileForm

# Extend CBV from django-registration-redux
from registration.views import RegistrationView

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
	#return HttpResponse('Rango says here is the about page')
	context_dict = {'about': 'Rango says here is the about page.'}
	return render(request, 'rango/about.html', context_dict)

def show_category(request, category_name_slug): # get category_name_slug from template (a click)
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
		pages = Page.objects.filter(Category=category).order_by('-views')

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
		form = CategoryForm(request.POST) # create a CategoryForm instance

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
		form = PageForm(request.POST) # create a PageForm instance from POST data

		if form.is_valid():
			if category:
				page = form.save(commit=False) # create a page instance from a PageForm instance
				page.Category = category
				page.views = 0
				page.save() # save the page instance to database
			return show_category(request, category_name_slug)
		else:
			print(form.errors)

	context_dict = {'category':category, 'form':form}
	return render(request, 'rango/create_page.html', context_dict)

# We no longer need this method as we use django-registration-redux instead
# def register(request):
# 	'''For user registration'''
# 	# A boolean value for telling template whether the registration was successful.
# 	# Set to False initially. Code changes value to True when registration succeeds.
# 	registered = False

# 	# If it's a HTTP POST, we're interested in processing form data.
# 	if request.method == 'POST':
# 		# Attempt to grab information from the raw form information.
# 		# Note that we make use of both UserForm and UserProfileForm.
# 		user_form = UserForm(data=request.POST)
# 		profile_form = UserProfileForm(data=request.POST)

# 		# If the two forms are valid...
# 		if user_form.is_valid() and profile_form.is_valid():
# 			# Save the user's form data to the database.
# 			user = user_form.save()

# 			# Now we hash the password with the set_password method.
# 			# Once hashed, we can update the user object.
# 			user.set_password(user.password)
# 			user.save

# 			# Now sort out the UserProfile instance.
# 			# Since we need to set the user attribute outselves,
# 			# we set commit=False. This delays saving the model 
# 			# until we're ready to avoid integrity problems.
# 			profile = profile_form.save(commit=False)
# 			profile.user = user
# 			# Did the user provide a profile picture?
# 			# If so, we need to get it from the input form and put it in the UserProfile model.
# 			if 'picture' in request.FILES:
# 				profile.picture = request.FILES['picture']

# 			# Now we save the UserProfile model instance.
# 			profile.save()

# 			# Update our variable to indicate that template registration was successful.
# 			registered = True

# 		else:
# 			# Invalid from or forms - mistake or something else?
# 			# Print problems to the terminal.
# 			print(user_form.errors, profile_form.errors)
# 	else:
# 		# Not a HTTP POST, so we render our form using two ModelForm instances.
# 		# These forms will be blank, ready for user input.
# 		user_form = UserForm()
# 		profile_form = UserProfileForm()

# 	# Render the template depending on the context.
# 	context_dict = {'user_form': user_form, 'profile_form': profile_form, 'registered': registered}
# 	return render(request, 'rango/register.html',context_dict)


# We no longer need this method as we use django-registration-redux instead
# def user_login(request):
# 	# If the request is a HTTP POST, try to pull out the relevant information.
# 	if request.method == 'POST':
# 		# Gather the username and password provided by the user.
# 		# This information is obtained from the login form.
# 		# We use request.POST.get('<variable>') as opposed to
# 		# request.POST['<variable>'], because the request.POST.get('<variable>')
# 		# returns None if the value does not exist, while request.POST['<variable>']
# 		# will raise a KeyError exception.
# 		username = request.POST.get('username')
# 		password = request.POST.get('password')

# 		# Use Django's machinery to attemp to see if the username/password combination
# 		# is valid - a User object is returned if it is.
# 		user = authenticate(username=username, password=password)

# 		# If we have a User object, the details are correct.
# 		# If None, no user with matching credentials was found.
# 		if user:
# 			# Is the account active? It could have been disabled.
# 			if user.is_active:
# 				# If the account is valid and active, we can log the user in.
# 				# We'll send the user back to the homepage.
# 				login(request, user)
# 				return HttpResponseRedirect(reverse('index')) # lookup the URL of the name 'index'
# 			else:
# 				# An inactive account was used - no logging in!, logout
# 				return HttpResponse("You Rango account is disabled.")
# 		else:
# 			# Bad login details were provided. So we can't log the user in.
# 			# Print errors in terminal.
# 			print("Invalid login details: {0}, {1}".format(username, password))
# 			return HttpResponse("Invalid login details supplied.")
# 	# The request is not a HTTP POST, so display the login form.
# 	# This scenario would most likely be a HTTP GET.
# 	else:
# 		# No context variables to poss to the template system, hence the
# 		# blank dictionary object...
# 		return render(request, 'rango/login.html', [])


# We no longer need this method as we use django-registration-redux instead
# # Use the login_requiret() decorator to ensure only those logged in can access the view.
# @login_required
# def user_logout(request):
# 	# Since we know the user is logged in, we can now just log them out.
# 	logout(request)
# 	# Take the user back to the homepage.
# 	return HttpResponse(reverse('index'))
	

# Restricting access with a decorator
@login_required
def restricted(request):
	return HttpResponse("Since you're logged in, you can see this text!")

# Tracks page clickthroughs
def track_url(request):
	'''It takes a parameterised HTTP GET request (e.g. rango/goto/?page_id=1) and updates
	the number of views for the pages. The view should then redirect to the actual URL.'''
	# DONE: update the template so that it uses rango/goto/?page_id=xxx instead of providing
	# the direct URL for users to click.
	pass
	# user click on an URL
	# page.views++
	# 
	page_id = None
	if request.method == 'GET' and 'page_id' in request.GET:
		page_id = request.GET['page_id']

		try:
			page = Page.objects.get(id=page_id)
			page.views = page.views + 1
			page.save()
			url = page.url
		except:
			pass

		return redirect(url)

@login_required
def register_profile(request):
	form = UserProfileForm()

	if request.method == "POST":
		form = UserProfileForm(reqeust.POST, request.FILES)
		if form.is_valid():
			user_profile = form.save(commit=False) # create a profile instance from UserProfileForm instance
			user_profile.user = request.user
			user_profile.save()

			return redirect('index')
		else:
			print(form.errors)
	context_dict = {'form': form}

	render(request, 'rango/profile_registration.html', context_dict)

# Modifying the Registration Flow defined on django-registration-redux
class MyRegistrationView(RegistrationView):
	def get_success_url(self, user):
		return url('register_profile')

@login_required
def profile(request, username):
	try:
		user = User.objects.get(username=username)
	except User.DoesNotExist:
		return redirect('index')

	userprofile = UserProfile.objects.get_or_create(user=user)[0]
	form = UserProfileForm(
		{'website':userprofile.website, 'picture':userprofile.picture})

	if request.method =='POST':
		form = UserProfileForm(request.POST, request.FILES, instance=userprofile)
		if form.is_valid():
			form.save(commit=True)
			return redirect('profile', user.username)
		else:
			print(form.errors)

	return render(request, 'rango/profile.html',
		{'userprofile': userprofile, 'selecteduser': user, 'form': form})

@login_required
def list_profiles(request):
	userprofile_list = UserProfile.objects.all()
	return render(request, 'rango/list_profiles.html', {'userprofile_list': userprofile_list})