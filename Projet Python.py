# Importation des librairies
import tkinter as tk
from tkinter import *
from tkinter import filedialog, messagebox, ttk
from tkinter.constants import BOTTOM, RIGHT
from tkinter import font as fontTk
from tkinter import Label
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

		if excel_filename[-4:] == ".csv":

			df = Load_csv_data(excel_filename)

		else:
			if excel_filename[-5:] == ".json":

				df = Load_json_data(excel_filename)

			else:
				tk.messagebox.showerror("Information", "Le format que vous avez choisi est invalide")



	except ValueError:
		tk.messagebox.showerror("Information", "Le fichier que vous avez choisi est invalide")
		return None

	except FileNotFoundError:
		tk.messagebox.showerror("Information", "Il n'y a pas de ficher dans {file_path}")

	return df



def Load_csv_data(excel_filename):

	df = pd.read_csv(excel_filename)
	label_file_csv = ttk.Label(file_frame, text="Fichier CSV chargé !")
	label_file_csv['font'] = f
	label_file_csv.place(rely=0.2, relx=0.36)

	clear_data()
	tv1["column"] = list(df.columns)
	tv1["show"] = "headings"


	ry = 0.02

	for column in tv1["columns"]:
		print(column)
		tv1.heading(column, text=column)

		btnCol = tk.Button(frame2, text="Colonne : " + column, command=lambda: affiche_colonne(column))
		btnCol['font'] = f
		btnCol.place(rely=ry, relx=0.4)

		btnGrp = tk.Button(frame2, text="Regrouper : " + column, command=lambda: affiche_colonne(column))
		btnGrp['font'] = f
		btnGrp.place(rely=ry, relx=0.7)

		ry = ry + 0.06

	return df

def Load_json_data(excel_filename):

	df = pd.read_json(excel_filename)
	label_file_json = ttk.Label(file_frame, text="Fichier JSON chargé !")
	label_file_json['font'] = f
	label_file_json.place(rely=0.2, relx=0)

	clear_data()
	tv1["column"] = list(df.columns)
	tv1["show"] = "headings"

	ry = 0.02

	for column in tv1["columns"]:
		print(column)
		tv1.heading(column, text=column)

		btnCol = tk.Button(frame2, text="Colonne : " + column, command=lambda: affiche_colonne(column))
		btnCol['font'] = f
		btnCol.place(rely=ry, relx=0.4)

		btnGrp = tk.Button(frame2, text="Regrouper : " + column, command=lambda: affiche_colonne(column))
		btnGrp['font'] = f
		btnGrp.place(rely=ry, relx=0.7)

		ry = ry + 0.06

	return df


def affiche_colonne(column):
	df = Load_excel_data()
	print(column)
	df2 = df[column]

	print(df2)

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
root.geometry("1800x900")
root.pack_propagate(False)
root.resizable(0, 0)


# Mise en place de la police

f = fontTk.Font(family='Comic Sans MS')


# Les differents affichages

frame1 = tk.LabelFrame(root, text="Affichage des données")
frame1['font'] = f
frame1.place(height=800, width=1000, relx = 0.44)


file_frame = tk.LabelFrame(root, text="Ouvrir")
file_frame['font'] = f
file_frame.place(height = 140, width = 400, rely= 0.01, relx = 0.01)

frame2 = tk.LabelFrame(root, text="Manipulation des données")
frame2['font'] = f
frame2.place(height = 700, width = 750, rely= 0.18, relx = 0.01)


# Les boutons

btn1 = tk.Button(file_frame, text="Rechercher", bg="blue", command=lambda: File_dialog())
btn1['font'] = f
btn1.place(rely=0.6, relx=0.53)

btn2 = tk.Button(file_frame, text="Charger", bg="green", command=lambda: Load_excel_data())
btn2['font'] = f
btn2.place(rely=0.6, relx=0.27)

btnClear = tk.Button(frame2, text="Effacer", command=lambda: clear_data())
btnClear['font'] = f
btnClear.place(rely=0.26, relx=0.03)

btn5prem = tk.Button(frame2, text="5 premieres données", command=lambda: affiche_5_premiers())
btn5prem['font'] = f
btn5prem.place(rely=0.08, relx=0.03)

btn5dern = tk.Button(frame2, text="5 dernieres données", command=lambda: affiche_5_derniers())
btn5dern['font'] = f
btn5dern.place(rely=0.14, relx=0.03)

btnAff = tk.Button(frame2, text="Tout afficher", command=lambda: affiche_tout())
btnAff['font'] = f
btnAff.place(rely=0.02, relx=0.03)

btnDescrp = tk.Button(frame2, text="Description", command=lambda: description())
btnDescrp['font'] = f
btnDescrp.place(rely=0.2, relx=0.03)

btnQuit = tk.Button(root, text="Quitter", bg="red", command=lambda: close_window())
btnQuit['font'] = f
btnQuit.place(rely=0.95, relx=0.92)

btn1 = tk.Button(frame2, text="Bouton 1")
btn1['font'] = f
btn1.place(rely=0.38, relx=0.03)

btn2 = tk.Button(frame2, text="Bouton 2")
btn2['font'] = f
btn2.place(rely=0.44, relx=0.03)

btn3 = tk.Button(frame2, text="Bouton 3")
btn3['font'] = f
btn3.place(rely=0.32, relx=0.03)


L1 = Label(frame2, text="Une ligne : ")
L1['font'] = f
L1.place(rely=0.5, relx=0.03)

E1 = Entry(frame2, bd = 2, width = 4)
E1['font'] = f
E1.place(rely=0.5, relx=0.15)

L2 = Label(frame2, text="Une portion de ligne :")
L2['font'] = f
L2.place(rely=0.56, relx=0.03)

E2 = Entry(frame2, bd =2, width = 3)
E2['font'] = f
E2.place(rely=0.56, relx=0.26)

E2bis = Entry(frame2, bd =2, width = 3)
E2bis['font'] = f
E2bis.place(rely=0.56, relx=0.32)

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
