# Author :  Lila

from tkinter import *
import sqlite3

root = Tk()
root.title("Database")  
root.iconbitmap('assets/fire.ico')
root.geometry("400x600")

# Create a database or connect to one
conn = sqlite3.connect('address_book.db')

# Create cursor
c = conn.cursor()

    # Create table
    # c.execute("""CREATE TABLE addresses(
    #           first_name text,
    #           last_name text,
    #           address text,
    #           city text,
    #           state text,
    #           zipcode integer
    #           )""")

# Create text boxes
f_name = Entry(root, width=30)
f_name.grid(row=0, column=1, padx=20,pady=(10,2))
l_name = Entry(root, width=30)
l_name.grid(row=1, column=1)
address = Entry(root, width=30)
address.grid(row=2, column=1)
city = Entry(root, width=30)
city.grid(row=3, column=1)
state = Entry(root, width=30)
state.grid(row=4, column=1)
zipcode = Entry(root, width=30)
zipcode.grid(row=5, column=1)

delete_box = Entry(root,width=30)
delete_box.grid(row=9,column=1,pady=5)


# Create text box labels
f_name_label = Label(root, text="First name")
f_name_label.grid(row=0, column=0,pady=(10,2))
l_name_label = Label(root, text="Last name")
l_name_label.grid(row=1, column=0)
address_label = Label(root, text="Address")
address_label.grid(row=2, column=0)
city_label = Label(root, text="City")
city_label.grid(row=3, column=0)
state_label = Label(root, text="State")
state_label.grid(row=4, column=0)
zipcode_label = Label(root, text="Zipcode")
zipcode_label.grid(row=5, column=0)

delete_box_label = Label(root,text="Select ID")
delete_box_label.grid(row=9,column=0,pady=5)

# Create Query function
def query():
    # Create a database or connect to one
    conn = sqlite3.connect('address_book.db')

    # Create cursor
    c = conn.cursor()

    c.execute("SELECT *,oid FROM addresses")
    records = c.fetchall()
    # print(records)
    
    #  Loop through results
    print_records = ''
    for record in records:
        print_records += str(record[0]) +" " + str(record[1]) +" " + "\t" +str(record[6]) + "\n"

    query_label = Label(root,text=print_records)
    query_label.grid(row=12,column=0,columnspan=2)


    # Commit changes
    conn.commit()

    # Close Connection
    conn.close()

# Create function to delete a record
def delete():
    # Create a database or connect to one
    conn = sqlite3.connect('address_book.db')

    # Create cursor
    c = conn.cursor()

    # Execute DELETE statement
    c.execute("DELETE from addresses WHERE oid = " + delete_box.get())

    # Commit changes
    conn.commit()

    # Close Connection
    conn.close()

# Creating a update function
def update():
    # Create a database or connect to one
    conn = sqlite3.connect('address_book.db')

    # Create cursor
    c = conn.cursor()
    record_id = delete_box.get()

    c.execute("""UPDATE addresses SET 
              first_name = :first,
              last_name = :last,
              address = :address,
              city = :city,
              state = :state,
              zipcode = :zipcode

              WHERE oid = :oid""",
              {
                  'first': f_name_editor.get(),
                  'last': l_name_editor.get(),
                  'address': address_editor.get(),
                  'city': city_editor.get(),
                  'state': state_editor.get(),
                  'zipcode': zipcode_editor.get(),
                  'oid': record_id
              })

    # Commit changes
    conn.commit()

    # Close Connection
    conn.close()

    editor.destroy()




# Create edit function to update a record
def edit():
    global editor
    editor = Tk()
    editor.title("Edit a Record")  
    editor.iconbitmap('assets/fire.ico')
    editor.geometry("400x600")

    # Create a database or connect to one
    conn = sqlite3.connect('address_book.db')

    # Create cursor
    c = conn.cursor()

    record_id = delete_box.get()
    c.execute("SELECT * FROM addresses WHERE oid = " + record_id)
    records = c.fetchall()

    # Creating global variables for text box names
    global f_name_editor
    global l_name_editor
    global address_editor
    global city_editor
    global state_editor
    global zipcode_editor

    # Create text boxes
    f_name_editor = Entry(editor, width=30)
    f_name_editor.grid(row=0, column=1, padx=20,pady=(10,2))
    l_name_editor = Entry(editor, width=30)
    l_name_editor.grid(row=1, column=1)
    address_editor = Entry(editor, width=30)
    address_editor.grid(row=2, column=1)
    city_editor = Entry(editor, width=30)
    city_editor.grid(row=3, column=1)
    state_editor = Entry(editor, width=30)
    state_editor.grid(row=4, column=1)
    zipcode_editor = Entry(editor, width=30)
    zipcode_editor.grid(row=5, column=1)

    # Create text box labels
    f_name_label = Label(editor, text="First name")
    f_name_label.grid(row=0, column=0,pady=(10,2))
    l_name_label = Label(editor, text="Last name")
    l_name_label.grid(row=1, column=0)
    address_label = Label(editor, text="Address")
    address_label.grid(row=2, column=0)
    city_label = Label(editor, text="City")
    city_label.grid(row=3, column=0)
    state_label = Label(editor, text="State")
    state_label.grid(row=4, column=0)
    zipcode_label = Label(editor, text="Zipcode")
    zipcode_label.grid(row=5, column=0)

    # Create a save Button to save edited record
    edit_btn = Button(editor, text="Save Record",command=update)
    edit_btn.grid(row=6, column=0, columnspan=2, padx=10, pady=10, ipadx=144)

    # Loop through results
    for record in records:
        f_name_editor.insert(0,record[0])
        l_name_editor.insert(0,record[1])
        address_editor.insert(0,record[2])
        city_editor.insert(0,record[3])
        state_editor.insert(0,record[4])
        zipcode_editor.insert(0,record[5])

    # Commit changes
    conn.commit()

    # Close Connection
    conn.close()


# Create submit function for database
def submit():
    # Create a database or connect to one
    conn = sqlite3.connect('address_book.db')

    # Create cursor
    c = conn.cursor()

    # Insert into table
    c.execute("INSERT INTO addresses VALUES (:f_name, :l_name, :u_address, :u_city, :s_state, :u_zipcode)",
    {'f_name': f_name.get(),
    'l_name': l_name.get(),
    'u_address': address.get(),
    'u_city': city.get(),
    's_state': state.get(),
    'u_zipcode': zipcode.get()
    })

    # Commit changes
    conn.commit()

    # Close Connection
    conn.close()

    # Clear text boxes
    f_name.delete(0, END)
    l_name.delete(0, END)
    address.delete(0, END)
    city.delete(0, END)
    state.delete(0, END)
    zipcode.delete(0, END)

# Create submit button
submit_btn = Button(root, text="Add Records", command=submit)
submit_btn.grid(row=6, column=0, columnspan=2, padx=10, pady=10, ipadx=138)

# Create show records button
query_btn = Button(root, text="Show Records", command=query)
query_btn.grid(row=7, column=0, columnspan=2, padx=10, pady=10, ipadx=136)

# Create a delete button
delete_btn = Button(root, text="Delete Record",command=delete)
delete_btn.grid(row=10, column=0, columnspan=2, padx=10, pady=10, ipadx=137)

# Create update button
edit_btn = Button(root, text="Edit Record",command=edit)
edit_btn.grid(row=11, column=0, columnspan=2, padx=10, pady=10, ipadx=143)

# Commit changes
conn.commit()

# Close Connection
conn.close()

root.mainloop()
