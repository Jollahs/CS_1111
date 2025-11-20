def extract_important_lines():
    # Open the file for reading
    infile = open("notes.txt", "r")
    
    # Open a second file for writing
    outfile = open("important_notes.txt", "w")
    
    # Process each line
    for line in infile:
        if "IMPORTANT" in line:
            outfile.write(line)

    # Close both files!
    infile.close()
    outfile.close()


# Example call
extract_important_lines()
