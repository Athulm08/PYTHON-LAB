def copy_odd_lines(input_file, output_file):
    try:
        with open(input_file, 'r') as infile:
            with open(output_file, 'w') as outfile:
                for line_num, line in enumerate(infile, start=1):
                    if line_num % 2 != 0:
                        outfile.write(line)
        print("Odd lines have been copied successfully.")
    except FileNotFoundError:
        print(f"Error: The file {input_file} does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")
input_file = 'test.txt'
output_file = 'text1.txt'
copy_odd_lines(input_file, output_file)

test.txt

hey
hello
how r u.....:)
