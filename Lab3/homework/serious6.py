def is_inside(l1,l2):
    xmax = l2[0] + l2[2]
    xmin = l2[0]
    ymax = l2[1] + l2[3]
    ymin = l2[1]
    if xmin < l1[0] < xmax and ymin < l1[1] < ymax:
        return True
    else:
        return False

a = is_inside ([200,120],[140,60,100,200])
print(a)
