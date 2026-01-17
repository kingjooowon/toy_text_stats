import os
import string

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(BASE_DIR, "sample.txt")

with open (file_path, "r", encoding="utf-8") as f:  
    text = f.read()

def count_lines(): # 총 줄 수
    line_count = 0
    for i in text:
        if i == ("\n"):
            line_count += 1
        else:
            continue
    
    return line_count

def count_words(): # 총 단어 수
    word_count = 0
    words = text.lower()
    words = words.strip(string.punctuation)
    words = words.split()
    
    word_count = len(words)
    
    return word_count


def count_message(): # 총 글자 수(공백 미포함)
    message_count = 0
    messages = text.lower().strip(" ").strip("\n")
    message_count = len(messages)
    
    return message_count

def find_longest(): # 가장 긴 단어
    longest_word = ""
    words = text.lower().strip(string.punctuation).split()
    for i in range(len(words)):
        if len(words[i]) > len(longest_word):
            longest_word = words[i]
        else:
            continue
    
    return longest_word

def find_average_len(): # 평균 단어 길이
    len_avg = 0.0
    total = 0
    words = text.lower().strip(string.punctuation).split()
    for i in range(len(words)):
        total += len(words[i])
    
    len_avg = total / len(words)
    
    return len_avg

if __name__ == "__main__":
    total_lines = count_lines()
    total_words = count_words()
    total_messages = count_message()
    longest_word = find_longest()
    wordLen_avg = find_average_len()
    
    print(f"총 줄 수: {total_lines}\n총 단어 수: {total_words}\n총 글자 수: {total_messages}\n가장 긴 단어: {longest_word}\n평균 단어 길이: {wordLen_avg}")