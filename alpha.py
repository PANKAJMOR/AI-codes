M,m = -1000,1000

def minmax(depth,nodei,maxplayer,values,alpha,beta):
    
    if depth == 3:
        return values[nodei]
    
    if maxplayer:
        best = M

        for i in range(0,2):
         val = minmax(depth+1,2*nodei+i,0,values,alpha,beta)
         best = max(best,val)
         alpha = max(alpha,best)

         if beta <= alpha:
            break

        return best
        
    else:
        best = m

        for i in range(0,2):
         val = minmax(depth+1,2*nodei+i,1,values,alpha,beta)
         best = min(best,val)
         beta = min(beta,best)

         if beta <= alpha:
            break

        return best    
    
values = [3,5,6,9,1,2,0,-1]
print(minmax(0,0,True,values,M,m))
       