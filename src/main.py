from trie import Trie
from spell_correct import SpellCorrector
from web_scraper import WebScraper

def load_words_from_file(file_path):
    with open(file_path, "r") as file:
        return [word.strip() for word in file.readlines()]

def main():
    # Initialize Trie and load words
    trie = Trie()
    words = load_words_from_file("data/word_list.txt")
    for word in words:
        trie.insert(word)

    # Initialize SpellCorrector and WebScraper
    spell_corrector = SpellCorrector(trie)
    web_scraper = WebScraper()

    while True:
        print("\n1. Search Word\n2. Spelling Correction\n3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            word = input("Enter a word to search: ")
            if trie.search(word):
                print(f"'{word}' is a valid word.")
                definition = web_scraper.lookup_definition(word)
                print(f"Definition{definition}")
            else:
                print(f"'{word}' is not a valid word.")
                suggestions = spell_corrector.correct_spelling(word)
                if suggestions:
                    print("Did you mean:", ", ".join(suggestions))

        elif choice == "2":
            word = input("Enter a word for spelling correction: ")
            suggestions = spell_corrector.correct_spelling(word)
            if suggestions:
                print("Suggestions:", ", ".join(suggestions))
            else:
                print("No suggestions found.")

        elif choice == "3":
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()