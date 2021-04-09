import itertools
import string

letters = list(string.ascii_letters)
for L in range(0, len(letters)+1):
  for subset in itertools.combinations(letters, L):
    print("".join(subset))
