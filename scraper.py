from get_url import get_request
from soup_parser import soup_parser
import csv
import sys

if __name__ == "__main__":
    #Get Request from the website
        num_pages = int(sys.argv[1])                          #Number of pages to be scrapped

        fp = open("books.csv", "w", newline="")          #Create a CSV file, making sure no extra \n is added
        csvwriter = csv.writer(fp)                       #Create CSV object. (csvwriter will handle the writes)
        header = ['Title', 'Price', 'Stars']             #Add a header
        csvwriter.writerow(header)                      

        for i in range(1,num_pages+1):                  #Scrap each of the pages requested
            books = soup_parser(f'https://books.toscrape.com/catalogue/page-{i}.html')
            csvwriter.writerows(books)                  #Write multiple elements from a lisst


        fp.close()
    