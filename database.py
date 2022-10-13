import mysql.connector
import os

class DataBase:

    def __init__(self) -> None:
        pass

    def connection(self):
        self.mydb = mysql.connector.connect(
        host= os.getenv('HOST'),
        user= os.getenv('HOSTNAME'),
        password= os.getenv('PASSWORD'),
        database= os.getenv('DATABASE')
        )

        self.cursor = self.mydb.cursor(dictionary=True)
        return self.cursor


    def buy(self, message, author):
        
        try:
            self.connection()
            tab_message = message.split()
            arg1 = str(tab_message[1])
            arg2 = int(tab_message[2])
            who = str(author)

            sql = "INSERT INTO SHOPPING_LIST (NAME, QUANT, WHO) VALUES (%s, %s, %s)"
            val = (arg1, arg2, who)
            self.cursor.execute(sql, val)
            self.cursor.close()
            self.mydb.close()
            return f"{arg2} {arg1} added to the list buddy"
        except Exception as e:
            return str(e)
    


    def shop(self):
        try:
            self.connection()
            self.cursor.execute(f"SELECT NAME, QUANT FROM SHOPPING_LIST")
            rows = self.cursor.fetchall()
            all_rows = ""
            for row in rows:
                all_rows = all_rows + str(row["QUANT"]) + "\t" + str(row["NAME"]) + "\n"
            self.cursor.close()
            self.mydb.close()
            return all_rows
        except Exception as e:
            return str(e)

    def clear_list(self, message):
        try:
            self.connection()
            message.pop(0)
            print(message)
            req = "DELETE FROM SHOPPING_LIST"
            response=""
            for element in message:
                if element == message[0]:
                    req += f" WHERE NAME='{str(element)}'"
                else:
                    req += f" OR NAME='{str(element)}'"
                response += f"{str(element)} cleared !\n"
            print(req)
            self.cursor.execute(req)
            self.cursor.close()
            self.mydb.close()
            if response=="":
                return "List cleared !" 
            else:
                return response
        except Exception as e:
            return str(e)

