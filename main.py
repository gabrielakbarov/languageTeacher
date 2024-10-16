import csv
import random

# Pfad zur CSV-Datei
csv_file = 'data/aserbaidschanisch_worter.csv'

# Wörter aus der CSV-Datei laden
def load_words(file_path):
    with open(file_path, mode='r') as file:
        reader = csv.DictReader(file)
        return list(reader)

# Funktion, um ein zufälliges Wort abzufragen
def quiz_word(words):
    word = random.choice(words)
    print(f"Aserbaidschanisches Wort: {word['Aserbaidschanisch']}")
    input("Drücke Enter für die Übersetzung...")
    print(f"Deutsche Übersetzung: {word['Deutsch']}")
    print(f"Aussprache: {word['Aussprache']}")
    print(f"Wortart: {word['Wortart']}, Thema: {word['Thema']}")
    print("")

# Hauptfunktion, um das Quiz zu starten
def start_quiz():
    words = load_words(csv_file)
    while True:
        quiz_word(words)
        again = input("Möchtest du ein weiteres Wort? (j/n): ")
        if again.lower() != 'j':
            break

# Skript starten
if __name__ == "__main__":
    start_quiz()
