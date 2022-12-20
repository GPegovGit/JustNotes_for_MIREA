

# # Получение должности по id сотрудника
# def get_job_title_by_employee_id(employee_id: int):
#         with connection.cursor() as cursor:
#                 try:
#                         query_str = f'SELECT job_title FROM public.employee WHERE employee_id = {employee_id}'
#                         cursor.execute(query_str)
#                         filtered_employees = cursor.fetchall()
#
#                         print(f'role of employee: {filtered_employees[0]}')
#
#                 except Exception as _ex:
#                         print("[INFO] Error.get_job_title_by_employee_id error. Reason: ", _ex)
import psycopg2

import config
from widget_classes import current_user
from psycopg2 import sql


def add_part(part_name: str, part_price: int, part_manufacturer_name: str):
    try:
        # connect to exist database
        connection = psycopg2.connect(
            host=config.host,
            user=current_user.login,
            password=current_user.password,
            database=config.db_name
        )
        connection.autocommit = True
        with connection.cursor() as cursor:
            try:
                s1 = sql.Literal(part_name)
                s2 = sql.Literal(part_price)
                s3 = sql.Literal(part_manufacturer_name)
                query = sql.SQL("INSERT INTO part(part_name, part_price, part_manufacturer_name) VALUES ({})").format(
    sql.SQL(', ').join([s1, s2, s3]))
                cursor.execute(query)
            except Exception as _ex:
                print("[INFO] Error. Part add error. Reason: ", _ex)
                return
    except Exception as _ex:
        print("[INFO] Error. Part add error. Reason: ", _ex)


def add_car(license_plate: str, color: str, estimated_value: int, car_model_id: int):
    try:
        # connect to exist database
        connection = psycopg2.connect(
            host=config.host,
            user=current_user.login,
            password=current_user.password,
            database=config.db_name
        )
        connection.autocommit = True
        with connection.cursor() as cursor:
            try:
                s1 = sql.Literal(license_plate)
                s2 = sql.Literal(color)
                s3 = sql.Literal(estimated_value)
                s4 = sql.Literal(car_model_id)
                query = sql.SQL("INSERT INTO car(license_plate, color, estimated_value, car_model_id) VALUES ({})").format(
    sql.SQL(', ').join([s1, s2, s3, s4]))
                cursor.execute(query)
            except Exception as _ex:
                print("[INFO] Error. Car add error. Reason: ", _ex)
                return
    except Exception as _ex:
        print("[INFO] Error. Car add error. Reason: ", _ex)


def add_car_brand(brand_name: str):
    try:
        # connect to exist database
        connection = psycopg2.connect(
            host=config.host,
            user=current_user.login,
            password=current_user.password,
            database=config.db_name
        )
        connection.autocommit = True
        with connection.cursor() as cursor:
            try:
                s1 = sql.Literal(brand_name)

                query = sql.SQL("INSERT INTO car_brand(brand_name) VALUES ({})").format(
                    sql.SQL(', ').join([s1]))
                cursor.execute(query)
            except Exception as _ex:
                print("[INFO] Error. Car_brand add error. Reason: ", _ex)
                return
    except Exception as _ex:
        print("[INFO] Error. Car_brand add error. Reason: ", _ex)


def add_model_data(model_name: str, model_year: int, brand_id: int):
    try:
        # connect to exist database
        connection = psycopg2.connect(
            host=config.host,
            user=current_user.login,
            password=current_user.password,
            database=config.db_name
        )
        connection.autocommit = True
        with connection.cursor() as cursor:
            try:
                s1 = sql.Literal(model_name)
                s2 = sql.Literal(model_year)
                s3 = sql.Literal(brand_id)
                query = sql.SQL("INSERT INTO model_data(model_name, model_year, brand_id) VALUES ({})").format(
    sql.SQL(', ').join([s1, s2, s3]))
                cursor.execute(query)
            except Exception as _ex:
                print("[INFO] Error. Model_data add error. Reason: ", _ex)
                return
    except Exception as _ex:
        print("[INFO] Error. Model_data add error. Reason: ", _ex)


def add_service(service_name: str, service_address: str, service_phone_number: str, service_manager: str):
    try:
        # connect to exist database
        connection = psycopg2.connect(
            host=config.host,
            user=current_user.login,
            password=current_user.password,
            database=config.db_name
        )
        connection.autocommit = True
        with connection.cursor() as cursor:
            try:
                s1 = sql.Literal(service_name)
                s2 = sql.Literal(service_address)
                s3 = sql.Literal(service_phone_number)
                s4 = sql.Literal(service_manager)
                query = sql.SQL("INSERT INTO service(service_name, service_address, service_phone_number, service_manager) VALUES ({})").format(
    sql.SQL(', ').join([s1, s2, s3, s4]))
                cursor.execute(query)
            except Exception as _ex:
                print("[INFO] Error. Service add error. Reason: ", _ex)
                return
    except Exception as _ex:
        print("[INFO] Error. Service add error. Reason: ", _ex)

#Getters
def get_parts():
    try:
        # connect to exist database
        connection = psycopg2.connect(
            host=config.host,
            user=current_user.login,
            password=current_user.password,
            database=config.db_name
        )
        connection.autocommit = True
        with connection.cursor() as cursor:
            try:
                query = sql.SQL("SELECT * FROM part")
                cursor.execute(query)
                parts = cursor.fetchall()
                return parts
            except Exception as _ex:
                print("[INFO] Error. Get part error. Reason: ", _ex)
                return
    except Exception as _ex:
        print("[INFO] Error. Get part error. Reason: ", _ex)


def get_cars():
    try:
        # connect to exist database
        connection = psycopg2.connect(
            host=config.host,
            user=current_user.login,
            password=current_user.password,
            database=config.db_name
        )
        connection.autocommit = True
        with connection.cursor() as cursor:
            try:
                query = sql.SQL("SELECT * FROM car")
                cursor.execute(query)
                cars = cursor.fetchall()
                return cars
            except Exception as _ex:
                print("[INFO] Error. Get cars error. Reason: ", _ex)
                return
    except Exception as _ex:
        print("[INFO] Error. Get cars error. Reason: ", _ex)


def get_car_brands():
    try:
        # connect to exist database
        connection = psycopg2.connect(
            host=config.host,
            user=current_user.login,
            password=current_user.password,
            database=config.db_name
        )
        connection.autocommit = True
        with connection.cursor() as cursor:
            try:
                query = sql.SQL("SELECT * FROM car_brand")
                cursor.execute(query)
                car_brands = cursor.fetchall()
                return car_brands
            except Exception as _ex:
                print("[INFO] Error. Get car_brand error. Reason: ", _ex)
                return
    except Exception as _ex:
        print("[INFO] Error. Get car_brand error. Reason: ", _ex)


def get_model_data():
    try:
        # connect to exist database
        connection = psycopg2.connect(
            host=config.host,
            user=current_user.login,
            password=current_user.password,
            database=config.db_name
        )
        connection.autocommit = True
        with connection.cursor() as cursor:
            try:
                query = sql.SQL("SELECT * FROM model_data")
                cursor.execute(query)
                model_data = cursor.fetchall()
                return model_data
            except Exception as _ex:
                print("[INFO] Error. Get model_data error. Reason: ", _ex)
                return
    except Exception as _ex:
        print("[INFO] Error. Get model_data error. Reason: ", _ex)


def get_services():
    try:
        # connect to exist database
        connection = psycopg2.connect(
            host=config.host,
            user=current_user.login,
            password=current_user.password,
            database=config.db_name
        )
        connection.autocommit = True
        with connection.cursor() as cursor:
            try:
                query = sql.SQL("SELECT * FROM service")
                cursor.execute(query)
                services = cursor.fetchall()
                return services
            except Exception as _ex:
                print("[INFO] Error. Get services error. Reason: ", _ex)
                return
    except Exception as _ex:
        print("[INFO] Error. Get services error. Reason: ", _ex)