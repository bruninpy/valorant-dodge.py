import eel
from valclient.client import Client
from valclient.exceptions import PhaseError

client = Client(region="br")
client.activate()

eel.init('web')

@eel.expose
def dodge():
    try:
        client.pregame_quit_match()  # Tenta executar a ação
    except PhaseError:
        print("you are not in a pre-game..")
    except Exception as e:
        print(f"something went wrong!")

# Inicia o servidor do Eel e a interface gráfica
eel.start('index.html', size=(900, 500))
