import tkinter as tk
from classes import Game

def main():
    # Create the main window
    root = tk.Tk()
    root.title("Tischtennis Punktzähler")

    # Make the window resizable
    root.resizable(True, True)

    # Start the application in fullscreen mode
    root.attributes('-fullscreen', True)

    # Use default player names
    player1_name = "Claiminizzer 1"
    player2_name = "Claiminizzer 2"

    # Initialize the game
    game = Game(player1_name, player2_name)

    # Fonts
    score_font = "Impact"
    name_font = "Courier New"

    # Function to update the font sizes when the window is resized
    def resize_font(event=None):
        root.update_idletasks()
        new_height = root.winfo_height()

        font_size_score_new = int(new_height * 0.75)
        font_size_score_new = max(font_size_score_new, 50)
        font_size_score_new = min(font_size_score_new, 500)

        font_size_name_new = int(new_height * 0.05)
        font_size_name_new = max(font_size_name_new, 15)
        font_size_name_new = min(font_size_name_new, 75)

        score_label_player1.config(font=(score_font, font_size_score_new))
        score_label_player2.config(font=(score_font, font_size_score_new))
        name_label_player1.config(font=(name_font, font_size_name_new))
        name_label_player2.config(font=(name_font, font_size_name_new))

    # Function to update the score labels
    def update_scores():
        score_label_player1.config(text=f"{game.score_player1}")
        score_label_player2.config(text=f"{game.score_player2}")

        # Reset background colors and score label colors
        player1_card.config(bg=card_bg_color)
        player2_card.config(bg=card_bg_color)
        score_label_player1.config(bg=card_bg_color, fg=text_color)
        score_label_player2.config(bg=card_bg_color, fg=text_color)
        name_label_player1.config(bg=card_bg_color, fg=text_color)
        name_label_player2.config(bg=card_bg_color, fg=text_color)

        if game.winner:
            if game.winner == game.player1_name:
                # Inverse the colors for the winner
                player1_card.config(bg=text_color)
                score_label_player1.config(bg=text_color, fg=card_bg_color)
                name_label_player1.config(bg=text_color, fg=card_bg_color)
            elif game.winner == game.player2_name:
                # Inverse the colors for the winner
                player2_card.config(bg=text_color)
                score_label_player2.config(bg=text_color, fg=card_bg_color)
                name_label_player2.config(bg=text_color, fg=card_bg_color)
        else:
            # Match point color change is disabled but kept in the code
            '''
            if game.is_player_at_match_point(1):
                score_label_player1.config(fg='green')
            if game.is_player_at_match_point(2):
                score_label_player2.config(fg='green')
            '''

    # Event handlers for key presses
    def on_key_press(event):
        key = event.char.lower()

        if key == '1':
            game.add_point(1)
            update_scores()
        elif key == '2':
            game.add_point(2)
            update_scores()
        elif key == 'u':
            game.undo_last_action()
            update_scores()
        elif key == 'r':
            game.reset_game()
            update_scores()
        elif key == 'q':
            exit_application()

    # Function to exit the application gracefully
    def exit_application(event=None):
        root.destroy()

    # Bind key presses to the root window
    root.bind('<KeyPress>', on_key_press)
    root.protocol("WM_DELETE_WINDOW", exit_application)

    # Set a background color to mimic a scoreboard
    root.configure(bg='#343434')  # Changed background color

    # Colors for the flip cards and text
    card_bg_color = '#343434'  # Changed card background color
    card_border_color = '#000000'
    text_color = '#FFC000'  # Yellow text color

    # Create frames for each player
    main_frame = tk.Frame(root, bg=root['bg'])
    main_frame.pack(expand=True, fill='both', padx=20, pady=20)

    # Player 1 card
    player1_card = tk.Frame(main_frame, bg=card_bg_color, bd=5, relief='raised')
    player1_card.pack(side='left', expand=True, fill='both', padx=10, pady=10)
    player1_card.pack_propagate(False)  # Prevent resizing

    name_label_player1 = tk.Label(
        player1_card,
        text=player1_name,
        font=(name_font, 20),  # Initial font size
        bg=card_bg_color,
        fg=text_color
    )
    name_label_player1.pack(pady=(20, 5))

    score_label_player1 = tk.Label(
        player1_card,
        text="0",
        font=(score_font, 100),  # Initial font size
        bg=card_bg_color,
        fg=text_color,
        anchor='center'
    )
    score_label_player1.pack(expand=True, fill='both')

    # Player 2 card
    player2_card = tk.Frame(main_frame, bg=card_bg_color, bd=5, relief='raised')
    player2_card.pack(side='right', expand=True, fill='both', padx=10, pady=10)
    player2_card.pack_propagate(False)  # Prevent resizing

    name_label_player2 = tk.Label(
        player2_card,
        text=player2_name,
        font=(name_font, 20),  # Initial font size
        bg=card_bg_color,
        fg=text_color
    )
    name_label_player2.pack(pady=(20, 5))

    score_label_player2 = tk.Label(
        player2_card,
        text="0",
        font=(score_font, 100),  # Initial font size
        bg=card_bg_color,
        fg=text_color,
        anchor='center'
    )
    score_label_player2.pack(expand=True, fill='both')

    # Add borders to mimic flip cards
    for frame in [player1_card, player2_card]:
        frame.config(
            highlightbackground=card_border_color,
            highlightcolor=card_border_color,
            highlightthickness=5
        )

    # Bind the configure event to resize the font when the window is resized
    root.bind('<Configure>', resize_font)

    # Run the main loop
    root.mainloop()

if __name__ == "__main__":
    main()
