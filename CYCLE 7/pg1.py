def read_file_to_list(file_name):
    lines_list = []
    with open(file_name, 'r') as file:
        for line in file:
            lines_list.append(line.strip())
    return lines_list

file_name = 'test.txt'
lines = read_file_to_list(file_name)
print(lines)

test.txt

hey
hello
how r u.....:)
