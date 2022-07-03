# Problem Link https://leetcode.com/problems/maximum-units-on-a-truck/

def maximum_units(boxTypes, truckSize):
    boxTypes.sort(key=lambda x: x[1], reverse=True)
    q = truckSize
    w = 0
    for i in boxTypes:
        if i[0] <= q:
            w += (i[0] * i[1])
            q -= i[0]
        else:
            w += (q * i[1])
            break
    return w


print(maximum_units([[5,10],[2,5],[4,7],[3,9]], 10))
