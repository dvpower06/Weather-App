import requests
from bs4 import BeautifulSoup

class Weather:

    def __init__(self, city):
        self.city = city.lower().replace(" ", "-")
        url = f'https://www.timeanddate.com/weather/portugal/{self.city}'
        self.response = requests.get(url)
        self.soup = BeautifulSoup(self.response.text, 'html.parser')
        self.temperature = ""
        self.description = ""
   


    def getWeather(self):     
            self.temperature = self.soup.find('div', class_='h2').get_text(strip=True)
            self.description = self.soup.find('div', class_='h2').find_next('p').get_text(strip=True)

    def cityExists(self):
            try:
                self.getWeather()
            except AttributeError:
                return False
            return True
    


    def run(self):
            self.getWeather()
            print(f"Weather in {self.city}:")
            print(f"Temperature: {self.temperature}")
            print(f"Condition: {self.description}")
          

if __name__ == "__main__":
    
        weather_app = Weather("lsfs")
        weather_app.run()
    
    