
def get_units(connection):
    cursor = connection.cursor()
    query = "select * from unit"
    cursor.execute(query)
    response = []
    for (unit_id, unit_name) in cursor:
        response.append({
            'unit_id': unit_id,
            'unit_name': unit_name
        })
    return response


if __name__ == '__main__':
    from sql_con import sql_connection

    connection = sql_connection()
    # print(get_all_products(connection))
    print(get_units(connection))