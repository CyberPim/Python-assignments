def search_text(text, nr_of_full_stops, nr_of_commas, nr_of_semicolons):
    for char in text:
        if char == ".":
            nr_of_full_stops[0] = (nr_of_full_stops[0] + 1)
        elif char == ",":
            nr_of_commas[0] = (nr_of_commas[0] + 1)
        elif char == ";":
            nr_of_semicolons[0] = (nr_of_semicolons[0] + 1)
   
    return True

nr_of_full_stops = [0]
nr_of_commas = [0]
nr_of_semicolons = [0]


text = str(input("Enter text: "))
search_text(text, nr_of_full_stops, nr_of_commas, nr_of_semicolons)
print(nr_of_full_stops + nr_of_commas + nr_of_semicolons)

