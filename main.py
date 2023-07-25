from kivy.lang import Builder
from kivymd.app import MDApp
import sqlite3

class MyApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "BlueGray"

        # Creating the database 
        connection = sqlite3.connect('first_database.db')
        db_cursor = connection.cursor()
        db_cursor.execute("""CREATE TABLE if not exists books(title text)""")
        connection.commit()
        connection.close()

        return Builder.load_file('app.kv')

    def submit(self):
        connection = sqlite3.connect('first_database.db')
        db_cursor = connection.cursor()

        # Submiting values to the database 
        connection.execute("INSERT INTO books VALUES (:name)", {'name': self.root.ids.word_input.text,})
        self.root.ids.word_label.text = f'{self.root.ids.word_input.text} added'
        self.root.ids.word_input.text = ''
        
        connection.commit()
        connection.close()
    
    def show_records(self):
        connection = sqlite3.connect('first_database.db')
        db_cursor = connection.cursor()
    
        # Showing values from database
        db_cursor.execute("SELECT * FROM books")
        records = db_cursor.fetchall()
        title = ''
        for record in records:
            title = f'{title}\n{record[0]}'
            self.root.ids.word_label.text = f'{title}'
    
        connection.commit()
        connection.close()

MyApp().run()

