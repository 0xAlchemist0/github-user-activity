#this package helps you parse and be able to use comand line flags ex: -h , string parameters , etc
import argparse

from github import get_user_events


def main():
    parser = argparse.ArgumentParser(description="A simple CLI tool")
    #-e is the command flag ex: -e param name
    #without it we have one flag which is nothing
    #the help is shown when using just the -h flag
    parser.add_argument("-e","--events", type=str, help="github events")
    
    args = parser.parse_args()
    get_user_events(args.events)

if __name__ == "__main__":
    main()
