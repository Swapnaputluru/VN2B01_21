list = [1, 2, 3, 4, 5]
set = {"a for affection", "b for balancing", "c for caring", "d for depression", "e for ego", }
word = "Emotions"
result = zip(list, set, word)
final = tuple(result)
print(final)

list1, set1, word1 = zip(*final)
print(list1)
print(set1)
print(word)
