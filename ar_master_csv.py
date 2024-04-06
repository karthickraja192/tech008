import csv
from tkinter import ttk


class csv_master:

    def table_style(self,tree,root):
        tree_heading_backround = '#004080'
        tree_heading_text = 'white'
        def prevent_resize(event):
            if tree.identify_region(event.x, event.y) == "separator":
                return "break"
        tree.column("#0", width=0, stretch="no")
        tree.bind('<Motion>', prevent_resize)
        tree.bind('<Button-1>', prevent_resize)
        style = ttk.Style(root)
        style.theme_use("clam")
        style.configure("Treeview.Heading", background=tree_heading_backround,foreground=tree_heading_text)
        style.configure("Treeview.Heading", font=('Calibri', 13,'bold'))
        tree.tag_configure("evenrow", background='#FFCC99', foreground='black')
        tree.tag_configure("oddrow", background='#FFE5CC', foreground='black')




# mm=csv_master()
# xx=mm.missing_value_elimination("dataset.csv","data_set/missing.csv")
# print(xx)