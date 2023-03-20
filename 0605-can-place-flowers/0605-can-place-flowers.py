class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        canPlant = 0

        for i in range(len(flowerbed)):
            if canPlant == n:
                return True

            if flowerbed[i] == 0:
                left = (i == 0 or flowerbed[i-1] == 0)
                right = (i == len(flowerbed)-1 or flowerbed[i+1] == 0)

                if left and right:
                    flowerbed[i] = 1
                    canPlant += 1

        return canPlant == n