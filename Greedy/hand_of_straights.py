from typing import List


class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        hand.sort()
        hand_dict = {}
        for card in hand:
            hand_dict[card] = hand_dict.get(card, 0) + 1

        for card in hand:
            if hand_dict[card] == 0:
                continue

            for i in range(groupSize):
                if hand_dict.get(card + i, 0) == 0:
                    return False
                hand_dict[card + i] -= 1

        return True


hand = [1, 2, 4, 2, 3, 5, 3, 4]  # [1,2,2,3,3,4,4,5] -> [1,2,3,4], [2,3,4,5]
groupSize = 4
print(Solution().isNStraightHand(hand, groupSize))  # True

# [1,2,3,3,4,5,6,7] -> [1,2,3,4], [3, X] -> False
hand = [1, 2, 3, 3, 4, 5, 6, 7]
groupSize = 4
print(Solution().isNStraightHand(hand, groupSize))  # False
