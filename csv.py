
import os

class Data:
    entries = []
    files = []
    lines = []
    result_file = open("results.csv","w")

class Entry:
    def __init__(self, name, publisher, i_date, d_version):
        self.name = name
        self.publisher = publisher
        self.i_date = i_date
        self.d_version = d_version
        self.count = 1

def process_filenames():
    for i in os.listdir(os.getcwd()):
        if i.endswith(".csv"):
            Data.files.append(i)

def process_lines():
    for entry in Data.files:
        o = open(entry, "r")
        for line in o.readlines():
            Data.lines.append(line)

def get_csv():
    flag = 0
    charbuffer = ""
    csv = []
    csv_array = []
    for line in Data.lines:
        for char in line:
            if char == '"' and flag == 0:
                flag = 1
            elif char == '"' and flag == 1:
                flag = 0
            elif char == "," and flag == 0:
                csv.append(charbuffer)
                charbuffer = ""
            elif flag == 1:
                charbuffer = charbuffer + char
        csv.append(charbuffer)
        charbuffer = ""
        csv_array.append(csv)
        csv = []
    return csv_array

def create_entry_objects():
    csv_array = get_csv()
    for entry in csv_array:
        if len(entry) == 4:
            Data.entries.append(Entry(entry[0],entry[1],entry[2],entry[3]))

def find_duplicates():
    i = 0
    while i < (len(Data.entries)):
        j = i + 1
        while j < (len(Data.entries)):
            if Data.entries[i].name == Data.entries[j].name and Data.entries[i].d_version == Data.entries[j].d_version:
                Data.entries[i].count += 1
                Data.entries.remove(Data.entries[j])
                j = j - 1
            j = j + 1
        i = i + 1

def write_results():
    Data.result_file.write('"ProgramName","Version","Count"' + "\n")
    for entry in Data.entries:
        if entry.name != "ProgramName":
            Data.result_file.write('"'+entry.name+'"' + "," + '"' + str(entry.d_version.strip("\n")) + '"' + "," + '"' + str(entry.count) + '"' + "\n")

def run():
    process_filenames()
    process_lines()
    create_entry_objects()
    find_duplicates()
    write_results()

run()
