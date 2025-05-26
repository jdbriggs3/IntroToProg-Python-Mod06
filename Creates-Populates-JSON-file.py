import json

FILE_NAME = "Enrollments.json"

# Define your data (list of student records)
json_data = [
    {"FirstName": "Bob", "LastName": "Smith", "CourseName": "Python 100"},
    {"FirstName": "Sue", "LastName": "Jones", "CourseName":"Python 100"}
]

# Write the JSON data to the file
file_obj = open(FILE_NAME, 'w')
json.dump(json_data, file_obj, indent=2)
file_obj.close()