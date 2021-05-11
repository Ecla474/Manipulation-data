# Importation des librairies
import tkinter as tk
from tkinter import filedialog, ttk, messagebox
from tkinter import font as fontTk
from tkinter import Label
import pandas as pd

# LES FONCTIONS

# Ferme la fenetre Tkinter


def close_window():
    root.destroy()


# Ouvre une nouvelle fenetre pour choisir le fichier data
def File_dialog():
    filename = filedialog.askopenfilename(initialdir="~/",
                                          title="Selectionner un fichier",
                                          filetypes=(("csv files", "*.csv"),
                                                     ("JSON files", "*.json"),
                                                     ("xlsx files", "*.xlsx"),
                                                     ("Tous les fichiers",
                                                      "*.*")
                                                     ))
    print(filename)
    label_file["text"] = filename
    return None


# Charge le fichier data choisi
def Load_excel_data():
    file_path = label_file["text"]
    try:

        excel_filename = r"{}".format(file_path)

        if excel_filename[-4:] == ".csv":

            df = pd.read_csv(excel_filename)
            label_file_csv = ttk.Label(file_frame, text="Fichier CSV chargé !")
            label_file_csv['font'] = f
            label_file_csv.place(rely=0.2, relx=0.36)
            tv1["column"] = ['index'] + list(df.columns)
            tv1["show"] = "headings"
            df = Load_csv_data(excel_filename)

        else:
            if excel_filename[-5:] == ".json":
                df = pd.read_json(excel_filename)
                label_file_json = ttk.Label(file_frame,
                                            text="Fichier JSON chargé !")
                label_file_json['font'] = f
                label_file_json.place(rely=0.2, relx=0)
                tv1["column"] = ['index'] + list(df.columns)
                tv1["show"] = "headings"
                df = Load_json_data(excel_filename)

            else:
                tk.messagebox.showerror("Information",
                                        "Fichier invalide ou inexistant !")

    except ValueError:
        tk.messagebox.showerror("Information",
                                "Fichier invalide ou inexistant !")
        return None

    return df


# Charge le fichier si il est en format CSV
def Load_csv_data(excel_filename):

    df = pd.read_csv(excel_filename)
    clear_data()
    ry = 0.02
    i = 0

    for column in tv1["columns"]:
        print(column)
        tv1.heading(column, text=column)

    for col2 in list(df.columns):

        btnCol = tk.Button(frame2, text="Colonne : " + col2,
                           command=lambda col2=col2: affiche_colonne(col2))
        btnCol['font'] = f
        btnCol.place(rely=ry, relx=0.4)

        btnGrp = tk.Button(frame2, text="Regrouper : " + col2,
                           command=lambda col2=col2: regroupe_colonne(col2))
        btnGrp['font'] = f
        btnGrp.place(rely=ry, relx=0.68)

        ry = ry + 0.06

    for col2 in list(df.columns):

        btnTri = tk.Button(frame2, text="Tri : " + col2,
                           command=lambda col2=col2: tri_colonne(col2))
        btnTri['font'] = f
        btnTri.place(rely=ry, relx=0.4)

        btnTri2 = tk.Button(frame2, text="Tri décroissant: " + col2,
                            command=lambda col2=col2:
                            tri_colonne_inverse(col2))
        btnTri2['font'] = f
        btnTri2.place(rely=ry, relx=0.68)

        ry = ry + 0.06
        i = i + 1

    return df


# Charge le fichier si il est en format JSON
def Load_json_data(excel_filename):

    df = pd.read_json(excel_filename)
    clear_data()
    ry = 0.02
    i = 0

    for column in tv1["columns"]:
        print(column)
        tv1.heading(column, text=column)

    for col2 in list(df.columns):

        btnCol = tk.Button(frame2, text="Colonne : " + col2,
                           command=lambda col2=col2: affiche_colonne(col2))
        btnCol['font'] = f
        btnCol.place(rely=ry, relx=0.4)

        btnGrp = tk.Button(frame2, text="Regrouper : " + col2,
                           command=lambda col2=col2: regroupe_colonne(col2))
        btnGrp['font'] = f
        btnGrp.place(rely=ry, relx=0.68)

        ry = ry + 0.06

    for col2 in list(df.columns):

        btnTri = tk.Button(frame2, text="Tri : " + col2,
                           command=lambda col2=col2: tri_colonne(col2))
        btnTri['font'] = f
        btnTri.place(rely=ry, relx=0.4)

        btnTri2 = tk.Button(frame2, text="Tri décroissant: " + col2,
                            command=lambda col2=col2:
                            tri_colonne_inverse(col2))
        btnTri2['font'] = f
        btnTri2.place(rely=ry, relx=0.68)

        ry = ry + 0.06
        i = i + 1

    return df


# Affiche une colonne du fichier data
def affiche_colonne(column):
    df = Load_excel_data()
    clear_data()
    tv1["column"] = ['index'] + [column]
    tv1["show"] = "headings"
    for column in tv1["columns"]:
        print(column)
        tv1.heading(column, text=column)

    df2 = df[column]
    df_rows = df2.to_numpy().tolist()
    i = 1
    for row in df_rows:
        print(row)
        tv1.insert("", "end", values=[i] + [row])
        i += 1
    return None


# Tri d'une Colonne par ordre croissant
def tri_colonne(column):
    df = Load_excel_data()
    clear_data()
    df2 = df.sort_values(by=column)
    df_rows = df2.to_numpy().tolist()
    i = 1
    for row in df_rows:
        print(row)
        tv1.insert("", "end", values=[i] + row)
        i += 1
    return None


# Tri d'une Colonne par ordre croissant
def tri_colonne_inverse(column):
    df = Load_excel_data()
    clear_data()
    df2 = df.sort_values(by=column, ascending=False)
    df_rows = df2.to_numpy().tolist()
    i = 1
    for row in df_rows:
        print(row)
        tv1.insert("", "end", values=[i] + row)
        i += 1
    return None


# Regroupe le nombre d'occurences pour les valeurs de la colonne selectionné
def regroupe_colonne(column):
    df = Load_excel_data()
    clear_data()
    df2 = df.groupby(column).count()
    df3 = df[column].sort_values().unique()
    print(df3)
    tv1["column"] = [column] + list(df2.columns)
    tv1["show"] = "headings"
    for column in tv1["columns"]:
        print(column)
        tv1.heading(column, text=column)
    df_rows = df2.to_numpy().tolist()
    i = 0
    for row in df_rows:
        print(row)
        print(df3[i])
        tv1.insert("", "end", values=[df3[i]] + row)
        i += 1
    return None


# Affiche les 5 premieres lignes
def affiche_5_premiers():

    df = Load_excel_data()
    clear_data()

    df2 = df.head()
    df_rows = df2.to_numpy().tolist()
    i = 1
    for row in df_rows:
        print(row)

        tv1.insert("", "end", values=[i] + row)
        i += 1
    return None


# Affiche les 5 dernieres lignes
def affiche_5_derniers():

    df = Load_excel_data()
    clear_data()
    df2 = df.tail()
    df_rows = df2.to_numpy().tolist()
    i = 1
    for row in df_rows:
        print(row)
        tv1.insert("", "end", values=[i] + row)
        i += 1
    return None


# Affiche le fichier entier
def affiche_tout():
    df = Load_excel_data()
    df_rows = df.to_numpy().tolist()
    i = 1
    for row in df_rows:
        print(row)

        tv1.insert("", "end", values=[i] + row)
        i += 1
    return None


# Affiche les détails du fichier
def description():

    df = Load_excel_data()
    df2 = df.describe()
    df_rows = df2.to_numpy().tolist()
    i = 0
    descr = ['count', 'mean', 'std', 'min', '25%', '50%', '75%', 'max']
    for row in df_rows:
        print(row)
        tv1.insert("", "end", values=[descr[i]] + row)
        i += 1
    return None


# Affiche une ligne
def affiche_ligne():
    df = Load_excel_data()
    clear_data()
    sl = E1.get()
    ligne = int(sl)
    df2 = df[ligne:ligne+1]
    df_rows = df2.to_numpy().tolist()
    for row in df_rows:
        print(row)
        tv1.insert("", "end", values=[ligne] + row)
    return None


# Affiche plusieurs lignes
def affiche_des_lignes():
    df = Load_excel_data()
    clear_data()
    sl2 = E2.get()
    sl2bis = E2bis.get()
    l2 = int(sl2)
    l2b = int(sl2bis)
    df2 = df[l2:l2b+1]
    df_rows = df2.to_numpy().tolist()
    l1 = l2
    for row in df_rows:
        print(row)
        tv1.insert("", "end", values=[l1] + row)
        l1 += 1
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
frame1.place(height=800, width=1000, relx=0.44)


file_frame = tk.LabelFrame(root, text="Ouvrir")
file_frame['font'] = f
file_frame.place(height=140, width=400, rely=0.01, relx=0.01)

frame2 = tk.LabelFrame(root, text="Manipulation des données")
frame2['font'] = f
frame2.place(height=700, width=750, rely=0.18, relx=0.01)


# Les boutons

btn1 = tk.Button(file_frame, text="Rechercher", bg="blue",
                 command=lambda: File_dialog())
btn1['font'] = f
btn1.place(rely=0.6, relx=0.53)

btn2 = tk.Button(file_frame, text="Charger", bg="green",
                 command=lambda: Load_excel_data())
btn2['font'] = f
btn2.place(rely=0.6, relx=0.27)

btnClear = tk.Button(frame2, text="Effacer", command=lambda: clear_data())
btnClear['font'] = f
btnClear.place(rely=0.38, relx=0.03)

btn5prem = tk.Button(frame2, text="5 premieres données",
                     command=lambda: affiche_5_premiers())
btn5prem['font'] = f
btn5prem.place(rely=0.08, relx=0.03)

btn5dern = tk.Button(frame2, text="5 dernieres données",
                     command=lambda: affiche_5_derniers())
btn5dern['font'] = f
btn5dern.place(rely=0.14, relx=0.03)

btnAff = tk.Button(frame2, text="Tout afficher",
                   command=lambda: affiche_tout())
btnAff['font'] = f
btnAff.place(rely=0.02, relx=0.03)

btnDescrp = tk.Button(frame2, text="Description",
                      command=lambda: description())
btnDescrp['font'] = f
btnDescrp.place(rely=0.2, relx=0.03)

btnQuit = tk.Button(root, text="Quitter", bg="red",
                    command=lambda: close_window())
btnQuit['font'] = f
btnQuit.place(rely=0.95, relx=0.92)

L1 = Label(frame2, text="Une ligne : ")
L1['font'] = f
L1.place(rely=0.26, relx=0.03)

E1 = tk.Entry(frame2, bd=2, width=4)
E1['font'] = f
E1.place(rely=0.26, relx=0.15)

B1 = tk.Button(frame2, text="Entrer", command=lambda: affiche_ligne())
B1['font'] = f
B1.place(rely=0.255, relx=0.21)

L2 = Label(frame2, text="Intervalle :")
L2['font'] = f
L2.place(rely=0.32, relx=0.03)

E2 = tk.Entry(frame2, bd=2, width=3)
E2['font'] = f
E2.place(rely=0.32, relx=0.17)

E2bis = tk.Entry(frame2, bd=2, width=3)
E2bis['font'] = f
E2bis.place(rely=0.32, relx=0.23)

B2 = tk.Button(frame2, text="Entrer", command=lambda: affiche_des_lignes())
B2['font'] = f
B2.place(rely=0.315, relx=0.29)


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
