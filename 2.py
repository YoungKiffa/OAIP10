def main():
    parol = int(input('Введите пароль:'))
    for right in range(0, 100000):
        print(right)
        if right == parol:
            print('Пароль ВЗЛ0МАН:', right)
            break


if __name__ == "__main__":
    main()
