
async def scheduler_start (conn ):
    conn.execute(users.insert(), [
        {'username': 'admin', 'hash': hash_admin  ,
        'email': 'test1@robointerativo.ru','role_id':1},
        {'username': 'user', 'hash': hash_user ,
        'email': 'test2@robointerativo.ru','role_id':2},
        ])

    conn.close()


async def scheduler_done (conn ):
    conn.execute(users.insert(), [
        {'username': 'admin', 'hash': hash_admin  ,
        'email': 'test1@robointerativo.ru','role_id':1},
        {'username': 'user', 'hash': hash_user ,
        'email': 'test2@robointerativo.ru','role_id':2},
        ])

    conn.close()
