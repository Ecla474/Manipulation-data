# Importation des librairies
import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from tkinter.constants import BOTTOM, RIGHT
from tkinter import font as fontTk
import pandas as pd
import dask.dataframe as dd
import dask.array as da
import dask.bag as db


# Ferme la fenetre Tkinter
def close_window():
    root.destroy()

# Ouvre une nouvelle fenetre pour choisir le fichier data
def File_dialog():
	filename = filedialog.askopenfilename(initialdir="~/Bureau/Python", title="Selectionner un fichier", filetypes=(("csv files", "*.csv"),("JSON files", "*.json"),("xlsx files", "*.xlsx"),("Tous les fichiers", "*.*")))
	print(filename)
	
	label_file["text"] = filename
	return None



# Charge le fichier data choisi
def Load_excel_data():
	file_path = label_file["text"]
	try:

		excel_filename = r"{}".format(file_path) 
		print(excel_filename[-5:])
		print("1")

		if excel_filename[-4:] == ".csv":
			df = pd.read_csv(excel_filename)
			label_file_csv = ttk.Label(file_frame, text="Fichier CSV chargé !")
			label_file_csv['font'] = f
			label_file_csv.place(rely=0.2, relx=0)


		else:
			tk.messagebox.showerror("Information", "Le format que vous avez choisi est invalide")



	except ValueError:
		tk.messagebox.showerror("Information", "Le fichier que vous avez choisi est invalide")
		return None

	except FileNotFoundError:
		tk.messagebox.showerror("Information", "Il n'y a pas de ficher dans {file_path}")

	clear_data()
	tv1["column"] = list(df.columns)
	tv1["show"] = "headings"

	ry = 0.52
	for column in tv1["columns"]:
		print(column)
		tv1.heading(column, text=column)
		btnCol = tk.Button(frame2, text="Afficher la colonne : " + column, command=lambda: affiche_colonne(column))
		btnCol['font'] = f
		btnCol.place(rely=ry, relx=0.03)
		ry = ry + 0.1

#	print("6")
	
#	df_rows = df.to_numpy().tolist()
#	print("7")

#	for row in df_rows:

#		print(row)
#		tv1.insert("", "end", values=row)
		
	
#		print("10")
	return df


def affiche_colonne(column):
	df = Load_excel_data()
	print(column)

	df2 = df[column]
	df_rows = df2.to_numpy().tolist()

	for row in df_rows:

		print(row)
		tv1.insert("", "end", values=row)
		
	return None

def affiche_5_premiers():

	df = Load_excel_data()

	df2 = df.head()
	df_rows = df2.to_numpy().tolist()

	for row in df_rows:

		print(row)
		tv1.insert("", "end", values=row)
		
	return None


def affiche_5_derniers():

	df = Load_excel_data()
	clear_data()

	df2 = df.tail()
	df_rows = df2.to_numpy().tolist()

	for row in df_rows:

		print(row)
		tv1.insert("", "end", values=row)
		
	return None

def affiche_tout():

	df = Load_excel_data()
	df_rows = df.to_numpy().tolist()
	print("7")

	for row in df_rows:

		print(row)
		tv1.insert("", "end", values=row)
		
	
#		print("10")
	return None

	
def description():

	df = Load_excel_data()
	df2 = df.describe()
	df_rows = df2.to_numpy().tolist()

	for row in df_rows:

		print(row)
		tv1.insert("", "end", values=row)
		
	return None

# Efface les données affichées
def clear_data():
	tv1.delete(*tv1.get_children())
	return None


root = tk.Tk()
root.geometry("1800x1000")
root.pack_propagate(False)
root.resizable(0, 0)


# Mise en place de la police

f = fontTk.Font(family='Comic Sans MS')


# Les differents affichages

frame1 = tk.LabelFrame(root, text="Affichage des données")
frame1['font'] = f
frame1.place(height=900, width=1280, relx = 0.25)


file_frame = tk.LabelFrame(root, text="Ouvrir")
file_frame['font'] = f
file_frame.place(height = 120, width = 400, rely= 0.01, relx = 0.01)

frame2 = tk.LabelFrame(root, text="Manipulation des données")
frame2['font'] = f
frame2.place(height = 350, width = 400, rely= 0.13, relx = 0.01)


# Les boutons

btn1 = tk.Button(file_frame, text="Rechercher", bg="blue", command=lambda: File_dialog())
btn1['font'] = f
btn1.place(rely=0.65, relx=0.53)

btn2 = tk.Button(file_frame, text="Charger", bg="green", command=lambda: Load_excel_data())
btn2['font'] = f
btn2.place(rely=0.65, relx=0.27)

btnClear = tk.Button(frame2, text="Effacer les données", command=lambda: clear_data())
btnClear['font'] = f
btnClear.place(rely=0.42, relx=0.03)

btn5prem = tk.Button(frame2, text="Afficher les 5 premieres données", command=lambda: affiche_5_premiers())
btn5prem['font'] = f
btn5prem.place(rely=0.12, relx=0.03)

btn5dern = tk.Button(frame2, text="Afficher les 5 dernieres données", command=lambda: affiche_5_derniers())
btn5dern['font'] = f
btn5dern.place(rely=0.22, relx=0.03)

btnAff = tk.Button(frame2, text="Afficher les données", command=lambda: affiche_tout())
btnAff['font'] = f
btnAff.place(rely=0.02, relx=0.03)

btnDescrp = tk.Button(frame2, text="Description des données", command=lambda: description())
btnDescrp['font'] = f
btnDescrp.place(rely=0.32, relx=0.03)

btnQuit = tk.Button(root, text="Quitter", bg="red", command=lambda: close_window())
btnQuit['font'] = f
btnQuit.place(rely=0.96, relx=0.9)

# Affichage d'un texte
label_file = ttk.Label(file_frame, text="Aucun fichier selectionné")
label_file['font'] = f
label_file.place(rely=0, relx=0)

tv1 = ttk.Treeview(frame1)
tv1.place(relheight=1, relwidth=1)




treescrolly = tk.Scrollbar(frame1, orient="vertical", command=tv1.yview)
treescrollx = tk.Scrollbar(frame1, orient="horizontal", command=tv1.xview)
tv1.configure(xscrollcommand=treescrollx.set, yscrollcommand=treescrolly.set)
treescrollx.pack(side="bottom", fill="x")
treescrolly.pack(side="right", fill="y")


root.mainloop()