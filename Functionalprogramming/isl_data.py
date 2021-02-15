isl=[{"team":"Mumbai City FC","match":16,"won":10,"drawn":4,"lost":2,"gf":25,"ga":11,"gd":14,"points":34},
     {"team":"ATK Mohun Bagan","match":16,"won":10,"drawn":3,"lost":3,"gf":22,"ga":10,"gd":12,"points":33},
     {"team":"NorthEast United FC","match":17,"won":6,"drawn":8,"lost":3,"gf":24,"ga":21,"gd":3,"points":26},
     {"team":"FC Goa","match":17,"won":5,"drawn":9,"lost":3,"gf":26,"ga":21,"gd":5,"points":24},
     {"team":"Hyderabad FC","match":17,"won":5,"drawn":9,"lost":3,"gf":21,"ga":17,"gd":4,"points":24},
     {"team":"Bengaluru FC","match":17,"won":5,"drawn":6,"lost":6,"gf":16,"ga":19,"gd":-3,"points":21},
     {"team":"Jamshedpur FC","match":17,"won":4,"drawn":7,"lost":6,"gf":19,"ga":21,"gd":-2,"points":19},
     {"team":"Chennaiyin FC","match":18,"won":3,"drawn":9,"lost":6,"gf":21,"ga":19,"gd":-6,"points":18},
     {"team":"SC East Bengal","match":17,"won":3,"drawn":8,"lost":6,"gf":19,"ga":22,"gd":-7,"points":17},
     {"team":"Kerala Blasters FC","match":17,"won":3,"drawn":7,"lost":7,"gf":22,"ga":29,"gd":-7,"points":16},
     {"team":"Odisha FC","match":17,"won":1,"drawn":6,"lost":10,"gf":30,"ga":30,"gd":-13,"points":9}]
#highest point
from functools import reduce
point_high=list(filter(lambda team:team["points"]==reduce(lambda p1,p2:p1 if p1>p2 else p2,list(map(lambda team:team["points"],isl))),isl))
print("Highest Points:",point_high)
#lowest
point_high=list(filter(lambda team:team["points"]==reduce(lambda p1,p2:p1 if p1<p2 else p2,list(map(lambda team:team["points"],isl))),isl))
print("Lowest Points:",point_high)