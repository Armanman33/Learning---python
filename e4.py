import webbrowser

user_term = input("Enter a search term: ").replace(" ", "+") #for url

webbrowser.open("https://www.google.com/search?q=" + user_term)

