from requests import get

class Digikala:
    def __init__(self, kala):
        self.kala = kala
    
    def pager(self):
        # construct the URL for the API call
        total_page_url = f"https://api.digikala.com/v1/search/?q={self.kala}&page=1"
        
        # send the API request and parse the response JSON
        total_pages = get(url=total_page_url).json()['data']['pager'].get("total_pages")
        
        return total_pages
    
    def dict_creator(self):
        ...

dk=Digikala(input("please enter ur search choice: "))
print(dk.pager())