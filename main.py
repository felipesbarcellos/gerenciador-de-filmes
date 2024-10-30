from views.view import *
from controllers.filmes_controller import ControllerFilmes
from db import cria_db
from models import *

if __name__ == "__main__":
    app = App()
    app.mainloop()
    # ControllerFilmes(view='').adicionar_filme('Kung Fu Panda')
    