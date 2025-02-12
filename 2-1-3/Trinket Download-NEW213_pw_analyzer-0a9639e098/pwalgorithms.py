# Module pwalgorithms
import numbers


# get words from password dictionary file
def get_dictionary():
  words = []
  dictionary_file = open("dictionary.txt")
  for line in dictionary_file:
    # store word, omitting trailing new-line
    words.append(line[:-1])
  dictionary_file.close()
  return words

# analyze a one-word password
def one_word(password):
  words = get_dictionary()
  guesses = 0
  # get each word from the dictionary file
  for w in words:
    guesses += 1
    if (w == password):
      return True, guesses
  return False, guesses

# analyze a one-word password
def two_word(password):
  words = get_dictionary()
  guesses = 0
  # get each word from the dictionary file
  for w in words:
    for h in words:
      guesses += 1
      if (w+h == password):
        return True, guesses
  return False, guesses

def two_word_and_digit(password):
  numbers = [0,1,2,3,4,5,6,7,8,9]
  words = get_dictionary()
  guesses = 0
  # get each word from the dictionary file
  for w in words:
    for h in words:
      for n in numbers:
        guesses += 1
        if (w+h+str(n) == password):
          return True, guesses
        if (str(n)+ w + h == password):
          return True, guesses
  return False, guesses