salary_list = [7.3, 8.5, 11, 12.7, 15.2, 21.12, 27.35]
#final_salary_list = []
#indexation = [] 
print("Salary table: ")
final_salary_list = list(map(lambda x: round(float(x)* 1.3, 2) , salary_list))
indexation = list(map(lambda x, y: round(x - y, 2), final_salary_list, salary_list))
for i in range(len(salary_list)):
    print(str(salary_list[i]) + " " + str(final_salary_list[i]) + " " + str(indexation[i]))
