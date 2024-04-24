import requests as req

"""
This functions returns the HTTP response from the requested URL

Input:
------
    url : str
        The url we are trying to reach

Output:
-------
    resp: requests.Response
        The request response from the website

"""

def get_request(url : str) -> req.Response: 
    resp = req.get(url)

    if(resp.status_code != 200):            #Informs the user if there's an error
        print(str(resp.status_code) + " - Error connecting to website")

    return resp


if __name__ == "__main__":
    print(get_request("https://books.toscrape.com/index.html"))
    get_request("https://books.toscrape.com/xxindex.html")
    