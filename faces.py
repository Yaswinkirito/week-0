def main():
    answer = input("say something \n")
    if ":)" in answer:
        answer = simile(answer)
    elif ":(" in answer:
        answer = sad(answer)
    print(answer)


def simile(go):
    go = go.replace(":)", " 🙂")
    return go


def sad(go):
    go = go.replace(":(", "🙁")
    return go


main()
