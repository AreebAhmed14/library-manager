# Library manager
import os
import json

data_file = "data.json"

def load_data():
    if os.path.exists(data_file):
        with open(data_file, "r") as file:
            print(f"Data loaded from {data_file}")
            return json.load(file)
    return {"books": []}  # Return a dictionary with an empty books list

def save_data(data):
    with open(data_file, "w") as file:
        json.dump(data, file)

def add_book(data):
    try:
        title = input("Enter the title of the book: ").strip()
        author = input("Enter the author of the book: ").strip()
        year = input("Enter the year of the book: ").strip()
        
        # Validate year input
        if not year.isdigit():
            print("Error: Year must be a number!")
            return
            
        addbook = {
            "title": title,
            "author": author,
            "year": int(year)  # Convert year to integer
        }    
        data["books"].append(addbook)  # Append to the books list
        save_data(data)
        print(f"Book '{title}' by {author} added successfully.")
    except Exception as e:
        print(f"Error adding book: {e}")

def remove_book(data):
    title = input("Enter the title of the book to remove: ")
    for book in data["books"]:  # Access the books list
        if book["title"] == title:
            data["books"].remove(book)  # Remove from the books list
            save_data(data)
            print(f"Book '{title}' removed successfully.")
            return
    print(f"Book '{title}' not found.")

def search_book(data):
    title = input("Enter the title of the book to search for: ")
    for book in data["books"]:  # Access the books list
        if book["title"] == title:
            print(f"Book found: {book}")
            return
    print(f"Book '{title}' not found.")

def display_books(data):
    if not data["books"]:  # Check the books list
        print("No books available.")
    else:
        print("Books in the library:")
        for book in data["books"]:  # Access the books list
            print(f"Title: {book['title']}, Author: {book['author']}, Year: {book['year']}")

def main():
    data = load_data()
    while True:
        print("\nLibrary Management System")
        print("1. Add Book")
        print("2. Remove Book")
        print("3. Search Book")
        print("4. Display Books")
        print("5. Exit")

        choice = input("Enter your choice: ")
        if choice == "1":
            add_book(data)
        elif choice == "2":
            remove_book(data)
        elif choice == "3":
            search_book(data)
        elif choice == "4":
            display_books(data)
        elif choice == "5":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
        

            
        
