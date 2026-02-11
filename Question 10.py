def find_lines_containing(filename, keyword):
    # List for keyword matches
    matches = []

    # Opens the file safely
    with open(filename,"r",encoding="utf-8") as file:
        for line_number, line in enumerate(file, start=1):
            if keyword.lower() in line.lower():
                matches.append((line_number, line.strip()))

    return matches




