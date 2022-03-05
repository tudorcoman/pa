
def makeCircularPermutations(word):
    return [word[i:] + word[:i] for i in range(len(word))]

sir = input()
print(makeCircularPermutations(sir)) 
