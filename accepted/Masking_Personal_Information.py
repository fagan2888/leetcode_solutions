## https://leetcode.com/problems/masking-personal-information/

## not really sure why this is a medium -- really just some string manipulation

## handle the email and phone number separately depending on whether or not we 
## have an @ symbol in our string.  for phone, strip anything that's not a digit
## then figure out whether we have a country code or not based on the number of 
## characters, and treat accordingly

## surprisingly, this simple solution comes in at ~87th percentile for runtime
## (though only ~9th percentile for memory for some reason?  guess other people 
## are doing it in-place)

class Solution:
    def maskPII(self, S: str) -> str:
        if '@' in S:
            S = S.lower()
            bef, aft = S.split('@')
            out = S[0] + '*'*5 + bef[-1]+'@'+aft
        else:
            ## remove non-numeric characters
            S = S.replace('-', '').replace('+', '').replace('(', '').replace(')', '').replace(' ', '')
            last_four = S[-4:]
            if len(S) > 10:
                country_code = '+' + '*'*(len(S)-10) + '-'
            else:
                country_code = ''
            out = country_code + '*'*3 + '-' + '*'*3 + '-' + last_four
        return out
                