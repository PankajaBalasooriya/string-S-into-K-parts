# open file to read the string and inputs
file_name = input()
with open(file_name, "r") as input_file:
    s = input_file.readline()
    k = int(input_file.readline())

    s = s.replace("\n", "")
output = []
if len(s) % k == 0:
    for i in range(0, len(s) - k + 1, k):
        t = ""
        li_rep_index = []
        for j in range(0, k):
            t = t + s[i + j]
        for n in range(0, len(t)):
            for l in range(n + 1, len(t)):
                if t[n] == t[l]:
                    li_rep_index.append(l)
        li_rep_index = list(set(li_rep_index))
        ti = list(t)
        # for m in li_rep_index:
        ti.pop(li_rep_index)
        u = ""
        for p in ti:
            u += p
        output.append(u)


    with open("Output.txt", "w") as output_file:
        for ui in output:
            output_file.write(f"{ui}\n")

else:
    print("Invalid Input")
