def is_clap_number(number, clap_digit):
    return number % clap_digit == 0 or str(clap_digit) in str(number)

def generate_clap_sequence(clap_digit):
    sequence = []
    for number in range(1, 101):
        if is_clap_number(number, clap_digit):
            sequence.append("Clap")
        else:
            sequence.append(str(number))
    return sequence

# 讀取輸入
clap_digit = int(input())

# 生成拍手序列
clap_sequence = generate_clap_sequence(clap_digit)

# 分行輸出拍手序列
for i in range(0, 100, 10):
    print(" ".join(clap_sequence[i:i+10]))
