class Twitter:

    def __init__(self):
        self.feed_heap = []
        self.follow_map = {} # user -> users he follows mapping (set)
        self.global_time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        tweet = [-self.global_time, userId, tweetId] # negate for max-heap->most recent
        self.global_time+=1
        heapq.heappush(self.feed_heap, tweet) # based on timestamps (unique)

    def getNewsFeed(self, userId: int) -> List[int]:

        # now we want to pop our feed_heap
        our_feed = []
        put_back = []

        while len(our_feed)<10 and len(self.feed_heap)>0: #we don't want to pop on empty
            negtime, userid, tweetid = heapq.heappop(self.feed_heap)
            if (userId in self.follow_map.keys() and userid in self.follow_map[userId]) or userid==userId:
                our_feed.append(tweetid)
            put_back.append([negtime, userid, tweetid]) # we always put it back anyways
            # as we don't want this to be destructive
        for tweet in put_back:
            heapq.heappush(self.feed_heap, tweet) # putting everything back

        return our_feed

        

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.follow_map.keys():
            self.follow_map[followerId].add(followeeId)
        else:
            self.follow_map[followerId] = {followeeId}
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.follow_map.keys() and followeeId in self.follow_map[followerId]:
            self.follow_map[followerId].remove(followeeId)
        # we should always have a user
       

        
