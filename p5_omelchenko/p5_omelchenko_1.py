salary_list = [7.3, 8.5, 11, 12.7, 15.2, 21.12, 27.35]
final_salary_list = []
indexation = [] 
print("Salary table: ")
for i in range(len(salary_list)):
    final_salary_list.append(round(float(salary_list[i])* 1.3, 2))
    indexation.append(round(final_salary_list[i] - salary_list[i], 2))
for i in range(len(salary_list)):
    print(str(salary_list[i]) + " " + str(final_salary_list[i]) + " " + str(indexation[i]))




