file_path = r"C:\Users\Mateusz\Desktop\Python_projects\Project 1\lesson_4_files\some_text.txt"

with open(file_path, "r") as file:
    print(file)
    print(file.readline())
    
    lines = file.readlines()
    print(lines)
    for line_number, line in enumerate(lines):
        print(line_number, line.count("a"))
    