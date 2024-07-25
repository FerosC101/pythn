import random
import time

class TypingSpeedTest:
    def __init__(self):
        self.sentences = [
            "The quick brown fox jumps over the lazy dog.",
            "A journey of a thousand miles begins with a single step.",
            "To be or not to be, that is the question.",
            "All that glitters is not gold.",
            "She sells seashells by the seashore.",
            "How much wood would a woodchuck chuck if a woodchuck could chuck wood?",
            "I scream, you scream, we all scream for ice cream.",
            "Peter Piper picked a peck of pickled peppers.",
            "A watched pot never boils.",
            "Actions speak louder than words.",
            "Birds of a feather flock together.",
            "Beauty is in the eye of the beholder.",
            "Better late than never.",
            "Brevity is the soul of wit.",
            "Don't count your chickens before they hatch.",
            "Every cloud has a silver lining.",
            "Fortune favors the brave.",
            "Haste makes waste.",
            "If it ain't broke, don't fix it.",
            "It's no use crying over spilled milk.",
            "Laughter is the best medicine.",
            "Necessity is the mother of invention.",
            "The early bird catches the worm.",
            "There's no place like home.",
            "Time flies when you're having fun.",
            "Two heads are better than one.",
            "When in Rome, do as the Romans do.",
            "You can't judge a book by its cover.",
            "A penny saved is a penny earned.",
            "A picture is worth a thousand words.",
            "Absence makes the heart grow fonder.",
            "All's well that ends well.",
            "Beggars can't be choosers.",
            "Cleanliness is next to godliness.",
            "Don't bite the hand that feeds you.",
            "Don't put all your eggs in one basket.",
            "Every rose has its thorn.",
            "Familiarity breeds contempt.",
            "Good things come to those who wait.",
            "Honesty is the best policy.",
            "Ignorance is bliss.",
            "It takes two to tango.",
            "Keep your friends close and your enemies closer.",
            "Knowledge is power.",
            "Laughter is the best medicine.",
            "Let sleeping dogs lie.",
            "Money doesn't grow on trees.",
            "Necessity is the mother of invention.",
            "No man is an island.",
            "One good turn deserves another.",
            "Out of sight, out of mind.",
            "Practice makes perfect.",
            "Rome wasn't built in a day.",
            "Silence is golden.",
            "The pen is mightier than the sword.",
            "The proof of the pudding is in the eating.",
            "There's no time like the present.",
            "To err is human, to forgive divine.",
            "Too many cooks spoil the broth.",
            "Variety is the spice of life.",
            "When the going gets tough, the tough get going.",
            "You can't have your cake and eat it too.",
            "You can't make an omelette without breaking eggs.",
            "Your guess is as good as mine."
        ]

    def start_typing_test(self, user, mode, limit):
        if mode == 'time':
            self.typing_test_time(user, limit)
        elif mode == 'words':
            self.typing_test_words(user, limit)

    def typing_test_time(self, user, seconds):
        print(f"\nYou have {seconds} seconds to type the following sentence as fast as you can:")
        sentence = random.choice(self.sentences)
        print(sentence)
        start_time = time.time()
        user_input = self.get_timed_input(seconds)
        end_time = time.time()

        time_taken = end_time - start_time
        wpm = self.calculate_wpm(user_input, time_taken)
        accuracy = self.calculate_accuracy(sentence, user_input)
        print(f"Time taken: {time_taken:.2f} seconds")
        print(f"Words per minute: {wpm:.2f}")
        print(f"Accuracy: {accuracy:.2f}%")
        user.add_score(wpm)

    def typing_test_words(self, user, word_count):
        print(f"\nType the following {word_count} words as fast as you can:")
        sentence = ' '.join(random.choices(self.sentences, k=word_count))
        print(sentence)
        start_time = time.time()
        user_input = input()
        end_time = time.time()

        time_taken = end_time - start_time
        wpm = self.calculate_wpm(user_input, time_taken)
        accuracy = self.calculate_accuracy(sentence, user_input)
        print(f"Time taken: {time_taken:.2f} seconds")
        print(f"Words per minute: {wpm:.2f}")
        print(f"Accuracy: {accuracy:.2f}%")
        user.add_score(wpm)

    def get_timed_input(self, limit):
        print(f"Start typing (you have {limit} seconds):")
        start = time.time()
        user_input = []
        while time.time() - start < limit:
            user_input.append(input())
        return ' '.join(user_input)

    def calculate_wpm(self, user_input, time_taken):
        word_count = len(user_input.split())
        return (word_count / time_taken) * 60

    def calculate_accuracy(self, sentence, user_input):
        correct_chars = sum(1 for a, b in zip(sentence, user_input) if a == b)
        return (correct_chars / len(sentence)) * 100
