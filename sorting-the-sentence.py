class Solution:
    def sortSentence(self, s: str) -> str:
        if len(s)>=2 and len(s)<=200:
            list=s.split()
            if len(list)>=1 and len(list)<=9:
                str=" "
                ordlist=[str]*len(list)
                for i in list:
                    index = int(i[-1])
                    ordlist[index-1]=i[:-1]
                str=str.join(ordlist)
                return str
