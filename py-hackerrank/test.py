def checkRecord(s: str) -> bool:
        at=0
        lct=0
        prev_char=None
        for c in s:
            if c=="A":
                at=at+1
            
            if at>1:
                return False
            
            if c=="L":
                if prev_char==None or prev_char=='L':
                    lct=lct+1
            else:
                lct=0
                
            if lct>=3:
                    return False
            prev_char=c
                
        return True

print(checkRecord("LALL"))