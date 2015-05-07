"""
>>> s = Solution()
>>> s.makeDict(['spam',10,15,'zzz','eggz'])
<type 'dict'>
{0: 'spam', 1: 10, 2: 15, 3: 'zzz', 4: 'eggz'}
"""

class Solution:

    def makeDict(self, alist):
        d = dict(enumerate(alist))
        print type(d)
        print d