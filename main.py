import random

player_name = input("你好！请输入你的名字: ")

target_number = random.randint(1, 100)
guess = None
attempts = 0
max_attempts = 7
guess_history = []  # <--- 新增：用于存储猜测历史的列表

print(f"--- 好的, {player_name}! 猜数字游戏开始！ ---")
print(f"我已经想好了一个1到100之间的整数，你有 {max_attempts} 次机会！")

while guess != target_number and attempts < max_attempts:
    try:
        # --- 新增改动：在每次输入前，先显示历史记录 ---
        print(f"你已经猜过的数字: {guess_history}")  # <--- 新增

        guess = int(input("请输入你猜的数字: "))

        guess_history.append(guess)  # <--- 新增：把本次的猜测加入列表
        attempts += 1

        if guess > target_number:
            print("太大了！再猜小一点。")
        elif guess < target_number:
            print("太小了！再猜大一点。")
        else:
            print(f"恭喜你, {player_name}！在第 {attempts} 次就猜对了！我想的数字就是 {target_number}！")

    except ValueError:
        print("请输入一个有效的数字！")

if guess != target_number:
    print(f"很遗憾, {player_name}，你的机会用完了。我想的数字是 {target_number}。")

print("--- 游戏结束！ ---")