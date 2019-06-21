## https://leetcode.com/problems/course-schedule-ii/submissions/

## ok so we have a number of courses we need to take (0 - N-1), 
## each of which may or may not have prereqs.  my solution is to
## make use of sets for rapid checking of in/out of set, and then
## continuing to try to add any classes that have had all of their
## prerequisites met.

## this isn't particularly fast since it's really the totally brute
## force solution, but it's fast enough.  comes in at 5th percentile,
## though it is quite memory efficient at 74th percentile there.

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        ## let's take a second to transform our list of pairs into a much more useful dictionary
        prereqs = {n: [] for n in range(numCourses)}
        for pr in prerequisites:
            prereqs[pr[0]].append(pr[1])

        ## now prereqs[ii] gives a list of the courses I must complete before
        ## doing course ii
            
        ## first find any courses without prereqs
        course_schedule = [n for n in prereqs if not len(prereqs[n])]

        ## keep of an unorded set (for quick lookup) of the courses
        ## that I've completed and those I have left to complete
        completed_courses = set(course_schedule)
        incompleted_courses = set(range(numCourses)) - completed_courses
        
        ## not loop until I either force myself to break or until I build
        ## up a complete course schedule
        while len(course_schedule) < numCourses:
            ## find which courses I haven't taken that I can take (i.e. all prereqs are done)
            ## order of these is irrelevant
            courses_i_can_now_take = set([n for n in incompleted_courses if False not in [c in completed_courses for c in prereqs[n]]])
            
            ## if I coulnd't take any courses this time around (and remember that I know
            ## that I have courses left to take in general), then I hit a deadend and 
            ## return an empty list
            if not len(courses_i_can_now_take):
                return []

            ## extend my course schedule, remove from the incomplete courses, and 
            ## union with my complete courses
            course_schedule.extend(courses_i_can_now_take)
            incompleted_courses = incompleted_courses - courses_i_can_now_take
            completed_courses |= courses_i_can_now_take
            
        return course_schedule