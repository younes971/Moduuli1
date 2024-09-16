
def get_airport_icao_code(icao):
    sql_command = f"select * from airport where ident = %s"
    print(sql_command, (icao,))
    cursor = connection.cursor(dictionary=True)
    cursor.execute(sql_command, (icao,))

    # result = cursor.fetchall()
    result = cursor.fetchone()
    # print(result[0][3], result[0][10])
    return result


icao_code = input("Enter the code that you want to fetch from database: ")

fetch = get_airport_icao_code(icao_code)
print(fetch)










