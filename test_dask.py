import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from tkinter.constants import BOTTOM, RIGHT
from tkinter import font as fontTk
#import pandas as pd
import dask.dataframe as dd
import dask.array as da
import dask.bag as db



root = tk.Tk()
root.geometry("750x600")
root.pack_propagate(False)
root.resizable(0, 0)

# Mise en place de la police
f = fontTk.Font(family='Comic Sans MS')

frame1 = tk.LabelFrame(root, text="Affichage des données")
frame1['font'] = f
frame1.place(height=308, width=600)

file_frame = tk.LabelFrame(root, text="Ouvrir")
file_frame['font'] = f
file_frame.place(height = 150, width = 400, rely= 0.65, relx = 0)

btn1 = tk.Button(file_frame, text="Rechercher", bg="blue", command=lambda: File_dialog())
btn1['font'] = f
btn1.place(rely=0.65, relx=0.53)

btn2 = tk.Button(file_frame, text="Charger", bg="green", command=lambda: Load_excel_data())
btn2['font'] = f
btn2.place(rely=0.65, relx=0.27)

btnQuit = tk.Button(root, text="Quitter", bg="red", command=lambda: close_window())
btnQuit['font'] = f
btnQuit.place(rely=0.92, relx=0.85)


label_file = ttk.Label(file_frame, text="Aucun fichier selectionné")
label_file['font'] = f
label_file.place(rely=0, relx=0)

tv1 = ttk.Treeview(frame1)
#tv1['font'] = f
tv1.place(relheight=1, relwidth=1)

treescrolly = tk.Scrollbar(frame1, orient="vertical", command=tv1.yview)
treescrollx = tk.Scrollbar(frame1, orient="horizontal", command=tv1.xview)
tv1.configure(xscrollcommand=treescrollx.set, yscrollcommand=treescrolly.set)
treescrollx.pack(side="bottom", fill="x")
treescrolly.pack(side="right", fill="y")

def close_window():
    root.destroy()

def File_dialog():
	filename = filedialog.askopenfilename(initialdir="~", title="Selectionner un fichier", filetypes=(("csv files", "*.csv"),("JSON files", "*.json"),("xlsx files", "*.xlsx"),("Tous les fichiers", "*.*")))
	print(filename)
	
	label_file["text"] = filename
	return None

def Load_excel_data():
	file_path = label_file["text"]
	try:
		excel_filename = r"{}".format(file_path) 
		if excel_filename[-4:] == ".csv":
    		
			print("1")
			
			df = dd.read_csv(excel_filename)
			
			print("2")
		else:
			df = dd.to_json(excel_filename)

	except ValueError:
		tk.messagebox.showerror("Information", "Le fichier que vous avez choisi est invalide")
		return None
	except FileNotFoundError:
		tk.messagebox.showerror("Information", "Il n'y a pas de ficher dans {file_path}")

	print("3")
	clear_data()
	print("4")
	tv1["column"] = list(df.columns)
	tv1["show"] = "headings"
	print("5")
	for column in tv1["columns"]:
		tv1.heading(column, text=column)

	print("6")
	df_rows = df.to_bag()
	print("7")
	for row in df_rows:
    	
		tv1.insert("", "end", values=row)

	print("8")
		
		
	return None

		


def clear_data():
	tv1.delete(*tv1.get_children())
	return None

root.mainloop()