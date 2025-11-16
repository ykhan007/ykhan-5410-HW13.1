****Markov Text Generator****

A simple Markov Chain based text generator created as part of my Algorithms coursework.
This project reads one or more text files, learns the word-patterns inside them, and generates new text that sounds similar to the original material.

**📌 Project Overview**

This project uses Markov chains to generate new text based on classic literature.
You provide any number of .txt files, choose a window size, temperature, and the number of words you want.
The program then creates a dictionary of word sequences and uses it to produce new, original text.

I tested the program using Alice in Wonderland and Pride and Prejudice, and the results were surprisingly close to the writing style of the books.

**📂 Features**

Load multiple text files at once
Adjustable window size (controls context strength)
Adjustable temperature (controls randomness)
Generates custom-length output
Works with any plain-text book or dataset
Fully interactive command-line interface

**🛠 How the Program Works**

Ask the user how many text files to load
Read and combine all files into one dataset
Build a Markov chain dictionary using the chosen window size
Generate text using probability and temperature settings
Print the final generated output
