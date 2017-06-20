#Python program that accepts a word from the user and reverse it

word = input("Enter any word : ")
result=list(word)
result.reverse()
print("Reversed result is :",''.join(result))