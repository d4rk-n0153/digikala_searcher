from requests import get

class Digikala:
    def __init__(self, search_term:str):
        """
        Initializes a Digikala search object.
        :param search_term: The term to search in Digikala.
        """
        self.serch_term = search_term
        self.total_page_url = f"https://api.digikala.com/v1/search/?q={self.serch_term}&page=1"
        self.global_url=f"https://api.digikala.com/v1/search/?q={self.serch_term}"

    def pager(self) -> int:
        """
        Gets the total number of pages in the search results.
        :return: The total number of pages in the search results.
        """
        total_pages = get(url=self.total_page_url).json()['data']['pager'].get("total_pages")
        return total_pages

    def names(self) -> tuple:
        """
        Gets the names of the products from the search results.
        :return: A tuple containing the names of the products.
        """
        names_ = (product.get("title_fa") for page in range(1, self.pager() + 1)
                  for product in get(self.global_url+f"&page={page}").json()['data'].get("products"))
        return tuple(names_)

    def statuses(self) -> tuple:
        """
        Gets the statuses of the products from the search results.
        :return: A tuple containing the statuses of the products.
        """
        statuses_ = (product.get("status") for page in range(1, self.pager() + 1)
                  for product in get(self.global_url+f"&page={page}").json()['data'].get("products"))
        return tuple(statuses_)
    
    def urls(self) -> tuple:
        """
        Gets the urls of the products from the search results.
        :return: A tuple containing the urls of the products.
        """
        urls_ = ("www.digikala.com"+str(product['url'].get("uri")) for page in range(1, self.pager() + 1)
                  for product in get(self.global_url+f"&page={page}").json()['data'].get("products"))
        return tuple(urls_)   
    def prices(self) -> tuple:
        """
        Gets the prices of the products from the search results.
        :return: A tuple containing the prices of the products.
        """
        prices_ = ((product["default_variant"]["price"].get("selling_price")) for page in range(1, self.pager() + 1)
                  for product in get(self.global_url+f"&page={page}").json()['data'].get("products"))
        return tuple(prices_)
           
    # def average_stars(self):
    #     stars_ = (product["data_layer"].get("dimension9") for page in range(1, self.pager() + 1)
    #               for product in get(self.global_url+f"&page={page}").json()['data'].get("products"))

        # return tuple(stars_)
    def total_scores(self) -> tuple:
        """
        Gets the total scores of the products from the search results.
        :return: A tuple containing the total scores of the products.
        """
        total_scores_ = (product["rating"].get("rate") for page in range(1, self.pager() + 1)
                  for product in get(self.global_url+f"&page={page}").json()['data'].get("products"))

        return tuple(total_scores_)
    def count_of_scores(self) -> tuple:
        """
        Gets the number of scores for each product from the search results.
        :return: A tuple containing the number of scores for each product.
        """
        count_of_scores_ = (product["rating"].get("count") for page in range(1, self.pager() + 1)
                  for product in get(self.global_url+f"&page={page}").json()['data'].get("products"))

        return tuple(count_of_scores_)
