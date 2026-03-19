'''
Hackerrank - Shoe Problem @ https://www.hackerrank.com/challenges/collections-counter/

Suppose you have to read below data as input in different variables 
and compute total revenue

10                      //#shoes
2 3 4 5 6 8 7 6 5 18    //available shoe sizes in shop (can be multiple)
6                       //no. of customers visiting
6 55                    //ith customer wants (shoe size, willing to pay $$)
6 45
6 55
4 40
18 60
10 50
'''
#Remember input() just reads the input as String
x_shoes = int(input())

#reading a string as input then converting it into a list of string items
shoe_size = list(input().split(' '))

#next we gotta convert those string items in above list into INT
#Use an iterator function of Lambda like MAP() to convert each List_Item into INT

shoe_size_map = map(lambda x: int(x), shoe_size)

#MAP is an object. To read/print it you gotta convert it into List
shoe_size = list(shoe_size_map)

available_shoe_dict = {}

for i in shoe_size:
    if i not in available_shoe_dict:
        available_shoe_dict[i] = 1
    else:
        available_shoe_dict[i]+=1

#print(available_shoe_dict)

n_cust = int(input())

#A dictionary cannot hold duplicate keys. So, you use a List
final_list = []

for i in range(n_cust):
    map1 = map(lambda x: int(x),input().split(' '))
    list1 = list(map1)
    final_list.append(list1)


raghu_revenue = 0

#print("final_list iterator")
for idx,shoe_list in enumerate(final_list):
    cust_size = shoe_list[0]
    cust_price = shoe_list[1]

    if cust_size in available_shoe_dict and (available_shoe_dict[shoe_list[0]]>0):
        raghu_revenue+=cust_price
        available_shoe_dict[cust_size]-=1

print(raghu_revenue)
