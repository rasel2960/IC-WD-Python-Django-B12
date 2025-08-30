from pathlib import Path

def count_words(path):
    # Count the approximate number of words in a file.

    try:
        contents = path.read_text(encoding="utf-8")
    except FileNotFoundError:
        pass
        # print(f"Sorry, the file {path.name} does not exist.")
    else:
        # count the approximate number of words in the file
        words = contents.split()
        num_words = len(words)
        print(f"The file {path.name} has {num_words} words.")


file_names = ['text_files/alice.txt', 'text_files/hadi.txt', 'text_files/long-doc.txt', 'text_files/ascii-art.txt']
for file_name in file_names:
    path = Path(file_name)
    count_words(path)

# folder = Path('text_files')
# files = folder.glob('*.txt')
#
# for word in files:
#     count_words(word)
