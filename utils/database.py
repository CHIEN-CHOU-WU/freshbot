
import aiosqlite

async def delete_data(first_name, last_name, nickname):
    db = await aiosqlite.connect('Main.db')
    cursor = await db.cursor()
    delete_query = f"DELETE FROM member WHERE first_name == ? and last_name == ? and nickname == ?"
    await cursor.execute(delete_query, (first_name, last_name, nickname))

    await db.commit()