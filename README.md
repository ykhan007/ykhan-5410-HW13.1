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
were to do credit to her housekeeping, when an answer arrived which deferred it all. mr. bingley was good-looking and gentlemanlike: he had a pleasant countenance, and easy, unaffected manners. his sisters were fine women, with an air of great relief. “call the next witness.” and he added in an undertone to the queen, “really, my dear, you must indeed go and see mr. bingley when he comes into the neighbourhood.” “it will be no use to us, if twenty such should come, since you will not visit them.” “depend upon it, my dear, that when there are twenty, i will visit them all.” mr. bennet was so odd a mixture of quick parts, sarcastic humour, reserve, and caprice, that the experience of three-and-twenty years had been insufficient to{5} make his wife understand his character. her mind was less difficult to develope. she was a woman of mean understanding, little information, and uncertain temper. when she was nine feet high. “i wish i had our dinah here, i know i do!” said alice aloud, addressing nobody in particular. “she’d soon fetch it back!” “and who is dinah, if i might venture to ask the question?” said the lory. alice replied
----------------------

Generate again with new settings? (y/n):n
