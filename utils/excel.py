import aiosqlite
from openpyxl import Workbook

async def update_excel(ctx, message_flag=False):
    db = await aiosqlite.connect('Main.db')
    cursor = await db.cursor()

    # Define tables to export
    tables_to_export = ['member', 'register_2024_Q1']  # Add more table names as needed

    # Create a new Excel workbook
    workbook = Workbook()

    for table_name in tables_to_export:
        # Fetch data from the table
        await cursor.execute(f"SELECT * FROM {table_name}")
        rows = await cursor.fetchall()

        # Add a worksheet for the current table
        worksheet = workbook.create_sheet(title=table_name)

        # Write header row
        header = [description[0] for description in cursor.description]
        worksheet.append(header)

        # Write data rows
        for row in rows:
            worksheet.append(row)

    # Remove the default sheet created by openpyxl
    workbook.remove(workbook['Sheet'])

    # Save the Excel file
    workbook.save("output.xlsx")

    await db.close()

    if message_flag:
        await ctx.send("Excel file updated!")