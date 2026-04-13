sentence=input("enter sentence:")
d={"store":"shop","car":"bike"}
for word,new_word in d.items():
    sentence=sentence.replace(word,new_word)
print(sentence)
