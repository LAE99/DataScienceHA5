def new_value_assignment(new_list, index_new_list, old_list, index_old_list):
    new_list[index_new_list] = old_list[index_old_list]


def merge_sort(list_to_sort_by_merge):
    if (len(list_to_sort_by_merge) > 1):
        middle_index = len(list_to_sort_by_merge) // 2 #split list in two sub lists in the middle
        left_value_list = list_to_sort_by_merge[:mid]
        right_value_list = list_to_sort_by_merge[mid:]

        merge_sort(left_value_list) #recursive application of merge_sort function for left and right list
        merge_sort(right_value_list)

        index_left_list = 0
        index_right_list = 0
        index_list_to_sort = 0

        while index_left_list < len(left_value_list) and index_right_list < len(right_value_list): #the values of the two lsit are compared and the lower is added to the list 
            if left_value_list[index_left_list] <= right_value_list[index_right_list]: 
                new_value_assignment(new_list=list_to_sort_by_merge, 
                                     index_new_list=index_list_to_sort, 
                                     old_list=left_value_list, 
                                     index_old_list=index_left_list)
                index_left_list += 1 # the index of the left list with the lower value is increased so that the value of the right lit which is higher can compared with the next value of the left list
            
            else:
                new_value_assignment(new_list=list_to_sort_by_merge, 
                                     index_new_list=index_list_to_sort, 
                                     old_list=right_value_list, 
                                     index_old_list=index_right_list) #the value of the right list is lower so this value is added to the original list and the right list index is increased
                
                index_right_list += 1
            index_list_to_sort += 1 #index at which the lower value is addded is increased with each round
        
        #the values which didn't added before now will be addded
        while index_left_list < len(left_value_list): 
            list_to_sort_by_merge[index_list_to_sort] = left_value_list[index_left_list]
            index_left_list += 1
            index_list_to_sort += 1

        while index_right_list < len(right_value_list):
            list_to_sort_by_merge[index_list_to_sort] = right_value_list[index_right_list]
            index_right_list += 1
            index_list_to_sort += 1


import matplotlib.pyplot as plt

my_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
x = range(len(my_list))
fig, ax = plt.subplots(nrows=1, ncols=1)

ax.plot(x, my_list, label = "unsorted")
#plt.show()
mergeSort(my_list)
x = range(len(my_list))
ax.plot(x, my_list, label = "sorted")

ax.set_xlabel('Indices of list')
ax.set_ylabel('Value at index of list')
fig.suptitle('Values of List')
ax.legend()
plt.ylim([0,100])
plt.xlim([0,9])
plt.show()