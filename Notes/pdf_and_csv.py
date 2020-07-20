import csv

data = open('files/example.csv', encoding='utf-8')
csv_data = csv.reader(data)
data_lines = list(csv_data)

all_emails = []

for line in data_lines[1:]:
    all_emails.append(line[3])

file_to_output = open('files/tos_save_file.csv', mode='w', newline='')
# In this case just append to the file
# file_to_output = open('files/tos_save_file.csv', mode='a', newline='')
csv_writer = csv.writer(file_to_output, delimiter=',')
csv_writer.writerow((['a', 'b', 'c']))
csv_writer.writerows((['a', 'b', 'c'], ['a', 'b', 'c'], ['a', 'b', 'c']))
file_to_output.close()
