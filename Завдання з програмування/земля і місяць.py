import math
def intersection_area(x1, y1, r1, x2, y2, r2):
    d=math.dist([x1,y1],[x2,y2])
    if d <=abs(r1-r2):
        r=min(r1, r2)
        return math.pi*r**2
    if d>r1+r2:
        return 0
    alpha_1=2*math.acos((r1**2-r2**2+d**2)/(2*r1*d))
    alpha_2=2*math.acos((r2**2 -r1**2+d**2)/(2*r2*d))
    s_1=(r1**2/2)*(alpha_1-math.sin(alpha_1))
    s_2=(r2**2/2)*(alpha_2-math.sin(alpha_2))
    s=s_1+s_2
    return s
x1,y1,r1=map(int, input().split())
x2,y2,r2=map(int, input().split())
intersection = intersection_area(x1, y1, r1, x2, y2, r2)
print("%.5f"%intersection)
    
