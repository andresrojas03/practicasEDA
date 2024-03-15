from Doubleq import deque

def main():
    dq = deque()
    
    dq.add_rear(4)
    dq.add_front(5)
    dq.add_front(7)
    dq.add_front(9)
    dq.add_rear(3)
    print(dq)
    dq.remove_front()
    dq.remove_rear()
    dq.peekrear()
    dq.peekfront()


if __name__ == "__main__":
    main()