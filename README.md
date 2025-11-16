Markov Text Generator

This project is a small Markov Text Generator I created for my Algorithms homework. The goal was to read multiple text files, build a Markov chain based on word sequences, and then generate new text that imitates the style of the original files.

I used classic books like Alice in Wonderland and Pride and Prejudice to test the generator. The program lets me choose how many files to combine, set a window size, change the temperature, and decide how many words to generate. It was interesting to see how the writing styles blend together.

How It Works

The program asks how many text files you want to load.

It reads all the files and combines them into one long string.

It builds a Markov dictionary based on the window size (the number of words in each state).

Using the dictionary and the temperature value, it generates new text word by word.

The output is a completely new piece of writing that still feels similar to the books used as input.

Features

Load any number of .txt files

Adjustable window size (controls how closely it follows the writing style)

Adjustable temperature (controls randomness)

Generates any number of words

Works with plain-text books from Gutenberg or your own files
