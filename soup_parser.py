from bs4 import BeautifulSoup
from get_url import get_request

"""
Will extract the information required from the book from its page.

(Title, Price, Stars)

Input:
------
    url : str
        URL of the page of the book to be extracted the information
    

Output:
-------
    title, price, rank : (str, str, str)
            Tuple wiwth the information requested for the book

"""
def book_info_parse(url: str) -> tuple:
    resp = get_request(url)                                 #Get the HTTP response

    soup = BeautifulSoup(resp.content, "html.parser")       #Settup the HTML parser

    title = soup.h1.text                                    #Extracts the info required
    price = soup.find("p", {"class":"price_color"}).text
    rank = soup.find("p", {"class":"star-rating"}).get("class")[1]

    return title,price,rank


"""
Will receive the URL of the current page to be scrapped and extract the information from each of the books present in that current page.

Input:
------
    url : str
        URL from the current page to be scrapped

Output:
-------
    list_books_info: list
        List os tuples of all the books info from the page

"""
def soup_parser(url : str) -> list:
    list_books_info = []

    page_HTTP_response = get_request(url)
    soup = BeautifulSoup(page_HTTP_response.content, "html.parser") #Get the HTML content
    list_books_HTML = soup.section.ol.find_all('li')    #Get all the li elemnts (where all the books from the current page are listed)

    for book in list_books_HTML:
        book_url = "https://books.toscrape.com/catalogue/" + book.h3.a.get("href") #Get the link to the specific book page
        book_info = book_info_parse(book_url)   #Get the info requested from the current book
        print(book_info)
        list_books_info.append(book_info)       #Add the current book to the list of books

    return list_books_info