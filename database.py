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



except Exception as _ex:
        print("[INFO] Error while working with PostgreSQL", _ex)
finally:
        if connection:
                # cursor.close()
                connection.close()
                print("[INFO] PostgreSQL connection closed")
