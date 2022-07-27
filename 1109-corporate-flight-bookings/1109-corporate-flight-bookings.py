class Solution:
    def corpFlightBookings(self, bookings, n):
        res = [0] * (n + 1)
        print(bookings)
        for i, j, k in bookings:
            res[i - 1] += k
            res[j] -= k
        print(res)
        for i in range(1, n):
            res[i] += res[i - 1]
        print(res)
        return res[:-1]
