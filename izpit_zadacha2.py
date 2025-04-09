# class Worker:
#     def __init__(self, worker_num,fname,lname,work_experience_company,salary,age):
#         self.worker_num=worker_num
#         self.fname=fname
#         self.lname=lname
#         self.work_experience_company=work_experience_company
#         self.salary=salary
#         self.age=age
    
#     def worker_information(self):
#         print(f"{self.worker_num}, {self.fname}, {self.lname}, {self.work_experience_company}, {self.salary}, {self.age}")
    
#     def salary_bonus(self):
#         if self.work_experience_company>10:
#             return round(self.salary*2/100, 2)
#         elif self.work_experience_company<5:
#             return round(self.salary*0.5/100, 2)
#         else:
#             return round(self.salary*1.5/100,2)
        
#     def search_by_num(workers_list, worker_num):
#         for worker in workers_list:
#             if worker.worker_num == worker_num:
#                 return True
#         return False
    
#     def search_by_name_experience(workers_list, fname, work_experience_company):
#         result_list = [worker for worker in workers_list if worker.fname == fname and worker.work_experience_company == work_experience_company]
#         return result_list
    
#     def add_worker(workers_list,worker):
#         workers_list.append(worker)
#         print("Worker information added succesfully!")

#     def remove_worker(workers_list, worker_num):
#         for worker in workers_list:
#             if worker.worker_num == worker_num:
#                 workers_list.remove(worker)
#                 print("Information deleted !!!")
#                 return
#         print("Wrong worker_num !!!")


# workers_list = [] 
# worker1 = Worker(1, "John", "Doe", 8, 50000, 30)
# worker2 = Worker(2, "Jane", "Smith", 12, 60000, 35)
# print(worker1)
# add_worker(workers_list, worker1)
# add_worker(workers_list, worker2)


#ДАННИТЕ СА ВЪВЕДЕНИ ОТ КОДА
class Worker:
    def __init__(self, worker_num, fname, lname, work_experience_company, salary, age):
        self.worker_num = worker_num
        self.fname = fname
        self.lname = lname
        self.work_experience_company = work_experience_company
        self.salary = salary
        self.age = age

    def worker_information(self):
        print(f"Worker Information: {self.fname} {self.lname}")
        print(f"Worker Number: {self.worker_num}")
        print(f"Work Experience: {self.work_experience_company} years")
        print(f"Salary: ${self.salary}")
        print(f"Age: {self.age} years")

    def salary_bonus(self):
        if 5 <= self.work_experience_company <= 10:
            bonus_percentage = 1.5
        elif self.work_experience_company > 10:
            bonus_percentage = 2.0
        else:
            bonus_percentage = 0.5

        bonus_amount = (bonus_percentage / 100) * self.salary
        self.salary += bonus_amount
        print(f"Bonus added: ${bonus_amount}")
        print(f"Updated Salary: ${self.salary}")


def search_by_num(workers_list, worker_num):
    for worker in workers_list:
        if worker.worker_num == worker_num:
            return True
    return False


def search_by_name_experience(workers_list, fname, work_experience):
    result_list = [worker for worker in workers_list if worker.fname == fname and worker.work_experience_company == work_experience]
    return result_list


def add_worker(workers_list, worker):
    workers_list.append(worker)
    print("Worker information added successfully!")


def remove_worker(workers_list, worker_num):
    for worker in workers_list:
        if worker.worker_num == worker_num:
            workers_list.remove(worker)
            print("Information deleted !!!")
            return
    print("Wrong worker_num !!!")


# Example usage:

workers_list = []

# Adding workers
worker1 = Worker(1, "John", "Doe", 8, 50000, 30)
worker2 = Worker(2, "Jane", "Smith", 12, 60000, 35)
add_worker(workers_list, worker1)
add_worker(workers_list, worker2)

# Searching by worker number
print(search_by_num(workers_list, 1))  # True
print(search_by_num(workers_list, 3))  # False

# Searching by name and work experience
result = search_by_name_experience(workers_list, "John", 8)
for worker in result:
    worker.worker_information()

# Adding a new worker
new_worker = Worker(3, "Alice", "Johnson", 4, 45000, 25)
add_worker(workers_list, new_worker)

# Removing a worker
remove_worker(workers_list, 2)

# Displaying updated worker list
for worker in workers_list:
    worker.worker_information()
        




#ДАННИТЕ СЕ ВЪВЕЖДАТ ОТ КОНЗОЛАТА
class Worker:
    def __init__(self, worker_num, fname, lname, work_experience_company, salary, age):
        self.worker_num = worker_num
        self.fname = fname
        self.lname = lname
        self.work_experience_company = work_experience_company
        self.salary = salary
        self.age = age

    def worker_information(self):
        print(f"Worker Information: {self.fname} {self.lname}")
        print(f"Worker Number: {self.worker_num}")
        print(f"Work Experience: {self.work_experience_company} years")
        print(f"Salary: ${self.salary}")
        print(f"Age: {self.age} years")

    def salary_bonus(self):
        if 5 <= self.work_experience_company <= 10:
            bonus_percentage = 1.5
        elif self.work_experience_company > 10:
            bonus_percentage = 2.0
        else:
            bonus_percentage = 0.5

        bonus_amount = (bonus_percentage / 100) * self.salary
        self.salary += bonus_amount
        print(f"Bonus added: ${bonus_amount}")
        print(f"Updated Salary: ${self.salary}")


def input_worker_data():
    worker_num = int(input("Enter worker number: "))
    fname = input("Enter first name: ")
    lname = input("Enter last name: ")
    work_experience_company = int(input("Enter work experience in years: "))
    salary = float(input("Enter salary: $"))
    age = int(input("Enter age: "))

    return Worker(worker_num, fname, lname, work_experience_company, salary, age)


def search_by_num(workers_list, worker_num):
    for worker in workers_list:
        if worker.worker_num == worker_num:
            return True
    return False


def search_by_name_experience(workers_list, fname, work_experience):
    result_list = [worker for worker in workers_list if worker.fname == fname and worker.work_experience_company == work_experience]
    return result_list


def add_worker(workers_list, worker):
    workers_list.append(worker)
    print("Worker information added successfully!")


def remove_worker(workers_list, worker_num):
    for worker in workers_list:
        if worker.worker_num == worker_num:
            workers_list.remove(worker)
            print("Information deleted !!!")
            return
    print("Wrong worker_num !!!")


# Example usage:

workers_list = []

# Adding workers
worker1 = input_worker_data()
add_worker(workers_list, worker1)

# Displaying worker information
worker1.worker_information()

# Searching by worker number
worker_num_to_search = int(input("Enter worker number to search: "))
print(search_by_num(workers_list, worker_num_to_search))

# Adding a new worker
new_worker = input_worker_data()
add_worker(workers_list, new_worker)

# Displaying updated worker list
for worker in workers_list:
    worker.worker_information()