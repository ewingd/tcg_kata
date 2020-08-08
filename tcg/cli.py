from curses import wrapper
import curses
import random


class Board:
    def __init__(self, window):
        self.window = window
        self.rows, self.cols = self.window.getmaxyx()
        self.COLOR_HP = 100
        self.COLOR_MP = 101
        self.COLOR_DECK = 102

        curses.init_pair(self.COLOR_HP, curses.COLOR_RED, curses.COLOR_BLACK)
        curses.init_pair(self.COLOR_MP, curses.COLOR_BLUE, curses.COLOR_BLACK)
        curses.init_pair(self.COLOR_DECK, curses.COLOR_WHITE, curses.COLOR_BLACK)

    def render(self):
        self.refresh()

        self.draw_frames()
        self.draw_player_frames()
        self.draw_player_hand()
        self.draw_opponent_hand()

        self.window.refresh()

    def refresh(self):
        self.rows, self.cols = self.window.getmaxyx()
        self.window.clear()

    def draw_frames(self):
        self.window.border()

        # Draw a horizontal line in the center of the window
        self.window.addch(int(self.rows / 2), 0, curses.ACS_LTEE)
        self.window.hline(int(self.rows / 2), 1, curses.ACS_HLINE, self.cols - 2)
        self.window.addch(int(self.rows / 2), self.cols - 1, curses.ACS_RTEE)

    def draw_player_frames(self):
        # Draw the player's information
        # self.draw_player_frame(int(self.rows / 2), self.cols - 10)
        self.draw_player_frame(self.rows - 5, self.cols - 10)

        # Draw the opponent's information
        # self.draw_player_frame(int(self.rows / 2) - 4, self.cols - 10)
        self.draw_player_frame(0, self.cols - 10)

    def draw_player_frame(self, row, col):
        # Draw HP
        self.window.addstr(
            row + 1, col + 1, "30 / 30", curses.color_pair(self.COLOR_HP)
        )
        # Draw MP
        self.window.addstr(
            row + 2, col + 1, " 0 /  0", curses.color_pair(self.COLOR_MP)
        )
        # Draw Deck / Discard
        self.window.addstr(
            row + 3, col + 1, "30 /  0", curses.color_pair(self.COLOR_DECK)
        )

    def draw_player_hand(self):
        row = self.rows - 4
        start_col = 2
        end_col = self.cols - 12
        card_count = 7
        card_width = int((end_col - start_col) / 7) - 1

        max_hand_width = end_col - start_col

        hand_width = card_width * card_count
        start_col = int((max_hand_width - hand_width) / 2)

        for card_num in range(card_count):
            card_start = start_col + (card_num * card_width)
            card_end = card_start + card_width - 2
            self.window.hline(row, card_start, curses.ACS_HLINE, card_width - 1)
            self.window.addch(row, card_start, curses.ACS_ULCORNER)
            self.window.addch(row, card_end, curses.ACS_URCORNER)
            self.window.vline(
                row + 1, card_start, curses.ACS_VLINE, self.rows - row - 2
            )
            self.window.vline(row + 1, card_end, curses.ACS_VLINE, self.rows - row - 2)

            self.window.addstr(row + 1, card_start + 2, "Card " + str(card_num + 1))
            self.window.addstr(row + 1, card_end - 2, str(random.randint(1, 9)))

    def draw_opponent_hand(self):
        row = 3
        start_col = 2
        end_col = self.cols - 12
        card_count = 6
        card_width = int((end_col - start_col) / 7) - 1

        max_hand_width = end_col - start_col

        hand_width = card_width * card_count
        start_col = int((max_hand_width - hand_width) / 2)

        for card_num in range(card_count):
            card_start = start_col + (card_num * card_width)
            card_end = card_start + card_width - 2
            self.window.hline(row, card_start, curses.ACS_HLINE, card_width - 1)
            self.window.addch(row, card_start, curses.ACS_LLCORNER)
            self.window.addch(row, card_end, curses.ACS_LRCORNER)
            self.window.vline(1, card_start, curses.ACS_VLINE, row - 1)
            self.window.vline(1, card_end, curses.ACS_VLINE, row - 1)


def main(stdscr):
    running = True

    curses.curs_set(0)

    board = Board(stdscr)

    while running:
        board.render()

        key = stdscr.getkey()

        if key in ("q", "Q"):
            running = False


if __name__ == "__main__":
    wrapper(main)
