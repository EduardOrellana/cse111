
def main():
    # Create and print a list named fruit.
    fruit_list = ["pear", "banana", "apple", "mango"]
    print(f"original: {fruit_list}")

    fruit_list.reverse()
    print(f"reverse: {fruit_list}")

    fruit_list.append("orange")
    print(f'with orange {fruit_list}')

    apple = fruit_list.index("apple")
    print(f'where is apple: {apple + 1}')

    fruit_list.remove('banana')
    print(f'without banana: {fruit_list}')

    fruit_list.pop()
    print(f'pop the last item: {fruit_list}')

    fruit_list.sort()
    print(f'Sorted list: {fruit_list}')

    fruit_list.clear()
    print(f'Clear the list: {fruit_list}')


if __name__ == "__main__":
    main()