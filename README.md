# TextAnalyzer

A command-line text analyzer built in Python. Type in any sentence and the program breaks it down across multiple dimensions — from basic stats to an interactive letter search.

## What it does

**Basic stats**
Counts total characters and total words in the input sentence.

**Case transformations**
Returns the sentence in uppercase, lowercase, and capitalized form.

**Vowel counter**
Iterates through the sentence, collects every vowel found, and returns both the list and the total count.

**Space counter**
Counts the number of whitespace characters in the sentence.

**Letter frequency search**
Drops into an interactive loop where you can search for any character and get back how many times it appears. Type `quit` to exit.

## How to run

Make sure you have Python 3+ installed, then:

```bash
python textanalyzer.py
```

No external libraries required.

## Example

```
Enter a sentence to analyze: Hello World

Total of characters: 11
Total of words: 2

Uppercase: HELLO WORLD
Lowercase: hello world
Capitalized: Hello world

Number of Vowels: 3
Vowels Found: ['e', 'o', 'o']

Number of Spaces: 1

Which letter should I count? (Type 'quit' to QUIT): l
The letter 'l' appears 3 times.
Sentence: Hello World

Which letter should I count? (Type 'quit' to QUIT): quit
Thanks for testing P8's text analyzer!
```

## Author

Eduardo Schneider (P8)
