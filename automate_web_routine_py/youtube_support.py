import os
from YoutubeShuffle import YoutubeShuffle



def execute_command(manager, command):
    """ execute the command """
    manager: YoutubeShuffle
    if command == "ad":
        manager.ad_killer()
    if command == "h" or command == "help" or command == "quick help" or command == "qh":
        return execute_help_command(command)
    opcode, *addressing_mode = command.split(maxsplit=1)
    if opcode == "s" or opcode == "search":
        if not addressing_mode:
            addressing_mode = input("what would you want to search?\n>")
        manager.search(addressing_mode)
        print(manager.string_found() + "\n")
        pick = input("pick the song you want to listen to\n>")
        if pick[:2] == "s ":
            return execute_command(manager, pick)
        while pick == "go":
            # execute the 'go' command
            manager.go()
            pick = input("pick the song you want to listen to\n>")
        manager.pick_found(pick)
    elif opcode == "r" or opcode == "recommended":
        manager.find_recommended()
        print(manager.string_recommended() + "\n")
        pick = input("pick the song you want to listen to\n>")
        if pick[:2] == "s ":
            return execute_command(manager, pick)
        while pick == "go":
            # execute the 'go' command
            manager.go()
            pick = input("pick the song you want to listen to\n>")
        manager.pick_recommended(pick)
    elif opcode == "p" or opcode == "pause" or opcode == "play":
        manager.play_pause()
    elif opcode == "m" or opcode == "mute":
        manager.mute()
    elif opcode == "b" or opcode == "back":
        manager.back()
    elif opcode == "f" or opcode == "forward":
        manager.forward()
    elif opcode == "refresh" or opcode == "re" or opcode == "reload":
        manager.refresh()
    elif opcode == "n" or opcode == "next":
        manager.find_next_song()
        print(manager.string_next_song() + "\n")
        go = input("do you want to go next? [y/n]\n>")
        if go == "y":
            manager.goto_next_song()
    elif opcode == "current" or opcode == "cs":
        print(manager.string_current_song())
    elif opcode == "clear" or opcode == "c":
        os.system("clear")
    elif opcode == "go":
        manager.go()



def execute_help_command(command):
    """ execute the help command """
    if command == "qh" or command == "quick help":
        quick_help_string = "\t-search: write a string and search it in youtube\n" \
                            "\t-recommended: find the songs youtube is recommending you\n" \
                            "\t-pause/play: pause or play the song\n" \
                            "\t-mute: mute or unmute the song\n" \
                            "\t-back: go back to the previous page\n" \
                            "\t-forward: go forward to the next page\n" \
                            "\t-refresh: refresh the current page\n" \
                            "\t-next: next find the next song youtube is going to play\n" \
                            "\t-clear: clear the terminal\n" \
                            "\t-quit: quit the session and close youtube\n" \
                            "\t-go: go to youtube on the other workspace, or go back\n"
        return quick_help_string
    else:
        return search_help() + recommended_help() + pause_play_help() + next_help() + back_help()\
                + forward_help() + mute_help() + clear_help() + quit_help() + refresh_help() + go_help()

def search_help():
    help_string = "#search:\n\twrite a string and search it in youtube\n" \
                  "\tyou will then pick a song between the found ones and listen to it\n" \
                  "\tsyntax: search argument\n\tthe argument is optional\n" \
                  "\tyou can write s for the compact form\n\n"
    return help_string


def recommended_help():
    help_string = "#recommended:\n\tfind the songs youtube is recommending you\n" \
                  "\tyou will then pick a song between the found ones and listen to it\n" \
                  "\tsyntax: recommended\n" \
                  "\tyou can write r for the compact form\n\n"
    return help_string


def pause_play_help():
    help_string = "#pause/play:\n\tpause or play the song\n" \
                  "\tsyntax: play or syntax: pause\n" \
                  "\tyou can write p for the compact form\n\n"
    return help_string


def mute_help():
    help_string = "#mute:\n\tmute or unmute the song\n" \
                  "\tsyntax: mute\n" \
                  "\tyou can write m for the compact form\n\n"
    return help_string


def back_help():
    help_string = "#back:\n\tgo back to the previous page\n" \
                  "\tit may happen your previous page is the search page\n" \
                  "\tbut most of the time you will go back to the previous song" \
                  "\tsyntax: back\n" \
                  "\tyou can write b for the compact form\n\n"
    return help_string


def forward_help():
    help_string = "#forward:\n\tgo forward to the next page\n" \
                  "\tuse it after you used the back command\n" \
                  "\tsyntax: forward\n" \
                  "\tyou can write f for the compact form\n\n"
    return help_string


def refresh_help():
    help_string = "#refresh:\n\trefresh the current page\n" \
                  "\tuse it at your discretion\n" \
                  "\tsyntax: refresh\n" \
                  "\tthis one has no compact form\n\n"
    return help_string


def next_help():
    help_string = "#next:\n\tnext find the next song youtube is going to play\n" \
                  "\tyou will then be prompted whether you want to listen to it " \
                  "or wait for the current song to finish\n" \
                  "\tsyntax: next\n" \
                  "\tyou can write n for the compact form\n\n"
    return help_string


def clear_help():
    help_string = "#clear:\n\tclear the terminal\n" \
                  "\tsyntax: clear\n" \
                  "\tyou can write c for the compact form\n\n"
    return help_string


def quit_help():
    help_string = "#quit:\n\tquit the session and close youtube\n" \
                  "\tsyntax: quit\n" \
                  "\tyou can write q for the compact form\n\n"
    return help_string

def go_help():
    help_string = "#go:\n\tgo to youtube on the other workspace, or go back\n" \
                  "\tsyntax: go\n" \
                  "\tthis one has no compact form\n\n"
    return help_string