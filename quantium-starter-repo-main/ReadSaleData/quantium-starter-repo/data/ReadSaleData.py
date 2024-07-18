import csv

file_names = ['daily_sales_data_0.csv', 'daily_sales_data_1.csv', 'daily_sales_data_2.csv']
output_file = 'filtered_data_csv'
files_processed = 0

with open(output_file, mode='w', newline='') as output_csv:
    csv_writer = csv.writer(output_csv)
    # add a csv header
    header = ["sales", "date", "region"]

    for file in file_names:
        with open(file) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            for row in csv_reader:
                if line_count == 0:
                    print(f'Column names are {", ".join(row)}')
                    csv_writer.writerow(header)
                    line_count += 1
                elif row[0].lower() == 'pink morsel'.lower():
                    total_value = float(row[1].replace('$', '')) * int(row[2])
                    print(f'{row[0]}, {row[1]}, {row[2]}, {row[3]}, {row[4]}')
                    new_row = [total_value, row[3], row[4]]
                    csv_writer.writerow(new_row)
                    line_count += 1
            print(f'Processed {line_count} lines.')
        files_processed += 1
    print(f'Files processed = {files_processed}')