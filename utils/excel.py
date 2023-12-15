import aiosqlite
from openpyxl import Workbook

async def update_excel(ctx, message_flag=False):
    db = await aiosqlite.connect('Main.db')
    cursor = await db.cursor()
    await cursor.execute("SELECT * FROM member")
    rows = await cursor.fetchall()

    # Create a new Excel workbook and add a worksheet
    workbook = Workbook()
    worksheet = workbook.active

    # Write header row
    header = [description[0] for description in cursor.description]
    worksheet.append(header)

    # Write data rows
    for row in rows:
        worksheet.append(row)

    # Save the Excel file
    workbook.save("member.xlsx")


    await db.close()

    if message_flag:
        await ctx.send("Excel file updated!")