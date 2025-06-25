

def input_something(prompt):
    while True:
        value = input(prompt)
        if value.strip():
            return value
        else:
            print("Input cannot be empty or just whitespace.")

def input_int(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value >= 1:
                return value
            else:
                print("Please enter an integer greater than or equal to 1.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

def print_movie_list(data):
    if not data:
        print("No movies saved")
        return
    for index, movie in enumerate(data):
        print(f"{index + 1}) {movie['name']} ({movie['year']})")

movie_data = [
    { "name": "Forrest Gump", "year": 1994, "duration": 142, "genres": ["Drama", "Romance"] },
    { "name": "Avengers: Endgame", "year": 2019, "duration": 181, "genres": ["Action", "Adventure", "Drama"] },
    { "name": "Back to the Future", "year": 1985, "duration": 114, "genres": ["Adventure", "Comedy", "Sci-Fi"] }
]

print("Welcome to Movie Admin!")

while True:
    print("\nChoose [a]dd, [l]ist, [s]earch, [v]iew, [d]elete or [q]uit.")
    choice = input("Enter your choice: ").strip().lower()

    if choice == "a":
        name = input_something("Enter movie name: ")
        year = input_int("Enter release year: ")
        duration = input_int("Enter duration (in minutes): ")

        genres = []
        while True:
            genre = input_something("Enter a genre: ")
            genres.append(genre)
           
        if genres:
            movie = {
                "name": name,
                "year": year,
                "duration": duration,
                "genres": genres
            }
            movie_data.append(movie)
            print("Movie added successfully!")
        else:
            print("You must enter at least one genre.")

    elif choice == "l":
        print_movie_list(movie_data)

    elif choice == "s":
        if not movie_data:
            print("No movies saved")
            continue
        term = input_something("Enter search term: ").lower()
        found = False
        for index, movie in enumerate(movie_data):
            if term in movie['name'].lower():
                print(f"{index + 1}) {movie['name']} ({movie['year']})")
                found = True
        if not found:
            print("No matching movies found.")

    elif choice == "v":
        if not movie_data:
            print("No movies saved")
            continue
        index = input_int("Enter movie index number to view: ") - 1
        if 0 <= index < len(movie_data):
            movie = movie_data[index]
            print(f"\nName: {movie['name']}")
            print(f"Year: {movie['year']}")
            print(f"Duration: {movie['duration']} minutes")
            print("Genres:")
            for genre in movie["genres"]:
                print("-", genre)
        else:
            print("Invalid index number.")

    elif choice == "d":
        if not movie_data:
            print("No movies saved")
            continue
        index = input_int("Enter movie index number to delete: ") - 1
        if 0 <= index < len(movie_data):
            deleted = movie_data.pop(index)
            print(f"Deleted '{deleted['name']}' successfully.")
        else:
            print("Invalid index number.")

    elif choice == "q":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")
