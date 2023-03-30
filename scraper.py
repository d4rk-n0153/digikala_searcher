from requests import get
from concurrent.futures import ThreadPoolExecutor

class Digikala:
    def __init__(self, search_term: str):
        """
        Initializes a Digikala search object.
        :param search_term: The term to search in Digikala.
        """
        self.search_term = search_term
        self.global_url = f"https://api.digikala.com/v1/search/?q={self.search_term}"

    def get_products(self, page_num):
        """
        Gets the products on a specific page of the search results.
        :param page_num: The page number of the search results to retrieve.
        :return: A list containing the products on the specified page.
        """
        url = f"{self.global_url}&page={page_num}"
        response = get(url)
        products = response.json()['data']['products']
        return products

    def pager(self) -> int:
        """
        Gets the total number of pages in the search results.
        :return: The total number of pages in the search results.
        """
        total_pages = get(url=f"{self.global_url}&page=1").json()['data']['pager'].get("total_pages")
        return int(total_pages)

    def names(self) -> tuple:
        """
        Gets the names of the products from the search results.
        :return: A tuple containing the names of the products.
        """
        with ThreadPoolExecutor(max_workers=5) as executor:
            products = list(executor.map(self.get_products, range(1, self.pager() + 1)))
        names_ = tuple(product.get("title_fa") for page in products for product in page)
        return names_

    def statuses(self) -> tuple:
        """
        Gets the statuses of the products from the search results.
        :return: A tuple containing the statuses of the products.
        """
        with ThreadPoolExecutor(max_workers=5) as executor:
            products = list(executor.map(self.get_products, range(1, self.pager() + 1)))
        statuses_ = tuple(product.get("status") for page in products for product in page)
        return statuses_

    def urls(self) -> tuple:
        """
        Gets the urls of the products from the search results.
        :return: A tuple containing the urls of the products.
        """
        with ThreadPoolExecutor(max_workers=5) as executor:
            products = list(executor.map(self.get_products, range(1, self.pager() + 1)))
        urls_ = tuple("www.digikala.com" + str(product['url'].get("uri")) for page in products for product in page)
        return urls_

    def prices(self) -> tuple:
        """
        Gets the prices of the products from the search results.
        :return: A tuple containing the prices of the products.
        """
        with ThreadPoolExecutor(max_workers=5) as executor:
            products = list(executor.map(self.get_products, range(1, self.pager() + 1)))
        prices_ = tuple(int(product["default_variant"]["price"].get("selling_price"))/10 if product.get("status") == "marketable" else 0 for page in products for product in page )
        return prices_

    def total_scores(self) -> tuple:
        """
        Gets the total scores of the products from the search results.
        :return: A tuple containing the total scores of the products.
        """
        with ThreadPoolExecutor(max_workers=5) as executor:
            products = list(executor.map(self.get_products, range(1, self.pager() + 1)))
        total_scores_ = tuple(product["rating"].get("rate") for page in products for product in page)
        return total_scores_

    def count_of_scores(self) -> tuple:
        """
        Gets the number of scores for each product from the search results.
        :return: A tuple containing the number of scores for each product.
        """
        with ThreadPoolExecutor(max_workers=5) as executor:
            products = list(executor.map(self.get_products, range(1, self.pager() + 1)))
        count_of_scores_ = tuple(product["rating"].get("count") for page in products for product in page)
        return count_of_scores_
