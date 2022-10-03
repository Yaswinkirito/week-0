words=input("say something ?")
for word in words:
    if word.lower() in ["a","e","i","o","u"]:
        words=words.replace(word,"")
print(words)
