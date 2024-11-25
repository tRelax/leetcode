from typing import List


class Solution:
    # crazy dumb by me but it works
    def trap(self, height: List[int]) -> int:
        l, r = 0, 1
        cur_area = 0
        l_h, r_h = 0, 0
        indx = 0
        cur_list = []
        while r < len(height):
            if height[l] == 0 and l_h == 0:
                l += 1
                r += 1
                continue
            l_h = height[l]
            r_h = height[r]

            if l_h > r_h:
                if len(cur_list) < indx + 1:
                    cur_list.append([l_h, r_h])
                else:
                    cur_list[indx].append(r_h)
            else:
                if len(cur_list) == indx + 1:
                    cur_list[indx].append(r_h)
                    indx += 1
                l = r

            r += 1
            if r == len(height):

                print(cur_list)
                if indx > len(cur_list) - 1:
                    indx = len(cur_list) - 1
                # 4 2 1 2 1
                while len(cur_list[indx]) >= 3:
                    if cur_list[indx][0] <= cur_list[indx][len(cur_list[indx]) - 1]:
                        break
                    elif min(cur_list[indx]) == cur_list[indx][len(cur_list[indx])-1]:
                        cur_list[indx].pop()
                    elif max(cur_list) == cur_list[0] and len(cur_list[indx]) != 3:
                        tmp_list = cur_list[indx][1:]
                        if max(tmp_list) != tmp_list[len(tmp_list) - 1]:
                            cur_list[indx].pop(0)
                        else:
                            break
                    else:
                        break

                print(cur_list)
                if len(cur_list[indx]) < 3:
                    cur_list.pop()
                elif cur_list[indx][0] > cur_list[indx][len(cur_list[indx]) - 1]:
                    cur_list[indx][0] = cur_list[indx][len(cur_list[indx]) - 1]
                print(cur_list)

        for l in cur_list:
            left_side = l[0]
            for i in range(1, len(l)):
                if left_side > l[i]:
                    cur_area += left_side - l[i]

        return cur_area

    # better solution
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        l_max, r_max = height[l], height[r]
        res = 0

        while l < r:
            if l_max < r_max:
                l += 1
                l_max = max(l_max, height[l])
                res += l_max - height[l]
            else:
                r -= 1
                r_max = max(r_max, height[r])
                res += r_max - height[r]
        return res


height = [0, 2, 0, 3, 1, 0, 1, 3, 2, 1]
# height = [0, 1, 1, 1, 0, 3]
# height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
# height = [2, 1, 0, 0]
height = [4, 2, 3]
height = [0, 7, 1, 4, 6]


print(Solution().trap(height))
