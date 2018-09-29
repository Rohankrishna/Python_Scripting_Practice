import random
from math import ceil

def find(order_list, element_to_search):
    start_index=0
    end_index=len(order_list)-1

    while True:
        middle_index=ceil((end_index+start_index)/2)
        #middle_index=round(middle_index)
        print(start_index, middle_index, end_index)

        if middle_index>end_index or middle_index<start_index or middle_index<0:
            return False

        middle_element=order_list[middle_index]  

        if middle_element==element_to_search:
            return True

        elif middle_element<element_to_search:
            start_index=middle_index+1    

        else:
            end_index=middle_index-1  

#if __name__ == "__main__":
n=int(input("enter number of elements in ordered list: "))
ol=[]
for i in range(1,n):
    ol.append(random.randint(1,100))
print("Unordered list = ",ol)
ol.sort()
print("Ordered list=  ",ol)
elem=int(input("Enter element you want to search: "))
print(find(ol, elem))
