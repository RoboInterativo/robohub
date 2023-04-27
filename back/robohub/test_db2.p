

from db import sqlite_context_engine,get_user_by_name,users

import asyncio
import os
async def async_main():

    WORK_DIR=os.path.dirname(os.path.abspath(__file__) )

    engine= sqlite_context_engine(WORK_DIR)

    print (engine)
    async with engine.connect() as conn:
        result = await conn.execute(
            users
            .select()
            .where(users.c.username == 'admin')
        )
        records =  result.fetchone()
        print(records)
        # user = await get_user_by_name(conn, 'admin')
        # print (user)


    await engine.dispose()


loop = asyncio.get_event_loop()
loop.run_until_complete(async_main())
