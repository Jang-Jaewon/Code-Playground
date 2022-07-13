class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        sum_account = [sum(account) for account in accounts]
        return max(sum_account)
            