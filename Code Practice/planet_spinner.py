import time
import os
planet_frames = [
    "🌍",
    "🌎",
    "🌏"
]
def spin_earth(delay=0.3, repeat=10):
    for _ in range(repeat):
        for frame in planet_frames:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Rotating Planet...\n")
            print(f"      {frame}")
            time.sleep(delay)
if __name__ == "__main__":
    spin_earth()