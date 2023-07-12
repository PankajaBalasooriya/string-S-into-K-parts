def split_string(s, k):
    lst = []
    for i in range(0, len(s) - k + 1, k):
        t = ""
        for j in range(0, k):
            t = t + s[i + j]
        lst.append(t)
    return lst


def remove_duplicates(str):
    str = list(str)
    for l in range(0, len(str)):
        for m in range(l + 1, len(str)):
            if str[l] == str[m]:
                str.pop(m)
                return remove_duplicates(str)
    return str

# open file to read the string and inputs
file_name = input()
with open(file_name, "r") as input_file:
    string = input_file.readline()
    length = int(input_file.readline())

    string = string.replace("\n", "")

if len(string) % length == 0:
    strings = split_string(string, length)

    with open("Output.txt", "w") as output_file:
        for strn in strings:
            u = ""
            for p in remove_duplicates(strn):
                u += p
            output_file.write(f"{u}\n")


else:
    print("Invalid Input")


