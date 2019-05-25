## https://leetcode.com/problems/unique-email-addresses/

## goal is to find the number of unique email addresses, given 
## some rules for simplifying a given email address.

## solution is to write a function to sanitize a single 
## email address, then map it over the inputs, then return 
## the size  of a set of the sanitized inputs

## ends up at ~97th percentile in terms of runtime, though
## only15th percentile in terms of RAM

class Solution:
    def sanitize_email_address(self, email: str) -> str:
        user, domain = email.split('@')
        
        ## drop everything after the first plus
        user = user.split('+')[0]
        
        ## remove any dots
        user = user.replace('.', '')
        
        return user+'@'+domain
        
    
    def numUniqueEmails(self, emails: List[str]) -> int:
        cleaned_emails = map(self.sanitize_email_address, emails)
        return len(set(cleaned_emails))