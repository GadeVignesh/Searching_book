import requests

def search_book(title, api_key=None):
    base_url = "https://www.googleapis.com/books/v1/volumes"
    params = {"q": title}
    if api_key:
        params["key"] = api_key

    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        data = response.json()
        if "items" in data:
            book = data["items"][0]["volumeInfo"]
            print(f"Title: {book.get('title', 'N/A')}")
            print(f"Authors: {', '.join(book.get('authors', ['N/A']))}")
            print(f"Publisher: {book.get('publisher', 'N/A')}")
            print(f"Published Date: {book.get('publishedDate', 'N/A')}")
            print(f"Description: {book.get('description', 'N/A')}")
        else:
            print("No books found.")
    else:
        print(f"Error: {response.status_code}")

if __name__ == "__main__":
    book_title = input("Enter the book title: ")
    api_key = input("Enter your Google Books API key (leave blank to skip): ").strip() or None
    search_book(book_title, api_key)
