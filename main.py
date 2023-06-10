import random


def main():
    # 長さ100の配列を作成
    my_array = list(range(1, 101))

    # 配列からランダムに1つ要素を選択
    selected_element = random.choice(my_array)
    random_integer = random.randint(1, 100)
    print(selected_element) # 結果を表示
    print(random_integer)

if __name__ == "__main__":
    main()