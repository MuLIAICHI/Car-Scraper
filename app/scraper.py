from bs4 import BeautifulSoup
import requests
import json

class Scraping:
    def __init__(self, gui) -> None:
        self.gui = gui

    def scrape_data(self, keyword, filename):
        data = []

        for pageNumber in range(1, 11):
            # Scrape the data
# Get the links of the pages
            websitePage = f'https://www.cars.com/shopping/results/?list_price_max=&makes[]={keyword}&maximum_distance=all&models[]=&page={pageNumber}&stock_type=new&zip='
            # Get the response for every single page
            response = requests.get(websitePage)
            # Get the Soup
            soup = BeautifulSoup(response.content, 'html.parser')
            # Find the vehicles on the page
            vehicles = soup.find_all('div', {'class': 'vehicle-card'})
            # Iterate through every single vehicle
            for vehicle in vehicles:
                try:
                    name = vehicle.find('h2', {'class': 'title'}).get_text()
                except:
                    name = 'NaN'
                try:
                    ratings = vehicle.find('span', {'class': 'sds-rating__count'}).get_text()
                except:
                    ratings = 'NaN'
                try:
                    rating_count = vehicle.find('span', {'class': 'sds-rating__link'}).get_text()[1:-1]
                except:
                    rating_count = 'NaN'
                try:
                    price = vehicle.find('span', {'class': 'primary-price'}).get_text()
                except:
                    price = 'NaN'
                try:
                    car_dealer = vehicle.find('div', {'class': 'dealer-name'}).get_text().strip()
                except:
                    car_dealer = 'NaN'
                car_data = {
                    'name': name,
                    'ratings': ratings,
                    'rating_count': rating_count,
                    'price': price,
                    'car_dealer': car_dealer
                }
                data.append(car_data)

        # Save the data to a JSON file
        with open(f'{filename}.json', 'w') as f:
            json.dump(data, f, indent=4)
        self.gui.show_completion()
