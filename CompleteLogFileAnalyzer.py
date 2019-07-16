import re
import time
from time import strftime

from pip._vendor.msgpack.fallback import xrange


def main():
    log_file_path = r"/Users/chinmaybhosale/Downloads/data.log"
    export_file_path = r"users/chinmaybhosale/Downloads"

    time_now = str(strftime("%Y-%m-%d %H-%M-%S", time.localtime()))

    file = "\\" + "Parser Output " + time_now + ".txt"
    export_file = export_file_path + file

    regex = '(<property name="(.*?)">(.*?)<\/property>)'

    parseData(log_file_path, export_file, regex, read_line=True)


def parseData(log_file_path, export_file, regex, read_line=True):
    with open(log_file_path, "r") as file:
        match_list = []
        if read_line == True:
            for line in file:
                for match in re.finditer(regex, line, re.S):
                    match_text = match.group()
                    match_list.append(match_text)
                    print(match_text)
        else:
            data = file.read()
            for match in re.finditer(regex, data, re.S):
                match_text = match.group();
                match_list.append(match_text)
    file.close()

    with open("output", "w+") as file:
        file.write("EXPORTED DATA:\n")
        match_list_clean = list(set(match_list))
        for item in xrange(0, len(match_list_clean)):
            print(match_list_clean[item])
            file.write(match_list_clean[item] + "\n")
    file.close()


if __name__ == '__main__':
    main()
