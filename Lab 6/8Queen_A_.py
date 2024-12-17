import heapq

def h(s):
  
    h = 0
    n = len(s)
    for i in range(n):
        for j in range(i + 1, n):
            if s[i] == s[j] or abs(s[i] - s[j]) == abs(i - j):
                h += 1
    return h

def a_star():
    initial_state = []
    q = []
    g = 8 
    heapq.heappush(q, (h(initial_state), initial_state, g))

    while q:
        f, state, g = heapq.heappop(q)

        if len(state) == 8 and h(state) == 0:
            return state

        for i in range(1, 9):
            if i not in state:  
                new_state = state + [i]
                heapq.heappush(q, (h(new_state) + g, new_state, g - 1))

    return None  

solution = a_star()
print("Solution:", solution)
