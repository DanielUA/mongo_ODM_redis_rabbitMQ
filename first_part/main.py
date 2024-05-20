import os
import sys
from cache import find_by_tag, find_by_author, find_by_tags

def main():
    while True:
        user_input = input("Введите команду: ")
        if user_input.lower() == 'exit':
            print("Завершение работы.")
            sys.exit(0)

        try:
            command, value = user_input.split(':')
            command = command.strip().lower()
            value = value.strip()
            
            if command == 'name':
                results = find_by_author(value)
                if results:
                    for author, quotes in results.items():
                        print(f"Цитаты от {author}:")
                        for quote in quotes:
                            print(f"- {quote}")
                else:
                    print(f"Цитаты автора {value} не найдены.")
            elif command == 'tag':
                results = find_by_tag(value)
                if results:
                    print(f"Цитаты с тегом {value}:")
                    for quote in results:
                        print(f"- {quote}")
                else:
                    print(f"Цитаты с тегом {value} не найдены.")
            elif command == 'tags':
                tags = value.split(',')
                results = find_by_tags(tags)
                if results:
                    print(f"Цитаты с тегами {', '.join(tags)}:")
                    for quote in results:
                        print(f"- {quote}")
                else:
                    print(f"Цитаты с тегами {', '.join(tags)} не найдены.")
            else:
                print("Неизвестная команда. Используйте 'name', 'tag', 'tags' или 'exit'.")
        except ValueError:
            print("Неправильный формат команды. Используйте команду в формате 'команда: значение'.")

if __name__ == "__main__":
    main()
