
# Python Program to Capitalize First Letter of Each Word in a File

def capitalize_file_words(filename):
    try:
        with open(filename, 'r') as file:
            for line in file:
                print(line.title(), end='')
    except FileNotFoundError:
        print(f"File '{filename}' not found.")

if __name__ == "__main__":
    filename = input("Enter the filename: ")
    capitalize_file_words(filename)