#!/usr/bin/env python3
import os
import sys
import argparse
import platform
from colorama import Fore, Style
from prettytable import PrettyTable

err = Fore.RED + '[X]' + Style.RESET_ALL
okay = Fore.GREEN + '[+]' + Style.RESET_ALL
info = Fore.YELLOW + '[!]' + Style.RESET_ALL

# check python version
if sys.version_info.major != 3:
    print('\n' + err + ' please run this script with python3!\n')
    sys.exit(1)


# clear and banner
def clear():
    if platform.system() == 'Linux':
        os.system('clear')
    else:
        print(err, 'non-linux support coming soon... maybe.')
        sys.exit(1)


def banner():
    print(Fore.LIGHTRED_EX + '''\

    |\___/|
   /       \      thievius! (username generator) v1.0
  /_ ▲   ▲ _\                   by cr0w
    ==\▼/==
    ''' + Style.RESET_ALL)


# the most unnecessary exit/exception logic
def confirm_exception():
    while True:
        try:
            print('\n\n' + err,
                  '^C was detected. would you like to exit?' + Fore.LIGHTRED_EX + ' (y/n)' + Style.RESET_ALL)
            choice = input('\r\n>> ')
            if choice.lower() in ['y']:
                print('')
                sys.exit(1)
            elif choice.lower() in ['n']:
                clear()
                banner()
                print(info, 'getting names...')
                print(okay, 'please enter: first name + last name (one name per line)')
                print(info, 'if you\'re done entering in names, type'
                      + Fore.LIGHTRED_EX + ' "done" ' + Style.RESET_ALL
                      + 'or' + Fore.LIGHTRED_EX + ' "exit"\n' + Style.RESET_ALL)
                break
            else:
                clear()
                banner()
                confirm_exception()
        except KeyboardInterrupt:
            clear()
            sys.exit(1)


# get name from user
names = []
# output filename
out_file = "users.txt"


def get_name():
    print(info, 'getting names...')
    print(okay, 'please enter:' + Fore.LIGHTRED_EX +
                ' first name' + Style.RESET_ALL + ' + ' + Fore.LIGHTRED_EX + 'last name '
                + Style.RESET_ALL + Fore.YELLOW +
                '(one name per line)')
    print(info, 'if you\'re done entering in names, type'
          + Fore.LIGHTRED_EX + ' "done" ' + Style.RESET_ALL
          + 'or' + Fore.LIGHTRED_EX + ' "exit"\n' + Style.RESET_ALL)
    while True:
        try:
            name = input('>> ')
            names.append(name)
            if name.lower() in ['done', 'exit']:
                names.pop()  # such a cool little function -> deletes last element of an array unless specified
                break
            elif name in ['',
                          ' ']:  # don't let users supply in spaces or nothing, could've done this with filter() too
                names.pop()
        except KeyboardInterrupt:
            confirm_exception()


def display_names():
    # names_display = ['names', names]
    if len(names) == 0:
        print('')
        print(err, 'no names supplied.')
        print(info, 'exiting...\n')
        sys.exit(1)
    else:
        print('')
        print(info, 'captured {} '.format(len(names)) + 'name(s)!')
        print(okay, 'here they are:')
        table = PrettyTable(border=True, header=False, padding_width=3)
        table.title = 'names'
        table.add_row(names)
        print(Fore.LIGHTRED_EX)
        print(table)
        print(Style.RESET_ALL)


# put the names into a temporary file for john
def export_names():
    print('')
    print(info, 'exporting target names into a file for JtR')
    with open('names.txt', 'w') as file:
        for name in names:
            file.write("".join(name) + '\n')
    print(okay, 'done! continuing execution...')


# generate usernames from exported names now
def generate_usernames():
    print(info, 'time to generate some usernames from the {}'.format(len(names)) + ' name(s)!')
    print(info, 'would you like to generate case-sensitive usernames?' + Fore.LIGHTRED_EX + ' (y/n)'
          + Style.RESET_ALL)
    while True:
        try:
            choice = input('\r\n>> ')
            print(Fore.LIGHTRED_EX)
            if choice.lower() in ['y', 'yes']:
                command = 'john --wordlist=names.txt --rules=Login-Generator --stdout > usernames.txt'
                os.system(command)
                print('')
                print(okay, 'finished!')
                line_count = sum(1 for line in open('usernames.txt'))
                print(info, 'thievius! has generated:' + Fore.LIGHTGREEN_EX,
                      '{}'.format(line_count), 'usernames!' + Style.RESET_ALL + '\n')
                reorder = 'cat usernames.txt | sort > users.txt'
                os.system(reorder)
                delete_temporary = 'rm names.txt usernames.txt'
                os.system(delete_temporary)
                break
            elif choice.lower() in ['n', 'no']:
                command = 'john --wordlist=names.txt --rules=Login-Generator-i --stdout > usernames.txt'
                os.system(command)
                print('')
                print(okay, 'finished!')
                line_count = sum(1 for line in open('usernames.txt'))
                print(info, 'thievius! has generated:' + Fore.LIGHTGREEN_EX,
                      '{}'.format(line_count), 'usernames' + Style.RESET_ALL + '!\n')
                reorder = 'cat usernames.txt | sort > ' + out_file
                os.system(reorder)
                delete_temporary = 'rm names.txt usernames.txt'
                os.system(delete_temporary)
                break
            else:
                clear()
                banner()
                generate_usernames()
        except KeyboardInterrupt:
            confirm_exception()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog="thievius!",description="This tool generates usernames from first and last names")
    parser.add_argument('-i',metavar="IN_FILE", help="Input a namelist file")
    parser.add_argument('-o',metavar="OUT_FILE", default="users.txt", help="Output file name")
    parser.add_argument("-l", metavar="\"FIRST LAST\"",nargs='+', help="Input a list of names as arguments. Use \"[First name] [Last name]\" to input full names ")
    args = parser.parse_args()
    clear()
    banner()
    if args.o:
        out_file = args.o
    if args.i or args.l:
        if args.i:
            print(info, "Loading names from file")
            try:
                f = open(args.i)
            except FileNotFoundError:
                print(err, "Input file not found")
                sys.exit(1)
            for l in f:
                names.append(l)

        else:
            print(info, "Loading names from arg list")
            names = args.l
    else:
        get_name()
    display_names()
    export_names()
    generate_usernames()
