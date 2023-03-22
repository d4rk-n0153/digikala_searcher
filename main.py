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
    
    def urls(self):
        urls_ = ("www.digikala.com"+str(product['url'].get("uri")) for page in range(1, self.pager() + 1)
                  for product in get(self.global_url+f"&page={page}").json()['data'].get("products"))

        return tuple(urls_)    
    def average_stars(self):
        stars_ = (product["data_layer"].get("dimension9") for page in range(1, self.pager() + 1)
                  for product in get(self.global_url+f"&page={page}").json()['data'].get("products"))

        return tuple(stars_)
    def total_scores(self):
        total_scores_ = (product["rating"].get("rate") for page in range(1, self.pager() + 1)
                  for product in get(self.global_url+f"&page={page}").json()['data'].get("products"))

        return tuple(total_scores_)
    def count_of_scores(self):
        total_scores_ = (product["rating"].get("count") for page in range(1, self.pager() + 1)
                  for product in get(self.global_url+f"&page={page}").json()['data'].get("products"))

        return tuple(total_scores_)
dk = Digikala(input("please enter ur search term: "))
print(f"totoal score is {dk.total_scores()}",f" count of scores is {dk.count_of_scores()}")