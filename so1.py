def solution(pobi, crong):
    # 페이지 수가 1~400 사이가 아닐때 , 리스트 왼쪽오른쪽이 바뀔때, 숫자 차이가 1이 아닐떄?
    if (pobi[1]-pobi[0] != 1) or min(pobi[0], pobi[1]) < 0 or max(pobi[0], pobi[1]) > 400 or min(crong[0], crong[1]) < 0 or max(crong[0], crong[1]) > 400:
        return print(-1)
    else:
        s = max(sum(map(int, list(str(pobi[0])))), sum(map(int, list(str(pobi[1])))))
        a = 1
        b = 1
        for i in map(int, list(str(pobi[0]))):
            a *= i

        for i in map(int, list(str(pobi[1]))):
            b *= i
            
        p = max(s,a,b) # 포비의 큰수
        
        s = max(sum(map(int, list(str(crong[0])))), sum(map(int, list(str(crong[1])))))
        a = 1
        b = 1
        for i in map(int, list(str(crong[0]))):
            a *= i

        for i in map(int, list(str(crong[1]))):
            b *= i
            
        c = max(s,a,b) # 크롱의 큰수
        
        if p > c:
            return print(1)
        elif p < c:
            return print(2)
        else:
            return print(0)
        
    
solution([97, 98], [197, 198])
solution([131, 132], [211, 212])
solution([99, 102], [211, 212])
        
        
        
        
        
        
    
    
    
    
    
