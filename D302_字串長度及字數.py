def count_words(string):
    words = string.split()
    return len(words)

# 讀取輸入的字串
string = input()

# 輸出字串的長度
print(len(string))

# 輸出字串中單詞的數目
print(count_words(string))