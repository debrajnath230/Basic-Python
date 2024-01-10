import requests
from bs4 import BeautifulSoup

class PriceTracer:
    def __init__(self, url):
        self.url = url
        self.user_agent = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"}
        self.response = requests.get(url=self.url, headers=self.user_agent).text
        self.soup = BeautifulSoup(self.response, 'html.parser')

    def product_title(self):
        title = self.soup.find("span", {"class": "B_NuCI"})
        if title is not None:
            return title.text
        else:
            return "Tag not found"

    def product_price(self):
        price = self.soup.find("div", {"class": "_30jeq3 _16Jk6d"})
        if price is not None:
            return price.text
        else:
            return "Price not found"

# Example usage
device = PriceTracer(url="https://www.flipkart.com/fujifilm-x-series-x-t4-mirrorless-camera-body-only/p/itm6665b78dd1a1c?pid=DLLFSY4X95PUZVQD&lid=LSTDLLFSY4X95PUZVQDDWQQRK&marketplace=FLIPKART&store=jek%2Fp31%2Ftrv&srno=b_1_1&otracker=browse&fm=organic&iid=en_1Zx5lcgsorLIVhLl-zMhqSTsE6yon8WmB6DzJ-0-PmnmE6DD3eTgxfewY5kqo2XCq2wBGEQFx1WlAUrd-C9JUQ%3D%3D&ppt=hp&ppn=homepage&ssid=3qjzbcfyr40000001704384098757")

print(device.product_title())
print(device.product_price())
