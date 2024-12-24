from typing import List
import heapq
from collections import defaultdict


class Twitter:

    def __init__(self):
        self.tweetMap = defaultdict(list)
        self.followSet = defaultdict(set)
        self.count = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append([self.count, tweetId])
        self.count -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        ownFeed = []
        res = []
        self.followSet[userId].add(userId)
        for followeeId in self.followSet[userId]:
            if followeeId in self.tweetMap:
                for ft in self.tweetMap[followeeId]:
                    ownFeed.append(ft)
        heapq.heapify(ownFeed)
        while ownFeed:
            res.append(heapq.heappop(ownFeed)[1])
        return res[:10]

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followSet[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followSet[followerId]:
            self.followSet[followerId].remove(followeeId)


twitter = Twitter()
twitter.postTweet(1, 10)  # User 1 posts a new tweet with id = 10.
twitter.postTweet(2, 20)  # User 2 posts a new tweet with id = 20.
# User 1's news feed should only contain their own tweets -> [10].
twitter.getNewsFeed(1)
# User 2's news feed should only contain their own tweets -> [20].
twitter.getNewsFeed(2)
twitter.follow(1, 2)     # User 1 follows user 2.
# User 1's news feed should contain both tweets from user 1 and user 2 -> [20, 10].
twitter.getNewsFeed(1)
# User 2's news feed should still only contain their own tweets -> [20].
twitter.getNewsFeed(2)
twitter.unfollow(1, 2)   # User 1 follows user 2.
# User 1's news feed should only contain their own tweets -> [10].
twitter.getNewsFeed(1)

print("\n")

twitter = Twitter()
twitter.postTweet(1, 1)
twitter.postTweet(1, 2)
twitter.postTweet(1, 3)
twitter.postTweet(1, 4)
twitter.postTweet(1, 5)
twitter.postTweet(2, 6)
twitter.postTweet(2, 7)
twitter.follow(1, 2)
twitter.getNewsFeed(1)  # [7, 6, 5, 4, 3, 2, 1]
twitter.unfollow(1, 2)
twitter.follow(1, 2)
twitter.getNewsFeed(1)  # [7, 6, 5, 4, 3, 2, 1]
twitter.postTweet(2, 8)
twitter.getNewsFeed(1)  # [8, 7, 6, 5, 4, 3, 2, 1]
twitter.unfollow(1, 2)
twitter.getNewsFeed(1)  # [5, 4, 3, 2, 1]
twitter.follow(1, 2)
twitter.postTweet(1, 9)
twitter.postTweet(1, 10)
twitter.postTweet(1, 11)
twitter.getNewsFeed(1)  # [11, 10, 9, 8, 7, 6, 5, 4, 3, 2]
