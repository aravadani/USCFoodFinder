from bs4 import BeautifulSoup
from datetime import date
import requests

search_term = str("Tater Tots")
MUrl = "https://hospitality.usc.edu/residential-dining-menus//?menu_venue=venue-27229&menu_date="
PUrl = "https://hospitality.usc.edu/residential-dining-menus//?menu_venue=venue-518&menu_date="
EUrl = "https://hospitality.usc.edu/residential-dining-menus//?menu_venue=venue-514&menu_date="

def main():
	today = date.today()
	print(today)
	check1 = result(MUrl + str(today))
	check2 = result(PUrl + str(today))
	check3 = result(EUrl + str(today))
	if check1:
		print(search_term + " @ The Village!")
	if check2:
		print(search_term + " @ Parkside!")
	if check3:
		print(search_term + " @ EVK!")
	if check1 == False and check2 == False and check3 == False:
		print("No Chicken Tenders Today :(")

	return 0

def result(URL):
	check = False;

	r = requests.get(URL)
	soup = BeautifulSoup(r.content, 'html5lib')

	columns=[] # a list to store all the different food sections
	table = soup.find('div', attrs = {'class':'fw-accordion-content dining-location-accordion row'})

	for row in table.findAll('li'):
		text = row.find(text=True, recursive=False)
		#print(text)
		if search_term in text:
			check = True
			break

	return check



if __name__ == "__main__":
	main()