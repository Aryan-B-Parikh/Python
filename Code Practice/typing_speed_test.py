import time
import random

sentences = [
    "The quick brown fox jumps over the lazy dog.",
    "Python makes programming fun and effective.",
    "Never stop learning because life never stops teaching.",
    "Discipline is the bridge between goals and accomplishment.",
    "Success is not in what you have, but who you are."
]

def typing_test():
    test_sentence = random.choice(sentences)
    print("\n🔥 Typing Speed Test 🔥")
    print("\nType the following sentence as fast as you can:\n")
    print(f"➡️  {test_sentence}\n")
    
    input("Press Enter when you're ready...")

    start = time.time()
    typed = input("\nStart typing: ")
    end = time.time()

    elapsed_time = round(end - start, 2)
    words = len(test_sentence.split())
    wpm = round((words / elapsed_time) * 60)

    print("\n⏱️ Time taken:", elapsed_time, "seconds")
    print("⚡ Words per minute (WPM):", wpm)

    if typed.strip() == test_sentence:
        print("✅ You typed it correctly!")
    else:
        print("❌ There were some mistakes in your typing.")

if __name__ == "__main__":
    typing_test()
