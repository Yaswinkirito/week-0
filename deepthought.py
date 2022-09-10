answer=input("What is the answer to The great question to Life, the Universe and Everything ? ")#promts user for an answer
if 42==answer or "forty two"==answer.lower().strip() or "forty-two"==answer.lower().strip():
    print("True")
else:
    print("False")