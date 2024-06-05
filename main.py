import os
import threading

def count_vowels(file_path):
    vowels = "aeiouAEIOU"
    count = 0
    with open(file_path, 'r') as file:
        for line in file:
            for char in line:
                if char in vowels:
                    count += 1
    print(f"{file_path}: {count} vowels")

def main():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    
    txt_files = [f for f in os.listdir(current_dir) if f.endswith('.txt')]
    
    threads = []
    for txt_file in txt_files:
        file_path = os.path.join(current_dir, txt_file)
        thread = threading.Thread(target=count_vowels, args=(file_path,))
        threads.append(thread)
        thread.start()
    
    for thread in threads:
        thread.join()

if __name__ == "__main__":
    main()
