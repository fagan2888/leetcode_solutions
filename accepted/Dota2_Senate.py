## https://leetcode.com/problems/dota2-senate/

## go through the rounds of voting, where a vote is to ban another
## senator or, if all senators of the other party are banned, delcare
## victory.

## the optimal play for each senator is to ban the first member of 
## the opposition party after them.  fastest way to handle that is to
## basically keep track of the number of bans that we have remaining
## to give out, noting that we'll always have bans from just one party.
## after all, the Ds will ban any Rs before they can vote if they have
## the chance to (and vice versa).  that means we can keep track of the 
## bans to give out using a single counter that can go positive for one 
## party and negative for the other.

## this solution is quite good, coming in at almost the 78th percentile
## for runtime and about the 50th percentile for memory.

class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        ## Ds add to this, Rs subtract
        ## so if > 0 and encouter an R, eliminate that R
        ## if > 0 and encounter another D, add another
        ## if < 0 and encounter a D, eliminate that D
        ## if < 0 and encounter another R, subtract another
        bans_to_proc = 0
        
        values = {'D': 1, 'R': - 1}

        ## go through rounds of voting until we have all one party
        while len(set(senate)) > 1:
            next_senate = ''
            for ii, char in enumerate(senate):
                if bans_to_proc == 0:
                    ## no bans from either party in the stack, so this character gets to 
                    ## ban the next of the opposition party and survives to the next round
                    next_senate += char
                    bans_to_proc += values[char]
                elif bans_to_proc > 0 and char == 'D':
                    ## no R bans to proc, so this character will ban the next R and survive
                    bans_to_proc += 1
                    next_senate += char
                elif bans_to_proc > 0 and char == 'R':
                    ## have an R ban to proc, so this character gets banned (but uses up a ban)
                    bans_to_proc -= 1
                    ## don't add this character to the next senate because it got banned 
                elif bans_to_proc < 0 and char == 'R':
                    ## no R bans to proc, so this character will ban the next D and survive
                    bans_to_proc -= 1
                    next_senate += char
                elif bans_to_proc < 0 and char == 'D':
                    ## have a D ban to proc, so proc it and ban this character
                    bans_to_proc += 1
                    ## again, got banned, so skip this character in the next senate
            senate = next_senate

        ## now we know we have all one party, so just return the party of the first senator
        if senate[0] == 'D':
            return 'Dire'
        else:
            return 'Radiant'