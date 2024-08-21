import curses, signal, sys, math
from support import *
from menu import menu_prompt
import time
import threading


class CliChat:
    def __init__(self):
        self.running = True
        # self.menu = menu_prompt()
        self.user_input = ""
        self.size = None

        # messages
        self.message_history = ""
        self.enter_message = "Enter : "
        self.prefix = " YOU > "

    def exit(self, sig, frame):  # signal handler for ctrl + c
        self.running = False

    def visible_content(self, width, height):
        visible_lines = []
        count = 0
        lines = self.message_history.split('\n')[-height:]
        for line in lines:
            line_spaces = math.ceil(len(line) / (width))

            if count + line_spaces > height:
                # if the line is too big
                remaining_screen_lines = height - count
                max_chars_to_show = remaining_screen_lines * width
                visible_lines.append(line[-max_chars_to_show:])
                break

            visible_lines.append(line)
            count += line_spaces
        return '\n'.join(visible_lines)


    def handle_input(self, stdscr):
        # handling input
        try:
            c = stdscr.get_wch()
            if isinstance(c, str):
                if c == "\n":  # ENTER HANDLER
                    msg = self.prefix + self.user_input + "<E>"
                    self.message_history += msg + '\n'
                    self.user_input = ""
                else:
                    self.user_input += c
            else:
                if c == curses.KEY_BACKSPACE or c == curses.KEY_DC:
                    self.user_input = self.user_input[:-1]
        except curses.error as e:
                pass


    def run(self, stdscr):
        stdscr.nodelay(True)
        curses.use_default_colors()
        while self.running:
            self.size = stdscr.getmaxyx()[1], stdscr.getmaxyx()[0]
            # top bar
            stdscr.clear()
            top_bar = curses.newwin(3, self.size[0], 0, 0)
            top_bar.addstr(1, 1, f"size:({self.size[0]}, {self.size[1]})")
            top_bar.box()

            # content
            content_window_height = self.size[1] - 3 - 1  # - 3 for the top_bar and -1 for the input bar
            content_window = curses.newwin(content_window_height, self.size[0], 3, 0)
            content = self.visible_content(self.size[0], content_window_height - 1)
            content_window.addstr(0, 0, content)



            # bottom input area
            input_bar = curses.newwin(1, self.size[0], self.size[1]-1, 0)
            self.handle_input(stdscr)
            typing_space = self.size[0] - len(self.enter_message) - 2
            cropped_input = self.user_input if len(self.user_input) < typing_space else self.user_input[-typing_space:]
            input_bar.addstr(0, 1, self.enter_message + cropped_input)

            # refreshing
            stdscr.refresh()
            top_bar.refresh()
            content_window.refresh()
            input_bar.refresh()

            time.sleep(0.03)



if __name__ == '__main__':
    app = CliChat()
    # handlers
    signal.signal(signal.SIGINT, app.exit)
    curses.wrapper(app.run)
    print("exited.")
    print(app.user_input)
    print(get_my_ip())


# i want to make the content window scrollable [X]
# i want to add more stuff to the top bar []
# i want to refactor and tidy the code more []
# i want to fix the flickering []
# i want to add colors []
# i want to add the commands help message []
# after all that we can go to the networking part []
