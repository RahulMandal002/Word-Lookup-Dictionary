# 📜 Word Lookup Dictionary  

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)  
![Trie](https://img.shields.io/badge/Data%20Structure-Trie-green)  
![Edit Distance](https://img.shields.io/badge/Algorithm-Edit%20Distance-orange)  
![Web Scraping](https://img.shields.io/badge/Feature-Web%20Scraping-yellowgreen)  

## 🔍 Overview  
A **desktop-based dictionary application** for efficient English word lookup, spelling correction, and auto-suggestions. Built using advanced data structures and algorithms, this project demonstrates strong problem-solving skills and software development expertise.

## Tech Stack

- **Programming Language:** Python
- **Data Structures:** Trie (Prefix Tree)
- **Algorithms:** Edit Distance (Levenshtein Distance)
- **Libraries/Tools:** BeautifulSoup, Requests, Unittest
- **Version Control:** Git

---

## Features

1. **Efficient Word Search**

   - Implemented a **Trie data structure** for fast prefix-based word retrieval and validation.
   - Achieved **millisecond response times** even with large datasets.

2. **Spelling Correction & Auto-Suggestion**

   - Integrated **Levenshtein distance (edit distance)** algorithm to provide accurate spelling corrections.
   - Suggested valid words based on user input, improving user experience.

3. **Online Lookup via Web Scraping**

   - Used **BeautifulSoup** and **Requests** to scrape word definitions and examples from online dictionaries.
   - Handled dynamic content and ensured data accuracy through robust error handling.

4. **User-Friendly Interface**

   - Designed a simple **command-line interface (CLI)** for word lookup, spelling correction, and auto-suggestions.

---

## Project Structure

```
Word_Lookup_Dictionary/
├── data/
│   ├── word_list.txt  # Preloaded word list for Trie construction
├── src/
│   ├── main.py        # Main application logic
│   ├── trie.py        # Trie data structure implementation
│   ├── spell_correct.py # Spelling correction and auto-suggestion logic
│   ├── web_scraper.py  # Web scraping module for online lookup
├── tests/              # Unit tests for Trie, spell correction, and scraping
│   ├── test_trie.py
│   ├── test_spell_correct.py
│   ├── test_web_scraper.py
├── requirements.txt   # Python dependencies
├── README.md          # Project documentation
```

---

## How to Run

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/Word_Lookup_Dictionary.git
   cd Word_Lookup_Dictionary
   ```
2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
3. **Run the application:**
   ```bash
   python src/main.py
   ```
4. **Run unit tests:**
   ```bash
   python -m unittest tests/test_trie.py
   python -m unittest tests/test_spell_correct.py
   python -m unittest tests/test_web_scraper.py
   ```

---
## ScreenShot  
**Running Project Screen Shot**  
![Word Lookup Dictionary Screenshot1](screenshot1.png)
![Word Lookup Dictionary Screenshot2](screenshot2.png)

---
## Key Achievements

- **Optimized Performance:** Achieved **O(L)** time complexity for word search and prefix-based suggestions using Trie, where **L** is the length of the word.
- **Scalable Design:** Implemented a **modular architecture**, making it easy to extend features like adding new word sources or improving the scraping logic.
- **Robust Testing:** Wrote **comprehensive unit tests** to ensure the reliability of the Trie, spelling correction, and web scraping modules.

---

## Future Enhancements

- Add a **GUI** using **Tkinter or PyQt** for a more user-friendly experience.
- Integrate with **APIs (e.g., Oxford Dictionary API)** for more accurate and detailed definitions.
- Implement **caching** to store frequently searched words and improve performance.
- Add **support for multiple languages**.

---

## Contributing

Contributions are welcome! If you'd like to contribute, please follow these steps:

1. **Fork** the repository.
2. **Create a new branch** for your feature or bug fix.
3. **Submit a pull request** with a detailed description of your changes.

---

## License

This project is licensed under the **MIT License**. See the `LICENSE` file for details.

📌 **Like this project? Give it a ⭐ on GitHub!** 😊

---
## Connect with Me


- **LinkedIn:** [https://linkedin.com/in/rahul-mandal-b742a3210/](#)

- **GitHub:** [https://github.com/RahulMandal002/](#)  


