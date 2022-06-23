# Problem Link https://leetcode.com/problems/average-salary-excluding-the-minimum-and-maximum-salary/

def average(salary):
    salary = sorted(salary)
    return sum(salary[1:len(salary)-1]) / (len(salary) - 2)


print(average([1000,2000,3000]))
