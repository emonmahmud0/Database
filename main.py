import tkinter
from tkinter import ttk, messagebox
import customs as cs
from functools import partial
import pymysql
import connections as cr
from abc import ABC, abstractmethod

class Management(ABC):
    def __init__(self, root):
        self.window = root
        self.window.title("Library Management System (LMS)")
        self.window.geometry("1060x640")
        self.window.config(bg = "white")
        @abstractmethod
        def ClearScreen(self):
            pass
        # Left Frame
        self.frame_1 = tkinter.Frame(self.window, bg=cs.color_1)
        self.frame_1.place(x=0, y=0, width=740, relheight = 1)
        # Right Frame
        self.frame_2 = tkinter.Frame(self.window, bg = cs.color_2)
        self.frame_2.place(x=740,y=0,relwidth=1, relheight=1)
        # A frame inside the right frame
        self.frame_3 = tkinter.Frame(self.frame_2, bg= cs.color_2)
        self.frame_3.place(x=0, y=300,relwidth=1, relheight=1)
        # All the Buttons in the frame 2
        self.add_book = tkinter.Button(self.frame_2, text='Add Book', font=(cs.font_1, 12), bd=2, command=self.AddNewBook, cursor="hand2", bg=cs.color_2, fg=cs.color_3).place(x=50, y=40, width=100)
        self.issue_book = tkinter.Button(self.frame_2, text='Issue Book', font=(cs.font_1, 12), bd=2, command=self.IssueBook, cursor="hand2", bg=cs.color_2, fg=cs.color_3).place(x=50, y=100, width=100)
        self.view_book = tkinter.Button(self.frame_2, text='View Book', font=(cs.font_1, 12), bd=2, command=self.ViewBook, cursor="hand2", bg=cs.color_2, fg=cs.color_3).place(x=50, y=160, width=100)
        self.return_book = tkinter.Button(self.frame_2, text='Return Book', font=(cs.font_1, 12), bd=2, command=self.ReturnBook, cursor="hand2", bg=cs.color_2, fg=cs.color_3).place(x=50, y=220, width=100)

        # New Buttons
        self.add_student = tkinter.Button(self.frame_2, text="Add Student", font=(cs.font_1, 12), bd=2, command=self.AddNewStudent, cursor="hand2", bg=cs.color_2, fg=cs.color_3).place(x=170, y=40, width=120)
        self.manage_categories = tkinter.Button(self.frame_2, text="Categories", font=(cs.font_1, 12), bd=2, command=self.ManageCategories, cursor="hand2", bg=cs.color_2, fg=cs.color_3).place(x=170, y=100, width=120)
        self.manage_fines = tkinter.Button(self.frame_2, text="Fines", font=(cs.font_1, 12), bd=2, command=self.ManageFines, cursor="hand2", bg=cs.color_2, fg=cs.color_3).place(x=170, y=160, width=120)

        # Additional Buttons for Advanced Queries
        self.view_overdue = tkinter.Button(self.frame_2, text="Overdue Books", font=(cs.font_1, 12), bd=2, command=self.ViewOverdueBooks, cursor="hand2", bg=cs.color_2, fg=cs.color_3).place(x=50, y=280, width=120)
        self.view_cs_books = tkinter.Button(self.frame_2, text="CS Books", font=(cs.font_1, 12), bd=2, command=self.ViewBooksBorrowedByCS, cursor="hand2", bg=cs.color_2, fg=cs.color_3).place(x=170, y=220, width=120)


    # Add new book form
    def AddNewBook(self):
        self.ClearScreen()

        # Frame for adding a new book
        add_book_frame = tkinter.Frame(self.frame_1, bg=cs.color_1)
        add_book_frame.place(x=50, y=50, width=600, height=400)

        # ID Label and Entry
        id_label = tkinter.Label(add_book_frame, text='Book ID', font=(cs.font_1, 12), bg=cs.color_1)
        id_label.grid(row=0, column=0, padx=10, pady=10, sticky=tkinter.W)
        self.id_entry = tkinter.Entry(add_book_frame, font=(cs.font_1, 12))
        self.id_entry.grid(row=0, column=1, padx=10, pady=10)

        # Book Name Label and Entry
        bookname_label = tkinter.Label(add_book_frame, text='Book Name', font=(cs.font_1, 12), bg=cs.color_1)
        bookname_label.grid(row=1, column=0, padx=10, pady=10, sticky=tkinter.W)
        self.bookname_entry = tkinter.Entry(add_book_frame, font=(cs.font_1, 12))
        self.bookname_entry.grid(row=1, column=1, padx=10, pady=10)

        # Author Label and Entry
        author_label = tkinter.Label(add_book_frame, text='Author', font=(cs.font_1, 12), bg=cs.color_1)
        author_label.grid(row=2, column=0, padx=10, pady=10, sticky=tkinter.W)
        self.author_entry = tkinter.Entry(add_book_frame, font=(cs.font_1, 12))
        self.author_entry.grid(row=2, column=1, padx=10, pady=10)

        # Edition Label and Entry
        edition_label = tkinter.Label(add_book_frame, text='Edition', font=(cs.font_1, 12), bg=cs.color_1)
        edition_label.grid(row=3, column=0, padx=10, pady=10, sticky=tkinter.W)
        self.edition_entry = tkinter.Entry(add_book_frame, font=(cs.font_1, 12))
        self.edition_entry.grid(row=3, column=1, padx=10, pady=10)

        # Price Label and Entry
        price_label = tkinter.Label(add_book_frame, text='Price', font=(cs.font_1, 12), bg=cs.color_1)
        price_label.grid(row=4, column=0, padx=10, pady=10, sticky=tkinter.W)
        self.price_entry = tkinter.Entry(add_book_frame, font=(cs.font_1, 12))
        self.price_entry.grid(row=4, column=1, padx=10, pady=10)

        # Quantity Label and Entry
        qty_label = tkinter.Label(add_book_frame, text='Quantity', font=(cs.font_1, 12), bg=cs.color_1)
        qty_label.grid(row=5, column=0, padx=10, pady=10, sticky=tkinter.W)
        self.qty_entry = tkinter.Entry(add_book_frame, font=(cs.font_1, 12))
        self.qty_entry.grid(row=5, column=1, padx=10, pady=10)

        # Category Label and Dropdown
        category_label = tkinter.Label(add_book_frame, text="Category", font=(cs.font_1, 12), bg=cs.color_1)
        category_label.grid(row=6, column=0, padx=10, pady=10, sticky=tkinter.W)

        # Fetch categories from the database and populate the dropdown
        categories = self.get_categories_from_db()
        self.category_var = tkinter.StringVar()
        self.category_dropdown = ttk.Combobox(add_book_frame, textvariable=self.category_var, values=categories, font=(cs.font_1, 12))
        self.category_dropdown.grid(row=6, column=1, padx=10, pady=10)
        self.category_dropdown.current(0)  # Set default selection

        # Add Book Button
        add_button = tkinter.Button(add_book_frame, text='Add Book', font=(cs.font_1, 12), bg=cs.color_2, command=self.add_book_to_db)
        add_button.grid(row=7, column=0, columnspan=2, padx=10, pady=10)

    # Function to fetch categories from the database
    def get_categories_from_db(self):
        categories = []
        try:
            con = pymysql.connect(host=cr.host, user=cr.user, password=cr.password, database=cr.database)
            cursor = con.cursor()
            query = "SELECT category_name FROM Categories"
            cursor.execute(query)
            rows = cursor.fetchall()
            for row in rows:
                categories.append(row[0])
            con.close()
        except pymysql.Error as e:
            messagebox.showerror("Error", f"MySQL Error fetching categories: {e}")
        except Exception as e:
            messagebox.showerror("Error", f"Error fetching categories: {e}")
        return categories

    def add_book_to_db(self):
        book_id = self.id_entry.get()
        book_name = self.bookname_entry.get()
        author = self.author_entry.get()
        edition = self.edition_entry.get()
        price = self.price_entry.get()
        qty = self.qty_entry.get()

        category_name = self.category_var.get()

        # Get category_id from category_name
        category_id = self.get_category_id_from_name(category_name)

        if category_id is None:
            messagebox.showerror("Error", "Invalid category selected.")
            return

        if book_id == '' or book_name == '' or author == '' or edition == '' or price == '' or qty == '':
            messagebox.showerror('Error!', 'All Fields are required', parent=self.window)
        else:
            try:
                con = pymysql.connect(host=cr.host, user=cr.user, password=cr.password, database=cr.database)
                cursor = con.cursor()
                query = "insert into book_list (book_id, book_name, author, edition, price, qty, category_id) VALUES (%s,%s,%s,%s,%s,%s,%s)"
                cursor.execute(query, (book_id, book_name, author, edition, price, qty, category_id))
                con.commit()
                messagebox.showinfo('Success', 'Book added successfully')
                self.reset_fields()
                con.close()
            except pymysql.Error as e:
                messagebox.showerror("Error!", f"MySQL Error due to {str(e)}", parent=self.window)
            except Exception as e:
                messagebox.showerror("Error!", f"Error due to {str(e)}", parent=self.window)

    def get_category_id_from_name(self, category_name):
        try:
            con = pymysql.connect(host=cr.host, user=cr.user, password=cr.password, database=cr.database)
            cursor = con.cursor()
            query = "SELECT category_id FROM Categories WHERE category_name = %s"
            cursor.execute(query, (category_name,))
            row = cursor.fetchone()
            con.close()
            if row:
                return row[0]
            else:
                return None
        except pymysql.Error as e:
            messagebox.showerror("Error", f"MySQL Error fetching category ID: {e}")
            return None
        except Exception as e:
            messagebox.showerror("Error", f"Error fetching category ID: {e}")
            return None

    # Issue book form
    def IssueBook(self):
        self.ClearScreen()

        # Frame for issuing a book
        issue_book_frame = tkinter.Frame(self.frame_1, bg=cs.color_1)
        issue_book_frame.place(x=50, y=50, width=600, height=400)

        # Book ID Label and Entry
        book_id_label = tkinter.Label(issue_book_frame, text='Book ID', font=(cs.font_1, 12), bg=cs.color_1)
        book_id_label.grid(row=0, column=0, padx=10, pady=10, sticky=tkinter.W)
        self.book_id_entry = tkinter.Entry(issue_book_frame, font=(cs.font_1, 12))
        self.book_id_entry.grid(row=0, column=1, padx=10, pady=10)

        # Book Name Label and Entry
        book_name_label = tkinter.Label(issue_book_frame, text='Book Name', font=(cs.font_1, 12), bg=cs.color_1)
        book_name_label.grid(row=1, column=0, padx=10, pady=10, sticky=tkinter.W)
        self.book_name_entry = tkinter.Entry(issue_book_frame, font=(cs.font_1, 12))
        self.book_name_entry.grid(row=1, column=1, padx=10, pady=10)

        # Student ID Label and Entry
        stu_id_label = tkinter.Label(issue_book_frame, text="Student ID", font=(cs.font_1, 12), bg=cs.color_1)
        stu_id_label.grid(row=2, column=0, padx=10, pady=10, sticky=tkinter.W)
        self.stu_id_entry = tkinter.Entry(issue_book_frame, font=(cs.font_1, 12))
        self.stu_id_entry.grid(row=2, column=1, padx=10, pady=10)

        # Issue Date Label and Entry
        issue_date_label = tkinter.Label(issue_book_frame, text='Issue Date', font=(cs.font_1, 12), bg=cs.color_1)
        issue_date_label.grid(row=3, column=0, padx=10, pady=10, sticky=tkinter.W)
        self.issue_date_entry = tkinter.Entry(issue_book_frame, font=(cs.font_1, 12))
        self.issue_date_entry.grid(row=3, column=1, padx=10, pady=10)

        # Return Date Label and Entry
        return_date_label = tkinter.Label(issue_book_frame, text='Return Date', font=(cs.font_1, 12), bg=cs.color_1)
        return_date_label.grid(row=4, column=0, padx=10, pady=10, sticky=tkinter.W)
        self.return_date_entry = tkinter.Entry(issue_book_frame, font=(cs.font_1, 12))
        self.return_date_entry.grid(row=4, column=1, padx=10, pady=10)

        # Issue Book Button
        issue_button = tkinter.Button(issue_book_frame, text='Issue Book', font=(cs.font_1, 12), bg=cs.color_2, command=self.issue_book_to_db)
        issue_button.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

    def issue_book_to_db(self):
        book_id = self.book_id_entry.get()
        book_name = self.book_name_entry.get()
        student_id = self.stu_id_entry.get()  # Get student_id
        issue_date = self.issue_date_entry.get()
        return_date = self.return_date_entry.get()

        if not book_id or not book_name or not student_id or not issue_date or not return_date:
            messagebox.showerror("Error", "Please fill in all fields.")
            return

        try:
            student_id = int(student_id)  # Convert student_id to integer
            con = pymysql.connect(host=cr.host, user=cr.user, password=cr.password, database=cr.database)
            cursor = con.cursor()
            query = "INSERT INTO borrow_record (book_id, student_id, issue_date, return_date) VALUES (%s, %s, %s, %s)"
            cursor.execute(query, (book_id, student_id, issue_date, return_date))
            con.commit()
            messagebox.showinfo('Done!', "The data has been submitted")
            self.reset_issuebook_fields()
            con.close()
        except ValueError:
            messagebox.showerror("Error", "Invalid Student ID. Please enter a number.")
        except pymysql.Error as e:
            messagebox.showerror("Error!", f"MySQL Error due to {str(e)}", parent=self.window)
        except Exception as e:
            messagebox.showerror("Error!", f"Error due to {str(e)}", parent=self.window)

    # Reset all the entry fields of add new book form
    def reset_fields(self):
        self.id_entry.delete(0, tkinter.END)
        self.bookname_entry.delete(0, tkinter.END)
        self.author_entry.delete(0, tkinter.END)
        self.edition_entry.delete(0, tkinter.END)
        self.price_entry.delete(0, tkinter.END)
        self.qty_entry.delete(0, tkinter.END)

    # Reset all the entry fields issue a book form
    def reset_issuebook_fields(self):
        self.book_id_entry.delete(0, tkinter.END)
        self.book_name_entry.delete(0, tkinter.END)
        self.stu_id_entry.delete(0, tkinter.END)  # Reset student_id field
        self.issue_date_entry.delete(0, tkinter.END)
        self.return_date_entry.delete(0, tkinter.END)

    # Removes all widgets from the frame 1 and frame 3
    def ClearScreen(self):
        for widget in self.frame_1.winfo_children():
            widget.destroy()
        for widget in self.frame_3.winfo_children():
            widget.destroy()

    '''Exit window'''
    def Exit(self):
        Exit = messagebox.askyesno("Library Management System", "Do you want to exit?")
        if Exit > 0:
            self.window.destroy()
            return

    # View book form
    def ViewBook(self):
        self.ClearScreen()

        # Frame for viewing books
        view_book_frame = tkinter.Frame(self.frame_1, bg=cs.color_1)
        view_book_frame.place(x=10, y=10, width=720, height=620)

        # Heading inside the frame
        heading_label = tkinter.Label(view_book_frame, text='View Books', font=(cs.font_1, 20, 'bold'), bg=cs.color_1)
        heading_label.pack(pady=10)

        # Search Frame
        search_frame = tkinter.Frame(view_book_frame, bg=cs.color_1)
        search_frame.place(x=10, y=50, width=700, height=40)

        search_label = tkinter.Label(search_frame, text="Search:", font=(cs.font_1, 12), bg=cs.color_1)
        search_label.grid(row=0, column=0, padx=5, pady=5, sticky=tkinter.W)

        self.search_entry = tkinter.Entry(search_frame, font=(cs.font_1, 12))
        self.search_entry.grid(row=0, column=1, padx=5, pady=5, sticky=tkinter.W)

        search_button = tkinter.Button(search_frame, text="Search", font=(cs.font_1, 12), bg=cs.color_2, command=self.search_books)
        search_button.grid(row=0, column=2, padx=5, pady=5, sticky=tkinter.W)

        # Table Frame
        table_frame = tkinter.Frame(view_book_frame, bg='white')
        table_frame.place(x=10, y=90, width=700, height=470)

        # Scroll Bar
        table_scroll = tkinter.Scrollbar(table_frame)
        table_scroll.pack(side=tkinter.RIGHT, fill=tkinter.Y)

        # Tree View For Table
        self.book_table = ttk.Treeview(table_frame, columns=('book_id', 'book_name', 'author', 'edition', 'price', 'qty', 'category_name'), yscrollcommand=table_scroll.set)
        self.book_table.pack(fill=tkinter.BOTH, expand=1)
        table_scroll.config(command=self.book_table.yview)

        # Set Heading of the Table
        self.book_table.heading('book_id', text='Book ID')
        self.book_table.heading('book_name', text='Book Name')
        self.book_table.heading('author', text='Author')
        self.book_table.heading('edition', text='Edition')
        self.book_table.heading('price', text='Price')
        self.book_table.heading('qty', text='Quantity')
        self.book_table.heading('category_name', text='Category')

        # Show Data
        self.show_books()

    def show_books(self):
        # Clear existing data in the table
        for item in self.book_table.get_children():
            self.book_table.delete(item)

        try:
            con = pymysql.connect(host=cr.host, user=cr.user, password=cr.password, database=cr.database)
            cursor = con.cursor()
            query = """
            SELECT 
                b.book_id, 
                b.book_name, 
                b.author, 
                b.edition, 
                b.price, 
                b.qty, 
                c.category_name
            FROM 
                book_list b
            LEFT JOIN 
                Categories c ON b.category_id = c.category_id
            """
            cursor.execute(query)
            data = cursor.fetchall()

            for row in data:
                self.book_table.insert('', tkinter.END, values=row)

            con.close()
        except pymysql.Error as e:
            messagebox.showerror("Error", f"MySQL Error fetching books: {e}")
        except Exception as e:
            messagebox.showerror("Error", f"Error fetching books: {e}")

    def search_books(self):
        search_term = self.search_entry.get()
        # Clear existing data in the table
        for item in self.book_table.get_children():
            self.book_table.delete(item)

        try:
            con = pymysql.connect(host=cr.host, user=cr.user, password=cr.password, database=cr.database)
            cursor = con.cursor()
            query = """
            SELECT 
                b.book_id, 
                b.book_name, 
                b.author, 
                b.edition, 
                b.price, 
                b.qty, 
                c.category_name
            FROM 
                book_list b
            LEFT JOIN 
                Categories c ON b.category_id = c.category_id
            WHERE 
                b.book_name LIKE %s OR b.author LIKE %s
            """
            cursor.execute(query, ('%' + search_term + '%', '%' + search_term + '%'))
            data = cursor.fetchall()

            for row in data:
                self.book_table.insert('', tkinter.END, values=row)

            con.close()
        except pymysql.Error as e:
            messagebox.showerror("Error", f"MySQL Error fetching books: {e}")
        except Exception as e:
            messagebox.showerror("Error", f"Error fetching books: {e}")

    # Return book form
    def ReturnBook(self):
        self.ClearScreen()

        # Frame for returning books
        return_book_frame = tkinter.Frame(self.frame_1, bg=cs.color_1)
        return_book_frame.place(x=50, y=50, width=600, height=400)

        # Book ID Label and Entry
        book_id_label = tkinter.Label(return_book_frame, text='Book ID', font=(cs.font_1, 12), bg=cs.color_1)
        book_id_label.grid(row=0, column=0, padx=10, pady=10, sticky=tkinter.W)
        self.return_book_id_entry = tkinter.Entry(return_book_frame, font=(cs.font_1, 12))
        self.return_book_id_entry.grid(row=0, column=1, padx=10, pady=10)

        # Student ID Label and Entry
        stu_id_label = tkinter.Label(return_book_frame, text="Student ID", font=(cs.font_1, 12), bg=cs.color_1)
        stu_id_label.grid(row=1, column=0, padx=10, pady=10, sticky=tkinter.W)
        self.return_stu_id_entry = tkinter.Entry(return_book_frame, font=(cs.font_1, 12))
        self.return_stu_id_entry.grid(row=1, column=1, padx=10, pady=10)

        # Return Date Label and Entry
        return_date_label = tkinter.Label(return_book_frame, text='Return Date', font=(cs.font_1, 12), bg=cs.color_1)
        return_date_label.grid(row=2, column=0, padx=10, pady=10, sticky=tkinter.W)
        self.return_return_date_entry = tkinter.Entry(return_book_frame, font=(cs.font_1, 12))
        self.return_return_date_entry.grid(row=2, column=1, padx=10, pady=10)

        # Return Book Button
        return_button = tkinter.Button(return_book_frame, text='Return Book', font=(cs.font_1, 12), bg=cs.color_2, command=self.return_book_to_db)
        return_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

    def return_book_to_db(self):
        book_id = self.return_book_id_entry.get()
        student_id = self.return_stu_id_entry.get()
        return_date = self.return_return_date_entry.get()

        if not book_id or not student_id or not return_date:
            messagebox.showerror("Error", "Please fill in all fields.")
            return

        try:
            student_id = int(student_id)  # Convert student_id to integer
            con = pymysql.connect(host=cr.host, user=cr.user, password=cr.password, database=cr.database)
            cursor = con.cursor()
            # Assuming you have a way to identify the borrow record (e.g., using book_id and student_id)
            query = "DELETE FROM borrow_record WHERE book_id = %s AND student_id = %s"
            cursor.execute(query, (book_id, student_id))
            con.commit()
            messagebox.showinfo('Done!', "Book returned successfully.")
            self.reset_return_book_fields()
            con.close()
        except ValueError:
            messagebox.showerror("Error", "Invalid Student ID. Please enter a number.")
        except pymysql.Error as e:
            messagebox.showerror("Error!", f"MySQL Error due to {str(e)}", parent=self.window)
        except Exception as e:
            messagebox.showerror("Error!", f"Error due to {str(e)}", parent=self.window)

    def reset_return_book_fields(self):
        self.return_book_id_entry.delete(0, tkinter.END)
        self.return_stu_id_entry.delete(0, tkinter.END)
        self.return_return_date_entry.delete(0, tkinter.END)


    # Add new student form
    def AddNewStudent(self):
        self.ClearScreen()

        # Frame for adding a new student
        add_student_frame = tkinter.Frame(self.frame_1, bg=cs.color_1)
        add_student_frame.place(x=50, y=50, width=600, height=400)

        # Labels and Entry fields
        student_name_label = tkinter.Label(add_student_frame, text="Student Name", font=(cs.font_1, 12), bg=cs.color_1)
        student_name_label.grid(row=0, column=0, padx=10, pady=10, sticky=tkinter.W)
        self.student_name_entry = tkinter.Entry(add_student_frame, font=(cs.font_1, 12))
        self.student_name_entry.grid(row=0, column=1, padx=10, pady=10)

        department_label = tkinter.Label(add_student_frame, text="Department", font=(cs.font_1, 12), bg=cs.color_1)
        department_label.grid(row=1, column=0, padx=10, pady=10, sticky=tkinter.W)
        self.department_entry = tkinter.Entry(add_student_frame, font=(cs.font_1, 12))
        self.department_entry.grid(row=1, column=1, padx=10, pady=10)

        enrollment_year_label = tkinter.Label(add_student_frame, text="Enrollment Year", font=(cs.font_1, 12), bg=cs.color_1)
        enrollment_year_label.grid(row=2, column=0, padx=10, pady=10, sticky=tkinter.W)
        self.enrollment_year_entry = tkinter.Entry(add_student_frame, font=(cs.font_1, 12))
        self.enrollment_year_entry.grid(row=2, column=1, padx=10, pady=10)

        # Add Student Button
        add_button = tkinter.Button(add_student_frame, text="Add Student", font=(cs.font_1, 12), bg=cs.color_2, command=self.add_student_to_db)
        add_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

    def add_student_to_db(self):
        student_name = self.student_name_entry.get()
        department = self.department_entry.get()
        enrollment_year = self.enrollment_year_entry.get()

        if not student_name or not department or not enrollment_year:
            messagebox.showerror("Error", "Please fill in all fields.")
            return

        try:
            enrollment_year = int(enrollment_year)  # Convert to integer
            con = pymysql.connect(host=cr.host, user=cr.user, password=cr.password, database=cr.database)
            cursor = con.cursor()
            query = "INSERT INTO Students (student_name, department, enrollment_year) VALUES (%s, %s, %s)"
            cursor.execute(query, (student_name, department, enrollment_year))
            con.commit()
            con.close()
            messagebox.showinfo("Success", "Student added successfully!")
            self.reset_student_fields()  # Assuming you have a reset function
        except ValueError:
            messagebox.showerror("Error", "Invalid enrollment year. Please enter a number.")
        except pymysql.Error as e:
            messagebox.showerror("Error", f"MySQL Error adding student: {e}")
        except Exception as e:
            messagebox.showerror("Error", f"Error adding student: {e}")

    def reset_student_fields(self):
        self.student_name_entry.delete(0, tkinter.END)
        self.department_entry.delete(0, tkinter.END)
        self.enrollment_year_entry.delete(0, tkinter.END)

    # Manage Categories Form
    def ManageCategories(self):
        self.ClearScreen()

        # Frame for managing categories
        category_frame = tkinter.Frame(self.frame_1, bg=cs.color_1)
        category_frame.place(x=50, y=50, width=600, height=400)

        # Category Name Label and Entry
        category_name_label = tkinter.Label(category_frame, text="Category Name", font=(cs.font_1, 12), bg=cs.color_1)
        category_name_label.grid(row=0, column=0, padx=10, pady=10, sticky=tkinter.W)
        self.category_name_entry = tkinter.Entry(category_frame, font=(cs.font_1, 12))
        self.category_name_entry.grid(row=0, column=1, padx=10, pady=10)

        # Add Category Button
        add_category_button = tkinter.Button(category_frame, text="Add Category", font=(cs.font_1, 12), bg=cs.color_2, command=self.add_category_to_db)
        add_category_button.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

        # Table Frame
        table_frame = tkinter.Frame(category_frame, bg='white')
        table_frame.place(x=10, y=100, width=580, height=290)

        # Scroll Bar
        table_scroll = tkinter.Scrollbar(table_frame)
        table_scroll.pack(side=tkinter.RIGHT, fill=tkinter.Y)

        # Tree View For Table
        self.category_table = ttk.Treeview(table_frame, columns=('category_id', 'category_name'), yscrollcommand=table_scroll.set)
        self.category_table.pack(fill=tkinter.BOTH, expand=1)
        table_scroll.config(command=self.category_table.yview)

        # Set Heading of the Table
        self.category_table.heading('category_id', text='Category ID')
        self.category_table.heading('category_name', text='Category Name')

        # Show Data
        self.show_categories()

    def add_category_to_db(self):
        category_name = self.category_name_entry.get()

        if not category_name:
            messagebox.showerror("Error", "Please enter a category name.")
            return

        try:
            con = pymysql.connect(host=cr.host, user=cr.user, password=cr.password, database=cr.database)
            cursor = con.cursor()
            query = "INSERT INTO Categories (category_name) VALUES (%s)"
            cursor.execute(query, (category_name,))
            con.commit()
            con.close()
            messagebox.showinfo("Success", "Category added successfully!")
            self.clear_category_field()
            self.show_categories()
        except pymysql.Error as e:
            messagebox.showerror("Error", f"MySQL Error adding category: {e}")
        except Exception as e:
            messagebox.showerror("Error", f"Error adding category: {e}")

    def show_categories(self):
        # Clear existing data in the table
        for item in self.category_table.get_children():
            self.category_table.delete(item)

        try:
            con = pymysql.connect(host=cr.host, user=cr.user, password=cr.password, database=cr.database)
            cursor = con.cursor()
            query = "SELECT * FROM Categories"
            cursor.execute(query)
            data = cursor.fetchall()

            for values in data:
                self.category_table.insert('', tkinter.END, values=values)

            con.close()
        except pymysql.Error as e:
            messagebox.showerror("Error", f"MySQL Error fetching categories: {e}")
        except Exception as e:
            messagebox.showerror("Error", f"Error fetching categories: {e}")

    def clear_category_field(self):
        self.category_name_entry.delete(0, tkinter.END)

    # Manage Fines Form
    def ManageFines(self):
        self.ClearScreen()

        # Frame for managing fines
        fines_frame = tkinter.Frame(self.frame_1, bg=cs.color_1)
        fines_frame.place(x=50, y=50, width=600, height=400)

        # Student ID Label and Entry
        student_id_label = tkinter.Label(fines_frame, text="Student ID", font=(cs.font_1, 12), bg=cs.color_1)
        student_id_label.grid(row=0, column=0, padx=10, pady=10, sticky=tkinter.W)
        self.fine_student_id_entry = tkinter.Entry(fines_frame, font=(cs.font_1, 12))
        self.fine_student_id_entry.grid(row=0, column=1, padx=10, pady=10)

        # Book ID Label and Entry
        book_id_label = tkinter.Label(fines_frame, text="Book ID", font=(cs.font_1, 12), bg=cs.color_1)
        book_id_label.grid(row=1, column=0, padx=10, pady=10, sticky=tkinter.W)
        self.fine_book_id_entry = tkinter.Entry(fines_frame, font=(cs.font_1, 12))
        self.fine_book_id_entry.grid(row=1, column=1, padx=10, pady=10)

        # Fine Amount Label and Entry
        fine_amount_label = tkinter.Label(fines_frame, text="Fine Amount", font=(cs.font_1, 12), bg=cs.color_1)
        fine_amount_label.grid(row=2, column=0, padx=10, pady=10, sticky=tkinter.W)
        self.fine_amount_entry = tkinter.Entry(fines_frame, font=(cs.font_1, 12))
        self.fine_amount_entry.grid(row=2, column=1, padx=10, pady=10)

        # Fine Date Label and Entry
        fine_date_label = tkinter.Label(fines_frame, text="Fine Date", font=(cs.font_1, 12), bg=cs.color_1)
        fine_date_label.grid(row=3, column=0, padx=10, pady=10, sticky=tkinter.W)
        self.fine_date_entry = tkinter.Entry(fines_frame, font=(cs.font_1, 12))
        self.fine_date_entry.grid(row=3, column=1, padx=10, pady=10)

        # Payment Status Label and Dropdown
        payment_status_label = tkinter.Label(fines_frame, text="Payment Status", font=(cs.font_1, 12), bg=cs.color_1)
        payment_status_label.grid(row=4, column=0, padx=10, pady=10, sticky=tkinter.W)
        self.payment_status_var = tkinter.StringVar()
        self.payment_status_dropdown = ttk.Combobox(fines_frame, textvariable=self.payment_status_var, values=["Unpaid", "Paid"], font=(cs.font_1, 12))
        self.payment_status_dropdown.grid(row=4, column=1, padx=10, pady=10)
        self.payment_status_dropdown.current(0)  # Default to "Unpaid"

        # Add Fine Button
        add_fine_button = tkinter.Button(fines_frame, text="Add Fine", font=(cs.font_1, 12), bg=cs.color_2, command=self.add_fine_to_db)
        add_fine_button.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

        # Table Frame
        table_frame = tkinter.Frame(fines_frame, bg='white')
        table_frame.place(x=80, y=300, width=580, height=190)

        # Scroll Bars
        y_scroll = tkinter.Scrollbar(table_frame, orient=tkinter.VERTICAL)
        x_scroll = tkinter.Scrollbar(table_frame, orient=tkinter.HORIZONTAL)
        y_scroll.pack(side=tkinter.RIGHT, fill=tkinter.Y)
        x_scroll.pack(side=tkinter.BOTTOM, fill=tkinter.X)

        # Tree View For Table
        self.fines_table = ttk.Treeview(
            table_frame,
            columns=('fine_id', 'student_id', 'book_id', 'fine_amount', 'fine_date', 'payment_status'),
            yscrollcommand=y_scroll.set,
            xscrollcommand=x_scroll.set
        )
        self.fines_table.pack(fill=tkinter.BOTH, expand=1)

        y_scroll.config(command=self.fines_table.yview)
        x_scroll.config(command=self.fines_table.xview)

        # Set Heading of the Table
        self.fines_table.heading('fine_id', text='Fine ID')
        self.fines_table.heading('student_id', text='Student ID')
        self.fines_table.heading('book_id', text='Book ID')
        self.fines_table.heading('fine_amount', text='Fine Amount')
        self.fines_table.heading('fine_date', text='Fine Date')
        self.fines_table.heading('payment_status', text='Payment Status')

        # Show Data
        self.show_fines()

    def add_fine_to_db(self):
        student_id = self.fine_student_id_entry.get()
        book_id = self.fine_book_id_entry.get()
        fine_amount = self.fine_amount_entry.get()
        fine_date = self.fine_date_entry.get()
        payment_status = self.payment_status_var.get()

        if not student_id or not book_id or not fine_amount or not fine_date:
            messagebox.showerror("Error", "Please fill in all fields.")
            return

        try:
            student_id = int(student_id)
            fine_amount = float(fine_amount)
            # Basic date format check (you might want to use a more robust date validation)
            if len(fine_date) != 10 or fine_date[4] != '-' or fine_date[7] != '-':
                messagebox.showerror("Error", "Invalid date format. Please use YYYY-MM-DD.")
                return

            con = pymysql.connect(host=cr.host, user=cr.user, password=cr.password, database=cr.database)
            cursor = con.cursor()
            query = "INSERT INTO Fines (student_id, book_id, fine_amount, fine_date, payment_status) VALUES (%s, %s, %s, %s, %s)"
            cursor.execute(query, (student_id, book_id, fine_amount, fine_date, payment_status))
            con.commit()
            con.close()
            messagebox.showinfo("Success", "Fine added successfully!")
            self.clear_fine_fields()
            self.show_fines()
        except ValueError:
            messagebox.showerror("Error", "Invalid Student ID or Fine Amount. Please enter numbers.")
        except pymysql.Error as e:
            messagebox.showerror("Error", f"MySQL Error adding fine: {e}")
        except Exception as e:
            messagebox.showerror("Error", f"Error adding fine: {e}")

    def show_fines(self):
        # Clear existing data in the table
        for item in self.fines_table.get_children():
            self.fines_table.delete(item)

        try:
            con = pymysql.connect(host=cr.host, user=cr.user, password=cr.password, database=cr.database)
            cursor = con.cursor()
            query = "SELECT fine_id, student_id, book_id, fine_amount, fine_date, payment_status FROM Fines"  # Explicit column list
            cursor.execute(query)
            data = cursor.fetchall()

            for values in data:
                self.fines_table.insert('', tkinter.END, values=values)

            con.close()
        except pymysql.Error as e:
            messagebox.showerror("Error", f"MySQL Error fetching fines: {e}")
        except Exception as e:
            messagebox.showerror("Error", f"Error fetching fines: {e}")

    def clear_fine_fields(self):
        self.fine_student_id_entry.delete(0, tkinter.END)
        self.fine_book_id_entry.delete(0, tkinter.END)
        self.fine_amount_entry.delete(0, tkinter.END)
        self.fine_date_entry.delete(0, tkinter.END)
        self.payment_status_dropdown.current(0)  # Reset to "Unpaid"

    # View Overdue Books
    def ViewOverdueBooks(self):
        self.ClearScreen()
        # ... GUI setup ...
        # Frame for viewing overdue books
        overdue_book_frame = tkinter.Frame(self.frame_1, bg=cs.color_1)
        overdue_book_frame.place(x=10, y=10, width=720, height=620)

        # Heading inside the frame
        heading_label = tkinter.Label(overdue_book_frame, text='View Overdue Books', font=(cs.font_1, 20, 'bold'), bg=cs.color_1)
        heading_label.pack(pady=10)

        # Table Frame
        table_frame = tkinter.Frame(overdue_book_frame, bg='white')
        table_frame.place(x=10, y=60, width=700, height=500)

        # Scroll Bar
        table_scroll = tkinter.Scrollbar(table_frame)
        table_scroll.pack(side=tkinter.RIGHT, fill=tkinter.Y)

        # Tree View For Table
        self.overdue_table = ttk.Treeview(table_frame, columns=('book_name', 'student_name', 'return_date'), yscrollcommand=table_scroll.set)
        self.overdue_table.pack(fill=tkinter.BOTH, expand=1)
        table_scroll.config(command=self.overdue_table.yview)

        # Set Heading of the Table
        self.overdue_table.heading('book_name', text='Book Name')
        self.overdue_table.heading('student_name', text='Student Name')
        self.overdue_table.heading('return_date', text='Return Date')

        try:
            con = pymysql.connect(host=cr.host, user=cr.user, password=cr.password, database=cr.database)
            cursor = con.cursor()
            query = """
            SELECT 
                b.book_name, 
                s.student_name, 
                br.return_date
            FROM 
                book_list b
            JOIN 
                borrow_record br ON b.book_id = br.book_id
            JOIN 
                Students s ON br.student_id = s.student_id
            WHERE 
                br.return_date < CURDATE()
            """
            cursor.execute(query)
            data = cursor.fetchall()

            for row in data:
                self.overdue_table.insert('', tkinter.END, values=row)

            con.close()
        except pymysql.Error as e:
            messagebox.showerror("Error", f"MySQL Error fetching overdue books: {e}")
        except Exception as e:
            messagebox.showerror("Error", f"Error fetching overdue books: {e}")

    # View Books Borrowed by Computer Science Students
    def ViewBooksBorrowedByCS(self):
        self.ClearScreen()
        # ... GUI setup ...
        # Frame for viewing books borrowed by CS students
        cs_books_frame = tkinter.Frame(self.frame_1, bg=cs.color_1)
        cs_books_frame.place(x=10, y=10, width=720, height=620)

        # Heading inside the frame
        heading_label = tkinter.Label(cs_books_frame, text='Books Borrowed by CS Students', font=(cs.font_1, 20, 'bold'), bg=cs.color_1)
        heading_label.pack(pady=10)

        # Table Frame
        table_frame = tkinter.Frame(cs_books_frame, bg='white')
        table_frame.place(x=10, y=60, width=700, height=500)

        # Scroll Bar
        table_scroll = tkinter.Scrollbar(table_frame)
        table_scroll.pack(side=tkinter.RIGHT, fill=tkinter.Y)

        # Tree View For Table
        self.cs_books_table = ttk.Treeview(table_frame, columns=('book_name',), yscrollcommand=table_scroll.set)
        self.cs_books_table.pack(fill=tkinter.BOTH, expand=1)
        table_scroll.config(command=self.cs_books_table.yview)

        # Set Heading of the Table
        self.cs_books_table.heading('book_name', text='Book Name')

        try:
            con = pymysql.connect(host=cr.host, user=cr.user, password=cr.password, database=cr.database)
            cursor = con.cursor()
            query = """
            SELECT 
                b.book_name
            FROM 
                book_list b
            WHERE 
                b.book_id IN (
                    SELECT 
                        br.book_id
                    FROM 
                        borrow_record br
                    WHERE 
                        br.student_id IN (
                            SELECT 
                                s.student_id
                            FROM 
                                Students s
                            WHERE 
                                s.department = 'Computer Science'
                        )
                )
            """
            cursor.execute(query)
            data = cursor.fetchall()

            for row in data:
                self.cs_books_table.insert('', tkinter.END, values=row)

            con.close()
        except pymysql.Error as e:
            messagebox.showerror("Error", f"MySQL Error fetching books: {e}")
        except Exception as e:
            messagebox.showerror("Error", f"Error fetching books: {e}")

# Starting the GUI
if __name__ == "__main__":
    window = tkinter.Tk()
    Management(window)
    window.mainloop()