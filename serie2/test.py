from ColaD import CircularQ

def main():
    #size = 5
    p = CircularQ(5)

    p.enqueue(4)
    p.enqueue(5)
    p.enqueue(6)
    p.enqueue(7)
    p.enqueue(8)
    print(p)
    p.dequeue()
    print(p)
    p.dequeue()
    print(p)
    p.dequeue()
    print(p)
    p.dequeue()
    print(p)

if __name__ == "__main__":
    main()