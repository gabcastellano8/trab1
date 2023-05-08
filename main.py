from Desktop import Desktop
from Notebook import Notebook

desktop = Desktop("Dell Inspiron", "Preto", 3500.0, "500W")
notebook = Notebook("Dell G15", "Cinza", 5900.0, "8 horas")

desktop.getInformacoes()
desktop.cadastrar()
notebook.getInformacoes()
notebook.cadastrar()
