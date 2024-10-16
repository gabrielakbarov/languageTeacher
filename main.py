import csv
import random
import json

# Lade Strings aus der JSON-Datei
with open('strings/strings.json', 'r', encoding='utf-8') as f:
    strings = json.load(f)

csv_file = 'dict/aserbaidschanisch_worter_erweitert.csv'


def load_words(file_path):
    words = []
    with open(file_path, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            words.append(row)
    return words


def choose_topic():
    topics = ["Alltag", "Essen", "Reisen", "Tiere", "Bildung", "Smalltalk"]
    print(strings["choose_topic"])
    for i, topic in enumerate(topics, 1):
        print(f"{i}. {topic}")

    choice = int(input("Gib die Nummer des Themas ein: ")) - 1
    if 0 <= choice < len(topics):
        return topics[choice]
    else:
        print(strings["invalid_choice"])
        return strings["everyday-life"]


def quiz_word(topic_words, asked_words):
    if len(asked_words) == len(topic_words):
        print(strings["all_words_learned"])
        return True

    word = random.choice(topic_words)
    while word["Aserbaidschanisch"] in asked_words:
        word = random.choice(topic_words)

    asked_words.add(word["Aserbaidschanisch"])
    az_word = word["Aserbaidschanisch"]
    correct_answers = word["Deutsch"].split(",")
    user_answer = input(strings["ask_translation"].format(az_word)).strip().lower()


    if user_answer == 'q':
        return True

    if any(user_answer == answer.strip().lower() for answer in correct_answers):
        print(strings["correct_answer"])
    else:
        print(strings["wrong_answer"].format(correct_answers[0].strip()))  # Zeige die erste korrekte Antwort

    return False



def start_quiz():
    chosen_topic = choose_topic()
    if chosen_topic == "Smalltalk":
        csv_file = 'dict/smalltalk_sentences.csv'
    else:
        csv_file = 'dict/aserbaidschanisch_worter_erweitert.csv'

    words = load_words(csv_file)
    topic_words = [word for word in words if word["Thema"] == chosen_topic]

    if not topic_words:
        print(strings["no_words"].format(chosen_topic))
        return

    asked_words = set()

    while True:
        if quiz_word(topic_words, asked_words):
            break


if __name__ == "__main__":
    start_quiz()
