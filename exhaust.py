from assets.modules import messages
from assets.modules import scripts_manager

print(messages.logo)
print(messages.menu)

while True:
    choice = messages.get_choice()
    script = scripts_manager.get_script(choice, __file__)

    if script is not None:
        script.start()
