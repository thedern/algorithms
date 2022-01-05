from call_stack_class import Stack


def create_stack():
    return Stack()


def main():
    stack = create_stack()
    stack.push(12)
    stack.push(13)
    stack.push(2)
    print(f'stack size {stack.size()}')
    print(f'last item: {stack.peek()}')
    print(f'stack is empty: {stack.is_empty()}')
    print(f'stack contains: {stack.display()}')
    stack.pop()
    print(f'stack size {stack.size()}')
    print(f'last item: {stack.peek()}')
    print(f'stack contains: {stack.display()}')


if __name__ == "__main__":
    main()

