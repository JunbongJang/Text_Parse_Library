# Author: Junbong Jang
# Date: 5/17/2019

# transform the string containing all the problem set ids
# from one line into multiple lines.

infile_name = "../ASSISTmentsResearch/input_string.txt"
outfile_name = "../ASSISTmentsResearch/output_string.txt"

with open(outfile_name, 'w') as outfile, open(infile_name, 'r', encoding='utf-8') as infile:
    file_contents = infile.read()
    problem_ids = file_contents.split(',')

    counter = 0
    transformed_string = ""
    for problem_id in problem_ids:
        problem_id = problem_id.strip()
        if counter % 2 == 0:
            transformed_string += problem_id + ", "
        else:
            transformed_string += problem_id + "," + '\n'
        counter += 1

    outfile.write(transformed_string[0:len(transformed_string)-2])
