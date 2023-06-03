import csv
import json

# Etap 1: Pobierz dane testowe od użytkownika
names = []
missing_assignments = []
grades = []

for _ in range(3):
    name = input("Enter student's name: ")
    names.append(name)

    missing = int(input("Enter number of missing assignments: "))
    missing_assignments.append(missing)

    grade = int(input("Enter current grade: "))
    grades.append(grade)

# Etap 2: Utwórz plik CSV z danymi uczniów
file_path = "students.csv"

with open(file_path, "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Class", "First Name", "Last Name", "Missing Assignments", "Grade"])

    for name, missing, grade in zip(names, missing_assignments, grades):
        class_name = input("Enter student's class: ")
        last_name, first_name = name.split(" ")
        writer.writerow([class_name, first_name, last_name, missing, grade])

print(f"CSV file '{file_path}' created successfully.")

# Etap 3: Wczytaj dane z pliku CSV
def read_csv(file_path):
    names = []
    missing_assignments = []
    grades = []

    try:
        with open(file_path, "r") as file:
            reader = csv.reader(file)
            next(reader)  # Skip header row

            for row in reader:
                names.append(row[1] + " " + row[2])
                missing_assignments.append(int(row[3]))

                try:
                    grades.append(int(row[4]))
                except ValueError:
                    print(f"Invalid grade value for student {row[1]} {row[2]}")
                    grades.append(0)

        return names, missing_assignments, grades

    except FileNotFoundError:
        print(f"File {file_path} not found.")
        return None

data = read_csv(file_path)

if data is not None:
    names, missing_assignments, grades = data

    # Etap 4: Wygeneruj i wyświetl wiadomości
    def generate_message(names, missing_assignments, grades):
        with open("message.txt", "r") as file:
            message_template = file.read()

        for name, missing_assignment, grade in zip(names, missing_assignments, grades):
            potential_grade = grade + 1
            message = message_template.format(missing_assignment, grade, potential_grade)
            print(f"Sending message to {name}:")
            print(message)
            print("\n")

    generate_message(names, missing_assignments, grades)

# Dodatkowe zagadnienia: obsługa błędów, format JSON

# Przykład obsługi błędów
try:
    with open("nonexistent_file.txt", "r") as file:
        content = file.read()
    print(content)
except FileNotFoundError:
    print("File not found.")

# Przykład formatowania danych w formacie JSON
data = {
    "names": names,
    "missing_assignments": missing_assignments,
    "grades": grades
}

json_data = json.dumps(data)
print(json_data)
