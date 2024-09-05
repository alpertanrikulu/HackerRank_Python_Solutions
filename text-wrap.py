import textwrap

def wrap(string, max_width):
    newString = []
    for i in range(0, len(string), max_width):
        if i + max_width <= len(string):
            newString.append(string[i:i+max_width])
        else:
            newString.append(string[i:i+(len(string) % max_width)])
    newString = "\n".join(newString)
    return newString

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
