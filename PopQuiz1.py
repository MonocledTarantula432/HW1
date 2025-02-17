from utils import Queue


def hotPotato(names, count):
    q = Queue() #N
    for name in names:		#O(N)
        q.enqueue(name) # Initially, length = N - 1
    round = 1
    while q.size() > 1: # Simulates the rounds of the game #O(N)
        if round % 2 == 1:
            for i in range(count):  # Rotate the queue ‘count’ times #O(K)
                q.enqueue(q.dequeue())
        else:
            for i in range(0, count, -1):
                q.enqueue(q.dequeue())
        print('Round', round, ':', q.front(), "is eliminated.")
        round += 1
        q.dequeue() # Removed from the game

    return q.dequeue() #Returns the only remaining player from the queue

print('Winner:',hotPotato(["Bill","David","Susan","Jane","Kent","Brad"],5))
