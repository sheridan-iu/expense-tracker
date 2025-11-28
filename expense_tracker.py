import csv
from collections import defaultdict

FILE = "expenses.csv"

# Ensure CSV exists
try:
    open(FILE, "r").close()
except FileNotFoundError:
    with open(FILE, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["amount", "category", "note"])


def add_expense(amount, category, note=""):
    with open(FILE, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([amount, category, note])
    print("✔ 已添加消费记录！")


def summary_by_category():
    data = defaultdict(float)
    with open(FILE, "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            data[row["category"]] += float(row["amount"])

    print("\n=== 按类别统计结果 ===")
    for cat, total in data.items():
        print(f"{cat}: {total} 元")


def main():
    while True:
        print("\n=== 消费统计小工具 ===")
        print("1. 添加一笔消费")
        print("2. 查看按类别统计的结果")
        print("3. 退出")

        choice = input("选择功能: ")

        if choice == "1":
            amount = input("金额: ")
            category = input("类别（如 食物/交通/购物）: ")
            note = input("备注（可选）: ")
            add_expense(amount, category, note)
        elif choice == "2":
            summary_by_category()
        elif choice == "3":
            print("再见！")
            break
        else:
            print("无效选项，请重新输入。")


if __name__ == "__main__":
    main()
