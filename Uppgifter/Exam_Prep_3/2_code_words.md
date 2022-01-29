Implement the function `code_words(text, dictionary)`, which takes as the first argument an arbitrary text as string, and returns a new version of the text where certain code words are replaced with other words. The second argument is the dictionary of code words.

For example:

```python
>>> d = {"happiness": "cake", "homework": "date"}
>>> print(code_words("you have your happiness", d))
you have your cake
>>> print(code_words("I have a homework today", d))
I have a date today                 
```

All words in the text are separated by spaces. Words that are not in the dictionary should be left unchanged.
