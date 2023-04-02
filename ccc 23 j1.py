p=input()
c=input()
p=int(p)
c=int(c)
points_for_delivery=p*50
points_lost=c*10
if p>c:
    bonus_points=500
if p<c:
    bonus_points=0
if p==c:
    bonus_points=0
total_points=points_for_delivery-points_lost+bonus_points
print(total_points)