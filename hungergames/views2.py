from django.shortcuts import render

# Create your views here.
import json
import random
import requests
import webbrowser
from django.views.generic import TemplateView
import urllib
import re

def fetch_facet_json(url):
	facet_json = json.load(urllib.urlopen(url))
	return facet_json

def autosuggest(tag_type, language, geography):
	autosuggest = "http://" + geography + ".openfoodfacts.org/cgi/suggest.pl?lc="+ language + "&tagtype=" + tag_type
	return autosuggest

def get_traces(self):
	traces = fetch_facet_json("http://world.openfoodfacts.org/traces.json")
	return traces

def allergens(self):
	allergens = fetch_facet_json("http://world.openfoodfacts.org/allergens.json")
	return allergens

def allergens_list(self):
	allergens_list = allergens['tags']	
	return allergens_list

def additives(self):
	additives = fetch_facet_json("http://world.openfoodfacts.org/additives.json")
	return additives

def additives_list(self):
	additives_list = additives['tags']
	return additives_list

def brands(self):
	brands = fetch_facet_json("http://world.openfoodfacts.org/brands.json")
	return brands

def brands_list(self):
	brands_list = brands['tags']
	return brands_list

def countries(self):
	countries = fetch_facet_json("http://world.openfoodfacts.org/countries.json")
	return countries

def countries_list(self):
	countries_list = countries['tags']	
	return countries_list

def codes(self):
	packaging_codes = fetch_facet_json("http://world.openfoodfacts.org/codes.json")
	return codes

def codes_list(self):
	codes_list = codes['tags']	
	return codes_list

def categories(self):
	categories = fetch_facet_json("http://world.openfoodfacts.org/categories.json")
	import hungergames.categories as fgf
	categories = json.load(fgf)
	return categories

def categories_list(self):
	categories = fetch_facet_json("http://world.openfoodfacts.org/categories.json")
	categories_list = categories['tags']
	return categories_list

def ingredients(self):
	ingredients = fetch_facet_json("http://world.openfoodfacts.org/ingredients.json")
	return ingredients

def ingredients_list(self):	
	ingredients_list = ingredients['tags']
	return ingredients_list

def labels(self):
	labels = fetch_facet_json("http://world.openfoodfacts.org/labels.json")
	return traces

def labels_list(self):
	labels_list = labels['tags']
	return labels_list

def languages(self):
	languages = fetch_facet_json("http://world.openfoodfacts.org/languages.json")
	return ingredients

def languages_list(self):	
	languages_list = languages['tags']
	return languages_list

def packagings(self):
	packagings = fetch_facet_json("http://world.openfoodfacts.org/packaging.json")
	return packagings

def packaging_list(self):
	packaging_list = packagings['tags']
	return packaging_list

def packaging_codes(self):
	packaging_codes = fetch_facet_json("http://world.openfoodfacts.org/packager-codes.json")
	return packaging_codes

def packaging_codes_list(self):
	packaging_codes_list = packaging_codes['tags']	
	return packaging_codes_list

def purchase_places(self):
	purchase_places = fetch_facet_json("http://world.openfoodfacts.org/purchase-places.json")
	return purchase_places

def purchase_places_list(self):
	purchase_places_list = purchase_places['tags']
	return purchase_places_list

def states(self):
	states = fetch_facet_json("http://world.openfoodfacts.org/states.json")
	return states

def states_list(self):
	states_list = states['tags']
	return states_list

def stores(self):
	stores = fetch_facet_json("http://world.openfoodfacts.org/stores.json")
	return stores

def stores_list(self):
	stores_list = stores['tags']	
	return stores_list

def traces_list(self):
	traces_list = traces['tags']
	return traces_list


# def quantity_list(self):
# 	quantity_list = quantity['tags']
# 	return quantity_list

# def official_websites_list(self):
# 	official_websites_list = official_websites['tags']
# 	return official_websites_list

# def best_before_date_list(self):
# 	best_before_date_list = best_before_date['tags']
# 	return best_before_date_list

# def serving_size_list(self):
# 	serving_size_list = serving_size['tags']
# 	return serving_size_list

# def energy_list(self):
# 	energy_list = energy['tags']
# 	return energy_list

# def fat_list(self):
# 	fat_list = fat['tags']
# 	return fat_list

# def saturated_fat_list(self):
# 	saturated_fat_list = saturated_fat['tags']
# 	return saturated_fat_list

# def carbohydrates_list(self):
# 	carbohydrates_list = carbohydrates['tags']
# 	return carbohydrates_list

# def sugars_list(self):
# 	sugars_list = sugars['tags']
# 	return sugars_list

# def fiber_list(self):
# 	fiber_list = fiber['tags']
# 	return fiber_list

# def proteins_list(self):
# 	proteins_list = proteins['tags']
# 	return proteins_list

# def salt_list(self):
# 	salt_list = salt['tags']
# 	return salt_list

# def sodium_list(self):
# 	sodium_list = sodium['tags']
# 	return sodium_list

# def alcohol_list(self):
# 	alcohol_list = alcohol['tags']
# 	return alcohol_list

# def carbon_footprint_list(self):
# 	carbon_footprint_list = carbon_footprint['tags']
# 	return carbon_footprint_list


def get_json_for_randomization(url):
	header = {'x-requested-with': 'XMLHttpRequest'}
	mainPage = requests.get(url, headers = header)
	json_for_randomization = mainPage.json()
	return json_for_randomization

def get_json_url_for_product(barcode):
	json_url_for_product = "http://world.openfoodfacts.org/api/v0/product/"+ str(barcode) +".json"
	return json_url_for_product

def get_edit_url_for_product(barcode):
	edit_url_for_product = "http://world.openfoodfacts.org/cgi/product.pl?type=edit&code=" + str(barcode)
	return edit_url_for_product

def get_result(url_json):
	if requests.get(url_json) == 404:
		result = json.dumps(urllib.urlopen('http://world.openfoodfacts.org/states.json').read())
	else:
		result = json.dumps(urllib.urlopen(url_json).read())
		#result = requests.get(urljson3).text.replace("\n", " ").replace("-", " ").lower()
	return result

def get_packaging(barcode):
	product = get_result(get_json_url_for_product(barcode))
	packaging = product.packaging
	return packaging

def get_packaging_codes(barcode):
	product = get_result(get_json_url_for_product(barcode))
	packaging_code = product.packaging_codes
	return packaging_code

def get_categories(barcode):
	product = get_result(get_json_url_for_product(barcode))
	categories = product.categories
	return categories

def get_ingredients(barcode):
	product = get_result(get_json_url_for_product(barcode))
	ingredients = product.ingredients
	return ingredients

def get_labels(barcode):
	product = get_result(get_json_url_for_product(barcode))
	labels = product.labels
	return labels

def get_brands(barcode):
	product = get_result(get_json_url_for_product(barcode))
	brands = product.brands
	return brands

def get_quantity(barcode):
	product = get_result(get_json_url_for_product(barcode))
	quantity = product.quantity
	return quantity

def get_official_websites(barcode):
	product = get_result(get_json_url_for_product(barcode))
	official_websites = product.official_websites
	return official_websites

def get_best_before_date(barcode):
	product = get_result(get_json_url_for_product(barcode))
	best_before_date = product.best_before_date
	return best_before_date

def get_stores(barcode):
	product = get_result(get_json_url_for_product(barcode))
	stores = product.stores
	return stores

def get_traces(barcode):
	product = get_result(get_json_url_for_product(barcode))
	traces = product.traces
	return traces

def get_serving_size(barcode):
	product = get_result(get_json_url_for_product(barcode))
	serving_size = product.serving_size
	return serving_size

def get_energy(barcode):
	product = get_result(get_json_url_for_product(barcode))
	energy = product.energy
	return energy

def get_fat(barcode):
	product = get_result(get_json_url_for_product(barcode))
	fat = product.fat
	return fat

def get_saturated_fat(barcode):
	product = get_result(get_json_url_for_product(barcode))
	saturated_fat = product.saturated_fat
	return saturated_fat

def get_carbohydrates(barcode):
	product = get_result(get_json_url_for_product(barcode))
	carbohydrates = product.carbohydrates
	return carbohydrates

def get_sugars(barcode):
	product = get_result(get_json_url_for_product(barcode))
	sugars = product.sugars


def get_fiber(barcode):
	product = get_result(get_json_url_for_product(barcode))
	fiber = product.fiber
	return fiber

def get_proteins(barcode):
	product = get_result(get_json_url_for_product(barcode))
	proteins = product.proteins
	return proteins

def get_salt(barcode):
	product = get_result(get_json_url_for_product(barcode))
	salt = product.salt
	return salt

def get_sodium(barcode):
	product = get_result(get_json_url_for_product(barcode))
	sodium = product.sodium
	return sodium

def get_alcohol(barcode):
	product = get_result(get_json_url_for_product(barcode))
	alcohol = product.alcohol
	return alcohol

def get_carbon_footprint(barcode):
	product = get_result(get_json_url_for_product(barcode))
	carbon_footprint = product.carbon_footprint
	return carbon_footprint

def get_first_three_digits(barcode):
	product = get_result(get_json_url_for_product(barcode))
	return product
	first_three_digits = barcode[0:3]
	return first_three_digits

def get_second_three_digits(barcode):
	second_three_digits = barcode[3:6]
	return second_three_digits

def get_third_three_digits(barcode):
	third_three_digits = barcode[6:9]
	return third_three_digits

def get_fourth_three_digits(barcode):
	fourth_three_digits = barcode[9:13]
	return fourth_three_digits

def get_image_ocr_json(first_three_digits, second_three_digits, third_three_digits,fourth_three_digits, image_name):
	try:
		image_ocr_json = "http://world.openfoodfacts.ovh/images/products/" + str(first_three_digits)+ "/" + str(second_three_digits)+ "/" + str(third_three_digits)+ "/" + str(fourth_three_digits)+ "/" + str(image_name) + ".json"
		return str(image_ocr_json)
	except IndexError:
		return None

def get_front_json_url(language,one,two,three,four,number):
	#"url_json_front_" + language = "http://static.openfoodfacts.org/images/products/" + str(one)+ "/" + str(two)+ "/" + str(three)+ "/" + str(four)+ "/" + "front_" + language + ".1.full.json"
	return "empty"

def get_nutrition_json_url(language,one,two,three,four,number):
	#"url_json_nutrition_" + language = "http://static.openfoodfacts.org/images/products/" + str(one)+ "/" + str(two)+ "/" + str(three)+ "/" + str(four)+ "/" + "nutrition_" + language + ".1.full.json"
	return "empty"

def get_ingredients_json_url(language,one,two,three,four,number):
	#"url_json_ingredients_" + language = "http://static.openfoodfacts.org/images/products/" + str(one)+ "/" + str(two)+ "/" + str(three)+ "/" + str(four)+ "/" + "ingredients_" + language + ".1.full.json"
	return "empty"

def make_slug_legible(slug):
	legible_slug = slug.replace("-", " ").replace("\n", " ").lower()
	return legible_slug

def get_random_product_from_json(url):
	# Fetch a random product
	raw_list_of_products = get_json_for_randomization(url)
	random_product = random.choice(raw_list_of_products['products'])
	return random_product

def parse_and_append(value_list, value_results, result1, result2, result3, result4):
	for i in value_list:
		if len(i['name']) > 3:
			value_name = make_slug_legible(i['name'])
			for result in (result1,result2,result3,result4):
				if value_name.lower() in result.lower():
					print "value_name"
					print value_name
					value_results.append(i['name'])
					print value_results


class AddCategoryRandomProduct(TemplateView):

	game = 'blablabla'
	if game == 'brands':
		template_name='hungergames/random_brand.html'
	elif game == 'labels':
		template_name='hungergames/random_labels.html'
	elif game == 'packager-codes':
		template_name='hungergames/random_packager-codes.html'
	elif game == 'categories':
		template_name='hungergames/random_category.html'
	else:
		template_name='hungergames/random_category.html'

	
	def get_context_data(self, **kwargs):
		context = super(AddCategoryRandomProduct, self).get_context_data(**kwargs)

		# Define a subset of eligible products
		game = 'blablabla'
		if game == 'brands':
			url = "http://world.openfoodfacts.org/state/brands-to-be-completed/entry-date/2015.json"
		elif game == 'labels':
			url = "http://world.openfoodfacts.org/state/labels-to-be-completed/entry-date/2015.json"
		elif game == 'packager-codes':
			url = "http://world.openfoodfacts.org/state/packager-codes-to-be-completed/entry-date/2015.json"
		elif game == 'categories':
			url = "http://world.openfoodfacts.org/state/categories-to-be-completed/entry-date/2015.json"
		else:
			url = "http://world.openfoodfacts.org/state/categories-to-be-completed/entry-date/2015.json"
		product = get_random_product_from_json(url)

		# Define result sets
		packaging_results = []
		packaging_codes_results = []
		categories_results = []
		ingredients_results = []
		labels_results = []
		brands_results = []
		quantity_results = []
		official_websites_results = []
		best_before_date_results = []
		stores_results = []
		traces_results = []
		serving_size_results = []
		energy_results = []
		fat_results = []
		saturated_fat_results = []
		carbohydrates_results = []
		sugars_results = []
		fiber_results = []
		proteins_results = []
		salt_results = []
		sodium_results = []
		alcohol_results = []
		carbon_footprint_results = []

		# Get product barcode
		product_barcode = product['code']
		# Get Product info and product edit link
		product_edit_url = get_edit_url_for_product(product_barcode)
		product_json_url = json.load(urllib.urlopen(get_json_url_for_product(product_barcode)))


		# Split the barcode into sections
		# Still buggy for non-normalized barcodes
		# Example : http://world.openfoodfacts.ovh/images/products/009/385/699/9789/1.json
		one = get_first_three_digits(product_barcode)
		two = get_second_three_digits(product_barcode)
		three = get_third_three_digits(product_barcode)
		four = get_fourth_three_digits(product_barcode)

		# Get JSON for raw images - Assumes 4 images - There can be more - or less
		# for language in languages:
		result1 = get_result(get_image_ocr_json(one, two, three, four, 1))
		result2 = get_result(get_image_ocr_json(one, two, three, four, 2))
		result3 = get_result(get_image_ocr_json(one, two, three, four, 3))
		result4 = get_result(get_image_ocr_json(one, two, three, four, 4))
		print result4
		print '-----------'
		print result3
		print '-----------'
		print result2
		print '-----------'
		print result1
		#category_list = dict()
		game = 'blablabla'
		if game == 'brands':
			# Parse brands
			brands_list == brands_list()
			parse_and_append(brands_list, brands_results, result1, result2, result3, result4)
		elif game == 'labels':
			# Parse labels
			labels_list == labels_list()
			parse_and_append(labels_list, labels_results, result1, result2, result3, result4)
		elif game == 'packager-codes':
			# Parse packaging codes
			packaging_codes_list == packaging_codes_list()
			parse_and_append(packaging_codes_list, packaging_codes_name, packaging_codes_results, result1, result2, result3, result4)
		elif game == 'ingredients':
			# Parse ingredients
			ingredients_list == ingredients_list()
			parse_and_append(ingredients_list, ingredients_name, ingredients_results, result1, result2, result3, result4)
		elif game == 'categories':
			# Parse categories

			category_list == category_list()
			parse_and_append(category_list, categories_results, result1, result2, result3, result4)
			parse_and_append(category_list, categories_results, get_categories(product_barcode), get_categories(product_barcode), get_categories(product_barcode), get_categories(product_barcode))
		else:
			# Parse categories
			global category_list
			category_list = categories_list(self)
			parse_and_append(category_list, categories_results, result1, result2, result3, result4)
	
			#category_list == category_list(self)
			parse_and_append(category_list, categories_results, result1, result2, result3, result4)

		context['categories_results'] = categories_results
		context['labels_results'] = labels_results
		context['brands_results'] = brands_results
		context['packaging_results'] = packaging_results
		context['packaging_codes_results'] = packaging_codes_results
		context['official_websites_results'] = official_websites_results
		context['best_before_date_results'] = best_before_date_results
		context['stores_results'] = stores_results
		context['traces_results'] = traces_results
		context['ingredients_results'] = ingredients_results
		context['serving_size_results'] = serving_size_results
		context['energy_results'] = energy_results
		context['fat_results'] = fat_results
		context['saturated_fat_results'] = saturated_fat_results
		context['carbohydrates_results'] = carbohydrates_results
		context['sugars_results'] = sugars_results
		context['fiber_results'] = fiber_results
		context['proteins_results'] = proteins_results
		context['salt_results'] = salt_results
		context['sodium_results'] = sodium_results
		context['alcohol_results'] = alcohol_results
		context['carbon_footprint_results'] = carbon_footprint_results

		context['product'] = product
		context['product_barcode'] = product_barcode
		context['product_edit_url'] = product_edit_url
		context['product_json_url'] = product_json_url
		return context

class ProductTemplateView(TemplateView):
	template_name='hungergames/product.html'

	def get_context_data(self, **kwargs):
		context = super(ProductTemplateView, self).get_context_data(**kwargs)

		# Define result sets
		packaging_results = []
		packaging_codes_results = []
		categories_results = []
		ingredients_results = []
		labels_results = []
		brands_results = []
		quantity_results = []
		official_websites_results = []
		best_before_date_results = []
		stores_results = []
		traces_results = []
		serving_size_results = []
		energy_results = []
		fat_results = []
		saturated_fat_results = []
		carbohydrates_results = []
		sugars_results = []
		fiber_results = []
		proteins_results = []
		salt_results = []
		sodium_results = []
		alcohol_results = []
		carbon_footprint_results = []

		# Define language
		language = "fr"
		# Define a subset of eligible products
		url = "http://world.openfoodfacts.org/state/labels-to-be-completed/entry-date/2015.json"

		# Get random product
		random_product = get_random_product_from_json(url)



		# Get cropped JSONs for ingredients, nutrition and front, in various languages
		# get_front_json_url(language,one,two,three,four,number)
		# get_ingredients_json_url(language,one,two,three,four,number)
		# get_nutrition_json_url(language,one,two,three,four,number)

		# Parse values
		#parse_and_append(value_list, value_name, value_results, result1, result2, result3, result4)

		# Parse quantities
		print "== Quantity =="
		for result in (result1,result2,result3,result4):
			quantity_results.append(re.findall(r"^([1-9][0-9]*)\s*(lbs|oz|g|kg|L)$", result)) #500g
		print quantity_results

		# Parse best_before_date
		# print "== Best Before Date =="
		# official_websites_results.append(re.findall(r'', result))
		# best_before_date_results.append(re.findall(r'\d\d\s(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\s\d{4}', result))
		# best_before_date_results.append(re.findall(r'\d\d\s(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)', result))
		# print best_before_date_results
		# Parse Stores
		# stores_results.append(re.findall(r'', result))
		# Parse Traces
		# traces_results.append(re.findall(r'', result))
		# Parse Serving Size
		# serving_size_results.append(re.findall(r'', result))
		# Parse Energy
		# energy_results.append(re.findall(r'', result)) 68 kcal
		# Parse Fat
		# fat_results.append(re.findall(r'', result))
		# Parse Saturated fat
		# saturated_fat_results.append(re.findall(r'', result))
		# Parse carbohydrates
		# carbohydrates_results.append(re.findall(r'', result))
		# Parse sugars
		# sugars_results.append(re.findall(r'', result))
		# Parse fiber
		# fiber_results.append(re.findall(r'', result))
		# Parse proteins
		# proteins_results.append(re.findall(r'', result))
		# Parse salt
		# salt_results.append(re.findall(r'', result))
		# Parse sodium
		# sodium_results.append(re.findall(r'', result))
		# Parse alcohol
		# alcohol_results.append(re.findall(r'', result))
		# Parse carbon_footprint
		# carbon_footprint_results.append(re.findall(r'', result))

		# jsonresp = mainPage.json()["responses"]
		# jsonlogo = jsonresp["logoAnnotations"]
		# print jsonlogo
		# logoAnnotations.description



		context['categories_results'] = categories_results
		context['labels_results'] = labels_results
		context['brands_results'] = brands_results
		context['packaging_results'] = packaging_results
		context['packaging_codes_results'] = packaging_codes_results

		context['official_websites_results'] = official_websites_results
		context['best_before_date_results'] = best_before_date_results
		context['stores_results'] = stores_results
		context['traces_results'] = traces_results
		context['ingredients_results'] = ingredients_results
		context['serving_size_results'] = serving_size_results
		context['energy_results'] = energy_results
		context['fat_results'] = fat_results
		context['saturated_fat_results'] = saturated_fat_results
		context['carbohydrates_results'] = carbohydrates_results
		context['sugars_results'] = sugars_results
		context['fiber_results'] = fiber_results
		context['proteins_results'] = proteins_results
		context['salt_results'] = salt_results
		context['sodium_results'] = sodium_results
		context['alcohol_results'] = alcohol_results
		context['carbon_footprint_results'] = carbon_footprint_results

		
		context['product'] = product
		context['product_barcode'] = barcode
		context['product_edit_url'] = product_edit_url
		context['product_json_url'] = product_json_url
		return context
		
		#3270720001541
		#http://world.openfoodfacts.ovh/images/products/3207200541.json
