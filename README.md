# Markov Text Generator

A simple Markov Chain based text generator created for my Algorithms coursework.  
This project reads one or more text files, learns the word-pattern patterns inside them, and generates new text that sounds similar to the original writing style.

---

## 📌 Project Overview

This project uses **Markov chains** to generate text based on any plain-text dataset.  
You can load multiple `.txt` files, choose a window size, temperature, and word count.  
The program then builds a Markov dictionary and produces new text using probability-based selection.

I tested the project with **Alice in Wonderland** and **Pride and Prejudice**, and the generated output came out surprisingly similar to the style of those books.

---

## 📂 Features

- Load **multiple text files** at once  
- Adjustable **window size** (context depth)  
- Adjustable **temperature** (randomness control)  
- Generate **custom-length** text  
- Works with **any** text file  
- Fully interactive command-line interface  

---

## 🛠 How the Program Works

1. Ask the user how many text files to load  
2. Read and combine all the text into one dataset  
3. Build a Markov chain dictionary using the selected window size  
4. Generate words based on temperature and probability  
5. Print the final generated output  

---

## 📝 Example Output

Below is the exact output generated from my test run:

Please enter a number.
How many text files to combine? 2
Path for file #1: alice.txt
Path for file #2: pride_and_prejudice.txt
Window size (e.g., 2 or 3): 3
Temperature (0 to 1): 0.6
How many words to generate? 200

--- Generated Text ---
playing against herself, for this curious child was very fond of them.”</p> <p>this accounted to elizabeth for the indulgence of some music. miss bingley moved with alacrity to the pianoforte, and after a minute or two sobs choked his voice. “same as if he felt that life could furnish nothing greater. he carved and ate and praised with delighted alacrity; and every dish was commended first by him, and then by a little curiosity, satisfied herself with walking to the window and pretending not to hear. in a doleful voice mrs. bennet thus began the projected conversation:—</p> <p>“oh, mr. collins!”</p> <p>“my dear madam,” replied he, “let us be for ever silent on this point. far be it from me, my dear sir, my gratitude is warmly excited by such affectionate attention; and, depend upon it, he means to be but little at netherfield, it would be insupportable. your sisters are engaged, and there is not another woman in the world <i>two</i> men over whom mr. darcy could not have. here again i shall give you pain—to what degree you only can tell. but whatever may be the possibility of meeting mr. darcy, while viewing the place, instantly occurred. it would

Generate again with new settings? (y/n): n
