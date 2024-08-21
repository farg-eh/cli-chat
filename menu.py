from support import *

class menu_prompt:
    def __init__(self):
        #self.app = cli_chat
        self.welcome_msg = "welcome to local-cli-chat by arai jenn"
        self.welcome_text = self.welcome_msg
        self.commands = {'create room-name':'creates a chat room with a specified name',
                         'list': 'lists available chat rooms',
                         'join n': 'join a chat room (use an index instead of n)',
                         'info': 'displays some info about u or the chat-room',
                         'leave': 'leaves the current chat room',
                         'close': 'closes the program'
                        }
        self.cmds_col_width = len(max(self.commands.keys(), key=lambda s: len(s))) + 3
        self.lines = len(self.commands.keys()) + 4

        # welcome text animation
        self.animation_timer = Timer(3, repeat=True, autostart=True)
    def animate(self):
        index = int(self.animation_timer.get_progress() * len(self.welcome_msg))
        self.welcome_text = text(self.welcome_msg[:index], 2) + text(self.welcome_msg[index], 1) + text(self.welcome_msg[index+1:], 2)


    def show(self):
        print(self.welcome_text)
        print(text("=" * len(self.welcome_msg), 5))
        print(text("commands :-", 2))
        for cmd, details in self.commands.items():
            print("    " + text("/" + cmd, 3), " " * (self.cmds_col_width - len(cmd)), text(details, 0))

    def update(self):
        self.animation_timer.update()
        self.animate()

