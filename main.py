from requests import get

class Digikala:
    def __init__(self, search_term):
        self.serch_term = search_term
        self.total_page_url = f"https://api.digikala.com/v1/search/?q={self.serch_term}&page=1"
        self.global_url=f"https://api.digikala.com/v1/search/?q={self.serch_term}"
    def pager(self):
        total_pages = get(url=self.total_page_url).json()['data']['pager'].get("total_pages")
        return total_pages

    def names(self):
        names_ = (product.get("title_fa") for page in range(1, self.pager() + 1)
                  for product in get(self.global_url+f"&page={page}").json()['data'].get("products"))

        return tuple(names_)
    
    def prices(self):
        ...

dk = Digikala(input("please enter ur search term: "))
print(dk.names())