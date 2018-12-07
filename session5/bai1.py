p1 = {
    "name": "Huy",
    "VND per hour" : 20,
    "hour": 25,
}
p2 = {
    "name": "Quan",
    "VND per hour": 30,
    "hour": 30

}
p3 = {
    "name": "H.Duc",
    "VND per hour" : 25,
    "hour" : 15,
}
p_list = [p1,p2,p3]
wage_list = [p["VND per hour"] * p["hour"] for p in p_list]
total = sum(wage_list)
print(total)
# print(p_list)
# total = 0
# for p in p_list:
#     hour = p["hour"]
#     vnd = p["VND per hour"]
#     name = p["name"]
#     wage =   int(hour*vnd)
#     print(name, wage)
#     total += wage
# print("total wage:",total)



    


