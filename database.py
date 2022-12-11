import psycopg2
from config import host, user, password, db_name

#4. Создание заявок
def add_new_task(deadline: str, executor_id: int, author_id: int, task_id: int, task_description: str, priority: int, status: str, contract_id: int):
        with connection.cursor() as cursor:
                try:
                        cursor.execute(f'CALL add_new_task(\'{deadline}\',{executor_id},{author_id},{task_id},\'{task_description}\',{priority},\'{status}\',{contract_id})')
                        print('New task added succesfully')
                except Exception as _ex:
                        print("[INFO] Error. New task not added. Reason: ", _ex)

#1. Регистрация новых пользователей (шифрования пока нет)
def add_new_employee(job: str, fname: str, lname: str, patronymyc: str, phone: int, email: str, employee_id: int, login: str, password: str):
        with connection.cursor() as cursor:
                try:
                        cursor.execute(
                                f'CALL add_employee(\'{job}\',\'{fname}\',\'{lname}\',\'{patronymyc}\', {phone},\'{email}\',{employee_id},\'{login}\', \'{password}\')')
                        print('New employee added succesfully')
                except Exception as _ex:
                        print("[INFO] Error. New employee not added. Reason: ", _ex)

#5. Поиск клиентов
def client_search(company_name: str):
        with connection.cursor() as cursor:
                try:
                        cursor.execute(
                                f'SELECT * FROM public.client WHERE company_name LIKE \'{company_name}\'')
                        search_results = cursor.fetchall()
                        print('Search results:')
                        for row in search_results:
                                print("Client id = ", row[0], )
                                print("Phone number = ", row[1])
                                print("Email = ", row[2])
                                print("Company name = ", row[3])
                                print("Client status = ", row[4])
                                print("Registration city = ", row[5], "\n")
                except Exception as _ex:
                        print("[INFO] Error. Search error. Reason: ", _ex)

#3. Простмотр задания
def view_tasks(username: str):
        with connection.cursor() as cursor:
                try:
                        cursor.execute(f'SELECT * FROM public.task WHERE executor_employee_id = (SELECT employee_id FROM public.employee WHERE username = \'{username}\')')
                        executor_tasks = cursor.fetchall()

                        cursor.execute(f'SELECT job_title FROM public.employee WHERE username = \'{username}\'')
                        job_title = cursor.fetchone()

                        if job_title[0] == 'manager':
                                cursor.execute(
                                        f'SELECT * FROM public.task WHERE author_employee_id = (SELECT employee_id FROM public.employee WHERE username = \'{username}\')')
                                author_tasks = cursor.fetchall()

                                print('Tasks by authorship of an employee:')
                                for row in author_tasks:
                                        print("deadline = ", row[0], )
                                        print("appointment_date = ", row[1])
                                        print("executor_employee_id = ", row[2])
                                        print("author_employee_id = ", row[3])
                                        print("task_id = ", row[4])
                                        print("task_description = ", row[5])
                                        print("priority = ", row[6])
                                        print("status = ", row[7])
                                        print("contract_id = ", row[8], "\n")


                        print('Tasks executed by an employee:')
                        for row in executor_tasks:
                                print("deadline = ", row[0], )
                                print("appointment_date = ", row[1])
                                print("executor_employee_id = ", row[2])
                                print("author_employee_id = ", row[3])
                                print("task_id = ", row[4])
                                print("task_description = ", row[5])
                                print("priority = ", row[6])
                                print("status = ", row[7])
                                print("contract_id = ", row[8], "\n")

                except Exception as _ex:
                        print("[INFO] Error. view tasks error. Reason: ", _ex)
#2
def view_employees(username: str):
        with connection.cursor() as cursor:
                try:
                        cursor.execute(f'SELECT job_title FROM public.employee WHERE username = \'{username}\'')
                        job_title = cursor.fetchone()

                        if job_title[0] == 'manager':
                                cursor.execute(
                                        f'SELECT * FROM public.employee')
                                current_user = cursor.fetchall()


                        else:
                                cursor.execute(
                                        f'SELECT * FROM public.employee WHERE username = \'{username}\'')
                                current_user = cursor.fetchall()

                        print('Employees seen by the current user:')
                        for row in current_user:
                                print("job_title = ", row[0], )
                                print("first_name = ", row[1])
                                print("last_name = ", row[2])
                                print("patronymyc = ", row[3])
                                print("phone_number = ", row[4])
                                print("email = ", row[5])
                                print("employee_id = ", row[6])
                                print("username = ", row[7])
                                print("password = ", row[8], "\n")

                except Exception as _ex:
                        print("[INFO] Error. employees view error. Reason: ", _ex)

#2
def view_contracts():
        with connection.cursor() as cursor:
                try:
                        cursor.execute(f'SELECT * FROM public.contract')
                        contracts = cursor.fetchall()

                        print('Contracts seen by the current user:')
                        for row in contracts:
                                print("contract_id = ", row[0], )
                                print("contract_name = ", row[1])
                                print("contract_description = ", row[2])
                                print("client_id = ", row[3])
                                print("item_serial_number = ", row[4], "\n")

                except Exception as _ex:
                        print("[INFO] Error. contractsview error. Reason: ", _ex)


# 2
def view_clients():
        with connection.cursor() as cursor:
                try:
                        cursor.execute(f'SELECT * FROM public.client')
                        contracts = cursor.fetchall()

                        print('Clients seen by the current user:')
                        for row in contracts:
                                print("client_id = ", row[0], )
                                print("phone_number = ", row[1])
                                print("email = ", row[2])
                                print("company_name = ", row[3])
                                print("client_status = ", row[4])
                                print("registration_city = ", row[5], "\n")

                except Exception as _ex:
                        print("[INFO] Error. clients view error. Reason: ", _ex)
#7
def tasks_report():
        with connection.cursor() as cursor:
                try:
                        cursor.execute(f'COPY (SELECT json_agg(row_to_json(task)) :: text FROM task WHERE status = \'finished\') to \'C:\DB\finished_tasks_report.json\'')
                        tasks_report = cursor.fetchall()

                except Exception as _ex:
                        print("[INFO] Error. tasks report error. Reason: ", _ex)

#6
def employees_report():
        with connection.cursor() as cursor:
                try:
                        cursor.execute(f'COPY (SELECT json_agg(row_to_json(employee)) :: text FROM employee) to \'C:\DB\employees_report.json\'')
                        employees_report = cursor.fetchall()

                except Exception as _ex:
                        print("[INFO] Error. employees report error. Reason: ", _ex)


def update_task(task_id: int, deadline: str = None, executor_id: int = None, priority: int = None, status: str = None):
        with connection.cursor() as cursor:
                try:
                        if(deadline != None):
                                cursor.execute(f'UPDATE task SET deadline = \'{deadline}\' WHERE task_id = {task_id}')
                        if (executor_id != None):
                                cursor.execute(f'UPDATE task SET executor_employee_id = {executor_id} WHERE task_id = {task_id}')
                        if (priority != None):
                                cursor.execute(f'UPDATE task SET priority = {priority} WHERE task_id = {task_id}')
                        if (status != None):
                                cursor.execute(f'UPDATE task SET status = \'{status}\' WHERE task_id = {task_id}')
                        print('Task updated succesfully')
                except Exception as _ex:
                        print("[INFO] Error. New task not added. Reason: ", _ex)

# Фильтр по таскам
def filter_tasks(author_id: int = None, executor_id: int = None, task_id: int = None, priority: int = None, status: str = None, contract_id: int = None):
        with connection.cursor() as cursor:
                try:
                        query_str = f'SELECT * FROM public.task'
                        s = 0
                        if author_id != None:
                                query_str+=f' WHERE author_employee_id = {author_id}'
                                s+=1
                        if executor_id != None:
                                if s==0:
                                        query_str += f' WHERE executor_employee_id = {executor_id}'
                                else:
                                        query_str += f' AND executor_employee_id = {executor_id}'
                                s += 1
                        if task_id != None:
                                if s == 0:
                                        query_str += f' WHERE task_id = {task_id}'
                                else:
                                        query_str += f' AND task_id = {task_id}'
                                s += 1
                        if priority != None:
                                if s == 0:
                                        query_str += f' WHERE priority = {priority}'
                                else:
                                        query_str += f' AND priority = {priority}'
                                s += 1
                        if status != None:
                                if s == 0:
                                        query_str += f' WHERE status = {status}'
                                else:
                                        query_str += f' AND status = {status}'
                                s += 1
                        if contract_id !=None:
                                if s == 0:
                                        query_str += f' WHERE contract_id = {contract_id}'
                                else:
                                        query_str += f' AND contract_id = {contract_id}'
                                s += 1


                        cursor.execute(query_str)
                        filtered_tasks = cursor.fetchall()

                        print('Filtered tasks:')
                        for row in filtered_tasks:
                                print("deadline = ", row[0], )
                                print("appointment_date = ", row[1])
                                print("executor_employee_id = ", row[2])
                                print("author_employee_id = ", row[3])
                                print("task_id = ", row[4])
                                print("task_description = ", row[5])
                                print("priority = ", row[6])
                                print("status = ", row[7])
                                print("contract_id = ", row[8], "\n")

                except Exception as _ex:
                        print("[INFO] Error. Task filter error. Reason: ", _ex)


# Фильтр по таскам
def filter_client(company_name: str = None, city: str = None, email: str = None, phone: int = None):
        with connection.cursor() as cursor:
                try:
                        query_str = f'SELECT * FROM public.client'
                        s = 0
                        if company_name != None:
                                query_str+=f' WHERE company_name = \'{company_name}\''
                                s+=1
                        if city != None:
                                if s==0:
                                        query_str += f' WHERE registration_city = \'{city}\''
                                else:
                                        query_str += f' AND registration_city = \'{city}\''
                                s += 1
                        if email != None:
                                if s == 0:
                                        query_str += f' WHERE email = \'{email}\''
                                else:
                                        query_str += f' AND email = \'{email}\''
                                s += 1
                        if phone != None:
                                if s == 0:
                                        query_str += f' WHERE phone_number = {phone}'
                                else:
                                        query_str += f' AND phone_number = {phone}'
                                s += 1


                        cursor.execute(query_str)
                        filtered_clients = cursor.fetchall()

                        print('Filtered tasks:')
                        for row in filtered_clients:
                                print("client_id = ", row[0], )
                                print("phone_number = ", row[1])
                                print("email = ", row[2])
                                print("company_name = ", row[3])
                                print("client_status = ", row[4])
                                print("registration_city = ", row[5], "\n")

                except Exception as _ex:
                        print("[INFO] Error. Client filter error. Reason: ", _ex)


# Фильтр по таскам
def filter_employee(first_name: str = None, second_name: str = None, patronymyc: str = None, phone: int = None, email: str = None, role: str = None):
        with connection.cursor() as cursor:
                try:
                        query_str = f'SELECT * FROM public.employee'
                        s = 0
                        if first_name != None:
                                query_str+=f' WHERE first_name = \'{first_name}\''
                                s+=1
                        if second_name != None:
                                if s==0:
                                        query_str += f' WHERE last_name = \'{second_name}\''
                                else:
                                        query_str += f' AND last_name = \'{second_name}\''
                                s += 1
                        if patronymyc != None:
                                if s == 0:
                                        query_str += f' WHERE patronymyc = \'{patronymyc}\''
                                else:
                                        query_str += f' AND patronymyc = \'{patronymyc}\''
                                s += 1
                        if phone != None:
                                if s == 0:
                                        query_str += f' WHERE phone_number = {phone}'
                                else:
                                        query_str += f' AND phone_number = {phone}'
                                s += 1
                        if email != None:
                                if s == 0:
                                        query_str += f' WHERE email = \'{email}\''
                                else:
                                        query_str += f' AND email = \'{email}\''
                                s += 1
                        if role != None:
                                if s == 0:
                                        query_str += f' WHERE job_title = \'{role}\''
                                else:
                                        query_str += f' AND job_title = \'{role}\''
                                s += 1


                        cursor.execute(query_str)
                        filtered_employees = cursor.fetchall()

                        print('Filtered employees:')
                        for row in filtered_employees:
                                print("job_title = ", row[0], )
                                print("first_name = ", row[1])
                                print("last_name = ", row[2])
                                print("patronymyc = ", row[3])
                                print("phone_number = ", row[4])
                                print("email = ", row[5])
                                print("employee_id = ", row[6])
                                print("username = ", row[7])
                                print("password = ", row[8], "\n")

                except Exception as _ex:
                        print("[INFO] Error. Employee filter error. Reason: ", _ex)


# Получение должности по id сотрудника
def get_job_title_by_employee_id(employee_id: int):
        with connection.cursor() as cursor:
                try:
                        query_str = f'SELECT job_title FROM public.employee WHERE employee_id = {employee_id}'
                        cursor.execute(query_str)
                        filtered_employees = cursor.fetchall()

                        print(f'role of employee: {filtered_employees[0]}')

                except Exception as _ex:
                        print("[INFO] Error.get_job_title_by_employee_id error. Reason: ", _ex)


# Получение должности по id сотрудника
def get_job_title_by_employee_id(employee_id: int):
        with connection.cursor() as cursor:
                try:
                        query_str = f'SELECT job_title FROM public.employee WHERE employee_id = {employee_id}'
                        cursor.execute(query_str)
                        filtered_employees = cursor.fetchall()

                        print(f'role of an employee: {filtered_employees[0]}')

                except Exception as _ex:
                        print("[INFO] Error.get_job_title_by_employee_id error. Reason: ", _ex)


# Получение должности по id сотрудника
def get_job_title_and_id_by_username(username: int):
        with connection.cursor() as cursor:
                try:
                        query_str = f'SELECT job_title, employee_id FROM public.employee WHERE username = \'{username}\''
                        cursor.execute(query_str)
                        role_and_id = cursor.fetchall()

                        for row in role_and_id:
                                print("job_title = ", row[0], )
                                print("employee_id = ", row[1], "\n")

                except Exception as _ex:
                                print("[INFO] get_job_title_and_id_by_username error. Reason: ", _ex)




try:
        # connect to exist database
        connection = psycopg2.connect(
                host=host,
                user=user,
                password=password,
                database=db_name
        )
        connection.autocommit = True

        # the cursor for perfoming database operations
        # cursor = connection.cursor()

        with connection.cursor() as cursor:
                cursor.execute(
                        "SELECT * FROM public.task"
                )

        #add_new_task(deadline='2022-12-2 00:00:00+03', executor_id=5, author_id=1, task_id=16, task_description='Съесть печеньку', priority=1, status='active', contract_id=3)
        #add_new_employee(job='manager', fname='Игорь', lname='Сидоров', patronymyc='Захарович', phone=8800559098, email='igorek77@mailru', employee_id=9, login='manager_6', password='Manager$$$')
        #client_search(company_name='Company_1')
        #view_tasks('manager_1')
        #view_employees('manager_1')
        #view_contracts()
        #view_clients()
        #tasks_report()
        #employees_report()
        #update_task(15, status='finished')
        #filter_tasks(1)
        #filter_client('Company_1', city='Chicago')
        #filter_employee(role='manager', first_name='Дмитрий')
        #get_job_title_by_employee_id(1)
        #get_job_title_and_id_by_username('manager_1')



except Exception as _ex:
        print("[INFO] Error while working with PostgreSQL", _ex)
finally:
        if connection:
                # cursor.close()
                connection.close()
                print("[INFO] PostgreSQL connection closed")
