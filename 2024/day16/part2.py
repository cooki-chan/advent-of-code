import queue
input = open('day16/inp.txt').read().split('\n')

tiles = set()
start = ()
end = ()

E = 1+0j
S = 0+1j
N = 0-1j
W  = -1+0j

for y, i in enumerate(input):
    for x, j in enumerate(i):
        match j:
            case ".":
                tiles.add(complex(x, y))
            case "E":
                end = complex(x,y)
            case "S":
                start = (0, complex(x,y))
                tiles.add(complex(x, y))

q = queue.PriorityQueue()

q.put(start)

while q.not_full:




