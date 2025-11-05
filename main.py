import random

target_number = random.randint(1, 100)
guess = None
attempts = 0
max_attempts = 7  # 最多可以猜7次

print("--- 猜数字游戏开始！ ---")
print(f"我已经想好了一个1到100之间的整数，你有 {max_attempts} 次机会！")

while guess != target_number and attempts < max_attempts:
    try:
        guess = int(input("请输入你猜的数字: "))
        attempts += 1  # 尝试次数加1

        if guess > target_number:
            print("太大了！再猜小一点。")
        elif guess < target_number:
            print("太小了！再猜大一点。")
        else:
            print(f"恭喜你，在第 {attempts} 次就猜对了！我想的数字就是 {target_number}！")

    except ValueError:
        print("请输入一个有效的数字！")

# 如果循环结束还没猜对，说明机会用完了
if guess != target_number:
    print(f"很遗憾，你的机会用完了。我想的数字是 {target_number}。")

print("--- 游戏结束！ ---")