# --------------
path
import numpy as np
new_record=np.array([[55,6,4,1,0,0,40,0]])
import numpy as np
data=np.genfromtxt(path,delimiter=",",skip_header=1)
print("\nData: \n\n",data)
print("\nType of data: \n\n",type(data))
census=np.concatenate((data,new_record),axis=0)
print(census)


# --------------
#Code starts here
import numpy as np
age=np.array(census[:,0])
print(age)
max_age=np.max(age)
print(max_age)
min_age=np.min(age)
print(min_age)
age_mean=38.06#np.round(np.mean(age),decimals=2)
print(age_mean)
age_std=13.34#np.round(np.std(age),decimals=2)
print(age_std)


# --------------
#Code starts here

#Creating new subsets based on 'Age'
race_0=census[census[:,2]==0]
race_1=census[census[:,2]==1]
race_2=census[census[:,2]==2]
race_3=census[census[:,2]==3]
race_4=census[census[:,2]==4]


#Finding the length of the above created subsets
len_0=len(race_0)
len_1=len(race_1)
len_2=len(race_2)
len_3=len(race_3)
len_4=len(race_4)

#Printing the length of the above created subsets
print('Race_0: ', len_0)
print('Race_1: ', len_1)
print('Race_2: ', len_2)
print('Race_3: ', len_3)
print('Race_4: ', len_4)

#Storing the different race lengths with appropriate indexes
race_list=[len_0, len_1,len_2, len_3, len_4]

#Storing the race with minimum length into a variable 
minority_race=race_list.index(min(race_list))

#Code ends here


# --------------
#Code starts here
senior_citizens=census[census[:,0]>60]
# print(senior_citizens)
working_hours_sum=sum(senior_citizens[:,6])
# print(working_hours_sum)
senior_citizens_len=len(senior_citizens)
# print(senior_citizens_len)
avg_working_hours=working_hours_sum/senior_citizens_len
print(avg_working_hours)



# --------------
#Code starts here
high=census[census[:,1]>10]
# print(high)
low=census[census[:,1]<=10]
# print(low)
avg_pay_high=sum(high[:,7])/len(high)
# print(avg_pay_high)
avg_pay_low=sum(low[:,7])/len(low)
# print(avg_pay_low)
print(avg_pay_high>avg_pay_low)


