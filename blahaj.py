import argparse

from termcolor import cprint

parser = argparse.ArgumentParser(description = "blahaj [arguments]")
parser.add_argument("-c", "--colors", nargs=1, metavar="flag", type=str, help="sets desired color scheme")# done
parser.add_argument("-t", "--text", nargs="*", metavar="text", type=str, help="text to colorize")# done
parser.add_argument("-i", "--individual", action='store_true', help="Color individual characters")# done
parser.add_argument("-w", "--words", action='store_true', help="Color individual words")# done
parser.add_argument("-f", "--flag", action='store_true', help="Returns as flag")
parser.add_argument("-s", "--shark", action='store_true', help="returns as blahaj")
parser.add_argument("-b", "--background", action='store_true', help="Color the background")
parser.add_argument("-r", action='store_true', help="selects a random color scheme")
args = parser.parse_args()
if args.colors != None:
    scheme = args.colors[0]
    arr = [(50, 60, 70),(80, 90, 70), (150, 160, 100)]
    scheme = arr
    print(scheme)
    if args.flag:
        for j in range(len(scheme)):
            cprint("                    ", scheme[j],scheme[j])
elif args.shark:
    #change to do blahaj
    if args.background:
        for j in range(len(string)):
            cprint(string[j], "black", arr[j%len(arr)], end="")
elif args.text != None:
    string = ""
    print(args.text)
    if len(args.text) >=2:
        for j in range(len(args.text)-1):
            string = string + args.text[j] + " "
        string = string + args.text[len(args.text)-1]
    else:
        string = args.text[0]
    print(string)
    arr = ["magenta","green", "yellow"]
    # cprint("Hello, World!", "green")
    if args.background:
        if args.individual:
            for j in range(len(string)):
                cprint(string[j], arr[j%len(arr)], end="")
        elif args.words:
            split = string.split(" ")
            for j in range(len(split)-1):
                cprint(split[j],arr[j%len(arr)], end=" ")
                cprint(split[len(split)-1],arr[len(split)%len(arr)], end="")
