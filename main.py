from requests import get
# 
class Digikala:
    def __init__(self, kala):
        self.kala = kala
    # 
    def pager(self):
        # construct the URL for the API call
        total_page_url = f"https://api.digikala.com/v1/search/?q={self.kala}&page=1"
        # 
        # send the API request and parse the response JSON
        total_pages = get(url=total_page_url).json()['data']['pager'].get("total_pages")
        # 
        return total_pages
    # 
    # def dict_creator(self):
    #     names=[]
    #     for page in range(1, self.pager()+1):
    #         products = get(f"https://api.digikala.com/v1/search/?q={self.kala}&page={page}").json()['data'].get("products")
    #         for product in products:
    #             names.append(product.get("title_fa").strip())
    #     return names
    def dict_creator(self):
        names= (product.get("title_fa") for page in range(1, self.pager()+1) 
            for product in get(f"https://api.digikala.com/v1/search/?q={self.kala}&page={page}").json()['data'].get("products"))
        return tuple(names)

dk=Digikala(input("please enter ur search choice: "))
print(dk.dict_creator())
# 