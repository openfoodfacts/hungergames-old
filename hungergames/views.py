from django.shortcuts import render

# Create your views here.
import json
import random
import requests
import webbrowser
from django.views.generic import TemplateView
import urllib
import re

class CategoryGameTemplateView(TemplateView):
	template_name='hungergames/categorygame.html'

	def get_context_data(self, **kwargs):
		context = super(CategoryGameTemplateView, self).get_context_data(**kwargs)

		# Get Parsing corpora

		traces = json.load(urllib.urlopen("http://world.openfoodfacts.org/traces.json"))
		ingredients = json.load(urllib.urlopen("http://world.openfoodfacts.org/ingredients.json"))
		stores = json.load(urllib.urlopen("http://world.openfoodfacts.org/stores.json"))
		packaging_codes = json.load(urllib.urlopen("http://world.openfoodfacts.org/packager-codes.json"))
		packagings = json.load(urllib.urlopen("http://world.openfoodfacts.org/packaging.json"))
		brands = json.load(urllib.urlopen("http://world.openfoodfacts.org/brands.json"))
		labels = json.load(urllib.urlopen("http://world.openfoodfacts.org/labels.json"))
		categories = json.load(urllib.urlopen("http://world.openfoodfacts.org/categories.json"))
		allergens = json.load(urllib.urlopen("http://world.openfoodfacts.org/allergens.json"))
		additives = json.load(urllib.urlopen("http://world.openfoodfacts.org/additives.json"))
		countries = json.load(urllib.urlopen("http://world.openfoodfacts.org/countries.json"))
		purchase_places = json.load(urllib.urlopen("http://world.openfoodfacts.org/purchase-places.json"))
		states = json.load(urllib.urlopen("http://world.openfoodfacts.org/states.json"))

		# Define a subset of eligible products
		#url = "http://world.openfoodfacts.org/state/categories-to-be-completed.json"
		url = "http://world.openfoodfacts.org/state/categories-to-be-completed/entry-date/2015.json"

		# Fetch a random product
		header = {'x-requested-with': 'XMLHttpRequest'}
		mainPage = requests.get(url, headers = header)
		jsonette = mainPage.json()
		jr = random.choice (jsonette['products'])

		# Get Product info and product edit link
		url_edit_product = "http://world.openfoodfacts.org/cgi/product.pl?type=edit&code=" + str(jr['code'])
		print "http://world.openfoodfacts.ovh/images/products/" + str(jr['code'])
		product = json.load(urllib.urlopen("http://world.openfoodfacts.org/api/v0/product/"+ str(jr['code']) +".json"))
		print product

		# Split the barcode into sections - Still buggy for non-normalized barcodes
		# http://world.openfoodfacts.ovh/images/products/009/385/699/9789/1.json

		four = jr['code'][9:13]
		three = jr['code'][6:9]
		two = jr['code'][3:6]
		one = jr['code'][0:3]
		context['code'] = jr['code']

		language = "fr"

		# Get JSON for raw images - Assumes 4 images - There can be more - or less

		urljson = "http://world.openfoodfacts.ovh/images/products/" + str(one)+ "/" + str(two)+ "/" + str(three)+ "/" + str(four)+ "/" + "1.json"
		urljson1 = "http://world.openfoodfacts.ovh/images/products/" + str(one)+ "/" + str(two)+ "/" + str(three)+ "/" + str(four)+ "/" + "1.json"
		urljson2 = "http://world.openfoodfacts.ovh/images/products/" + str(one)+ "/" + str(two)+ "/" + str(three)+ "/" + str(four)+ "/" + "2.json"
		urljson3 = "http://world.openfoodfacts.ovh/images/products/" + str(one)+ "/" + str(two)+ "/" + str(three)+ "/" + str(four)+ "/" + "3.json"
		urljson4 = "http://world.openfoodfacts.ovh/images/products/" + str(one)+ "/" + str(two)+ "/" + str(three)+ "/" + str(four)+ "/" + "4.json"

		context['urljson1'] = urljson1
		context['urljson2'] = urljson2
		context['urljson3'] = urljson3
		context['urljson4'] = urljson4

		# Get cropped JSONs for ingredients, nutrition and front, in various languages
		for language in languages:
			"url_json_front_" + language = "http://static.openfoodfacts.org/images/products/" + str(one)+ "/" + str(two)+ "/" + str(three)+ "/" + str(four)+ "/" + "front_" + language + ".1.full.json"
			"url_json_nutrition_" + language = "http://static.openfoodfacts.org/images/products/" + str(one)+ "/" + str(two)+ "/" + str(three)+ "/" + str(four)+ "/" + "nutrition_" + language + ".1.full.json"
			"url_json_ingredients_" + language = "http://static.openfoodfacts.org/images/products/" + str(one)+ "/" + str(two)+ "/" + str(three)+ "/" + str(four)+ "/" + "ingredients_" + language + ".1.full.json"

		if requests.get(urljson1) == 404:
			result1 = ""
		else:
			#result1 = requests.get(urljson1).text.replace("\n", " ").replace("-", " ").lower()
			result1 = json.load(urllib.urlopen(urljson1))
		if requests.get(urljson2) == 404:
			result2 = ""
		else:
			#result2 = requests.get(urljson2).text.replace("\n", " ").replace("-", " ").lower()
			result2 = json.load(urllib.urlopen(urljson2))
		if requests.get(urljson3) == 404:
			result3 = ""
		else:
			#result3 = requests.get(urljson3).text.replace("\n", " ").replace("-", " ").lower()
			result3 = json.load(urllib.urlopen(urljson3))
		if requests.get(urljson4) == 404:
			result4 = ""
		else:
			#result4 = requests.get(urljson4).text.replace("\n", " ").replace("-", " ").lower()
			result4 = json.load(urllib.urlopen(urljson4))


		context['result1'] = result1
		context['result2'] = result2
		context['result3'] = result3
		context['result4'] = result4

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


		packaging_list = packagings['tags']
		packaging_codes_list = packaging_codes['tags']
		categories_list = categories['tags']
		ingredients_list = ingredients['tags']
		labels_list = labels['tags']
		brands_list = brands['tags']

		# quantity_list = quantity['tags']
		# official_websites_list = official_websites['tags']
		# best_before_date_list = best_before_date['tags']
		stores_list = stores['tags']
		traces_list = traces['tags']
		# serving_size_list = serving_size['tags']
		# energy_list = energy['tags']
		# fat_list = fat['tags']
		# saturated_fat_list = saturated_fat['tags']
		# carbohydrates_list = carbohydrates['tags']
		# sugars_list = sugars['tags']
		# fiber_list = fiber['tags']
		# proteins_list = proteins['tags']
		# salt_list = salt['tags']
		# sodium_list = sodium['tags']
		# alcohol_list = alcohol['tags']
		# carbon_footprint_list = carbon_footprint['tags']
		allergens_list = allergens['tags']
		additives_list = additives['tags']
		countries_list = countries['tags']
		purchase_places_list = purchase_places['tags']



		# Parse Packaging
		print "== Packaging =="
		for i in packaging_list:
			if len(i['name']) > 3:
				packaging_name = i['name'].replace("-", " ").lower()
				for result in (result1,result2,result3,result4):
					if packaging_name.lower() in result:
						print i['name']
						packaging_results.append(i['name'])


		# Parse Packaging codes
		print "== Packaging Codes =="
		for i in packaging_codes_list:
			if len(i['name']) > 3:
				packaging_codes_name = i['name'].replace("-", " ").lower()
				for result in (result1,result2,result3,result4):
					if packaging_codes_name.lower() in result:
						print i['name']
						packaging_codes_results.append(i['name'])


		# Parse categories
		print "== Categories =="
		for i in categories_list:			
			if len(i['name']) > 3:
				category_name = i['name'].replace("-", " ").lower()
				for result in (result1,result2,result3,result4):
					if category_name in result:
						print i['name']
						categories_results.append(i['name'])
		
		# Parse ingredients
		print "== Ingredients =="
		for i in ingredients_list:
			if len(i['name']) > 3:
				ingredients_name = i['name'].replace("-", " ").lower()
				for result in (result1,result2,result3,result4):
					if ingredients_name in result:
						print i['name']
						ingredients_results.append(i['name'])

		# Parse labels
		print "== Labels =="
		for i in labels_list:
			if len(i['name']) > 3:
				lab_name = i['name'].replace("-", " ").lower()
				for result in (result1,result2,result3,result4):
					if lab_name in result:
						print i['name']
						labels_results.append(i['name'])
		
		# Parse brands
		print "== Brands =="

		for i in brands_list:
			if len(i['name']) > 3:
				brand_name = i['name'].replace("-", " ").lower()
				for result in (result1,result2,result3,result4):
					if brand_name in result:
						print i['name']
						brands_results.append(i['name'])

		# Parse quantities
		print "== Quantity =="
		for result in (result1,result2,result3,result4):
			quantity_results.append(re.findall(r"^([1-9][0-9]*)\s*(lbs|oz|g|kg|L)$", result)) #500g
		print quantity_results

		# Parse best_before_date
		print "== best before date =="
			# official_websites_results.append(re.findall(r'', result))
			best_before_date_results.append(re.findall(r'\d\d\s(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\s\d{4}', result))
			best_before_date_results.append(re.findall(r'\d\d\s(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)', result))
			print best_before_date_results

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
		#logoAnnotations.description

		context['product'] = product

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

		context['urloff'] = url_edit_product
		context['urljson'] = urljson
		return context
		
		#3270720001541
		#http://world.openfoodfacts.ovh/images/products/3207200541.json