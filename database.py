

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



