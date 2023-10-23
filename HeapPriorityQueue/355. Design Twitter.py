from typing import List
from collections import defaultdict
class Twitter:
    def __init__(self):
        self.feed = []
        self.following  = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.feed.append([userId,tweetId])

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        for i in range(len(self.feed)-1,-1,-1):
            tweet = self.feed[i]
            if tweet[0] == userId or tweet[0] in self.following[userId]:
                res.append(tweet[1])
                if len(res) == 10: break
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].discard(followeeId)
        


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)