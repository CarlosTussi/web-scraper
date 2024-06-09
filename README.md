A python web craper to extract and analyze data from books from online sources. 

Data sourced from [Books to Scrape](https://books.toscrape.com/)

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Output](#output)

## Installation
*Python Version: 3.11.7*
1. Clone the repository
    ```sh
    git clone https://github.com/CarlosTussi/web-scraper.git
    ```
2. Change into the project directory
    ```sh
    cd web-scraper
    ```
3. (Recommended) Create a virtual environment
    ```sh
    python -m venv venv
    ```
4. (Recommended) Activate the virtual environment
    - On Windows:
      ```sh
      venv\Scripts\activate
      ```
    - On macOS and Linux:
      ```sh
      source venv/bin/activate
      ```
5. Install the required packages
    ```sh
    pip install -r requirements.txt
    ```

## Usage

Run the script indicating the number of pages to be scraped.

```sh
python .\scraper.py 2
```

## Output

CSV file ("books.csv") is generated with the following headers:
*  Title	- Price  - 	Stars

Each row will contain the relevant data for a book extracted from the website.

