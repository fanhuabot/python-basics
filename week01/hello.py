"""第 1 周练习：第一个 Python 脚本。

运行：python week01/hello.py
"""

from datetime import date


def main() -> None:
    name = "fanhua"
    today = date.today()

    print("=" * 32)
    print(f"你好，{name}")
    print(f"今天是 {today:%Y 年 %m 月 %d 日}")
    print("=" * 32)

    # 小练习：把下面的占位换成你自己的答案
    print("\n本周目标：")
    goals = [
        "装好 Python 和 VS Code",
        "写出第一个能跑的程序",
        "学会 add / commit / push",
    ]
    for i, goal in enumerate(goals, start=1):
        print(f"  {i}. {goal}")

    # 小练习：改成一个简单的计算
    a, b = 3, 5
    print(f"\n顺手算一下：{a} + {b} = {a + b}")


if __name__ == "__main__":
    main()
