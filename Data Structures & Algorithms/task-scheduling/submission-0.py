class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # maybe we should have a sort of running time variable, and store in a hashtable 
        # the last time called to compute the delta, but this would be worst case O(cat)

        # we could have cat queues and pop accordingly to each queue's cooldown
        # but we would have to search all queues every time which would run in 
        # O(cat*m)

        # the actual solution is a bi-datastructure solution, where we keep both a 
        # max heap, to always know the most frequent element, as greedly picking the 
        # most frequent elment here actually optimizes the rounds

        t=0

        # we first need to count (A to Z)

        counts = [0]*26

        for task in tasks:
            counts[ord(task)-ord('A')]+=1

        # counting
    
        heap = [[-freq,chr(char+ord('A'))] for freq,char in zip(counts,range(len(counts))) if freq>0 ]
        # to make sure we don't get all the 0 freq chars
        # making sure to put freqs first and negative for max-heap
        heapq.heapify(heap)
        # and now, we greadily want to select the most frequent element, consume it, and put
        # it in the queue and add the elements that are now back available from the 
        # waiting queue
        waiting_queue = deque()
        t = 0
        while len(heap)>0 or len(waiting_queue)>0:
            t+=1 # we ran a cpu cycle to consume one of the best
            if len(heap)>0:
                negfreq, char = heapq.heappop(heap)
                if negfreq+1!=0: # to not add emptied out kinds
                    waiting_queue.append([t+n, negfreq+1, char]) # we add it to the queue
            # and the freeing time is t+n
            # and now we free from 'jail' all freable processes
            while len(waiting_queue)>0:
                if waiting_queue[0][0]==t:
                    _, negfreq, char = waiting_queue.popleft()
                    if negfreq == 0: continue # it means the element is gone
                    heapq.heappush(heap, [negfreq, char]) # pushing back free element
                else: # all elements in the queue are older and hence have no shot at being
                    # liberable
                    break
            # end of cycle
        return t
            

        

        

        