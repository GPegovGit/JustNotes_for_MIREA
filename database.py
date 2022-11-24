import psycopg2
from config import host, user, password, db_name

def add_new_task(deadline: str, executor_id: int, author_id: int, task_id: int, task_description: str, priority: int, status: str, contract_id: int):
        with connection.cursor() as cursor:
                try:
                        cursor.execute(f'CALL add_new_task(\'{deadline}\',{executor_id},{author_id},{task_id},\'{task_description}\',{priority},\'{status}\',{contract_id})')
                        print('New task added succesfully')
                except Exception as _ex:
                        print("[INFO] Error. New task not added. Reason: ", _ex)


def add_new_employee(job: str, fname: str, lname: str, patronymyc: str, phone: int, email: str, employee_id: int, login: str, password: str):
        with connection.cursor() as cursor:
                try:
                        cursor.execute(
                                f'CALL add_employee(\'{job}\',\'{fname}\',\'{lname}\',\'{patronymyc}\', {phone},\'{email}\',{employee_id},\'{login}\', \'{password}\')')
                        print('New employee added succesfully')
                except Exception as _ex:
                        print("[INFO] Error. New employee not added. Reason: ", _ex)


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

        add_new_task(deadline='2022-12-2 00:00:00+03', executor_id=5, author_id=1, task_id=16, task_description='Съесть печеньку', priority=1, status='active', contract_id=3)
        add_new_employee(job='manager', fname='Игорь', lname='Сидоров', patronymyc='Захарович', phone=8800559098, email='igorek77@mailru', employee_id=9, login='manager_6', password='Manager$$$')



except Exception as _ex:
        print("[INFO] Error while working with PostgreSQL", _ex)
finally:
        if connection:
                # cursor.close()
                connection.close()
                print("[INFO] PostgreSQL connection closed")
