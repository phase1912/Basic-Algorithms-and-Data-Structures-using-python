from linked_list import LinkedList

def main():
    try:
        llist = LinkedList()

        # Вставляємо вузли в початок
        llist.insert_at_beginning(5)
        llist.insert_at_beginning(10)
        llist.insert_at_beginning(15)

        # Вставляємо вузли в кінець
        llist.insert_at_end(20)
        llist.insert_at_end(25)

        # Друк зв'язного списку
        print("Зв'язний список:")
        llist.print_list()

        # Видаляємо вузол
        llist.delete_node(10)

        print("\nЗв'язний список після видалення вузла з даними 10:")
        llist.print_list()

        # Пошук елемента у зв'язному списку
        print("\nШукаємо елемент 15:")
        element = llist.search_element(15)
        if element:
            print(element.data)

        print("\nРеверс списку:")
        llist.reverse_list()
        llist.print_list()

        print("\nСортування")
        llist.sort_list()
        llist.print_list()

        llist2 = LinkedList()

        # Вставляємо вузли в початок
        llist2.insert_at_beginning(30)
        llist2.insert_at_beginning(40)
        llist2.insert_at_beginning(50)
        llist2.sort_list()

        print("\nЗлиття")
        llist.merge_sorted_lists(llist2)
        llist.print_list()

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()