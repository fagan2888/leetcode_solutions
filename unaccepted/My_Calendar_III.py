## https://leetcode.com/problems/my-calendar-iii/

## problem is to keep track of entries in a calendar, 
## and each time we add an entry, we return the largest number 
## of bookings on a single time.  

## for me, the hardest part is building a data-structure that
## can handle the calendar.  right now I'm just doing it with a
## list (where each time is an index), but even now as I write 
## up this explanation, that seems silly -- would be trivial to
## implement as a dictionary, which would make this much faster I think...

## however, when I do that, it actually comes out a little bit slower,
## by which I mean it fails on an earlier test case

class MyCalendarThree:

    def __init__(self):
        self.num_bookings = []
        self.max_K = 0
    
    def extend_num_bookings(self, n):
        while len(self.num_bookings) < n:
            self.num_bookings.append(0)
        

    def book(self, start: int, end: int) -> int:
        self.extend_num_bookings(end)
        for idx in range(start, end):
            self.num_bookings[idx] += 1
            if self.num_bookings[idx] > self.max_K:
                self.max_K = self.num_bookings[idx]

        return self.max_K
    

# Your MyCalendarThree object will be instantiated and called as such:
# obj = MyCalendarThree()
# param_1 = obj.book(start,end)