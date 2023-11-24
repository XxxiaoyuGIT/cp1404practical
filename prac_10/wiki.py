import wikipedia
def main():
    while True:
        title = input("Enter a page title or search phrase: ")
        #If the input is an empty string, it indicates that the user wishes to exit the program and break out of the loop.
        if not title:
            break
        try:
            # Attempt to obtain Wikipedia page object with specified title
            page = wikipedia.page(title, auto_suggest=False) #Disable automatic redirection suggestions.
            print("Title:", page.title)
            print("Summary:", wikipedia.summary(title))
            print("URL:", page.url)

        # Disable automatic redirection suggestion to capture ambiguous errors in Wikipedia and prompt users to provide more specific queries.
        # First handle specific types of exceptions, and then handle more general exceptions.
        except wikipedia.DisambiguationError as e:
            print("Disambiguation error:", e.options)

        # Capture page not found error, notify user that page does not exist
        except wikipedia.PageError:
            print("Page not found.")

        # Capture other possible exceptions.
        except Exception as e:
            print("An error occurred:", e)

if __name__ == "__main__":
    main()