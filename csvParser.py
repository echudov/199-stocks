import csv

important_values = "importantValues.csv"
streak_data = "StreakData.csv"

important_values_fields = []
important_values_rows = []

streak_data_indicies = []
streak_data_rows = []


with open(important_values, 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    important_values_fields = next(csvreader)
    for row in csvreader:
        important_values_rows.append(row)

# creates dictionary of values to iterate through simulations
important_values_dict = dict();
for i in range(len(important_values_rows)):
    important_values_dict[important_values_rows[i][0]] = {important_values_fields[j]: important_values_rows[i][j]
                                                          for j in range(1, len(important_values_fields))}

with open(streak_data, 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    streak_data_indicies = next(csvreader)
    for row in csvreader:
        streak_data_rows.append(row)


def column(col, rows):
    return_column = []
    for j in range(len(rows)):
        if not (rows[j][col] == ''):
            return_column.append(rows[j][col])
    return return_column

streak_data_columns = []
for i in range(len(streak_data_indicies)):
    streak_data_columns.append(column(i, streak_data_rows))

# creates dictionary of lists (1 for each index to keep track of streaks)
streak_data_dict = dict()
for i in range(len(streak_data_indicies)):
    streak_data_dict[streak_data_indicies[i]] = streak_data_columns[i]

