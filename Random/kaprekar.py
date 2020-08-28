for i in range(1,10):
    for j in range(1,10):
        for p in range(1,10):
            for q in range(1,10):
                num=[str(i),str(j),str(p),str(q)]
                c=True
                for i in range(3):
                    for j in range(i+1,4):
                        if(num[i]==num[j]):
                            c=False
                if(c):
                    ans = 0
                    while int(''.join(num)) != 6174:
                        num = list(str(int(''.join(sorted(num,reverse=True)))-int(''.join(sorted(num)))))
                        ans+=1
                        if(ans>7):
                            print(num)
                            raise Exception
                    print(ans)