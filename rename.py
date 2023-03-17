import os, csv, argparse

def rr(file_dir:str, csv_file:str):
    with open(os.path.abspath(csv_file),'r', encoding='utf-8')as f:
        reader = list(csv.reader(f))
    path = os.path.abspath(file_dir)
    file_list = os.listdir(path)
    file_list.sort()
    file_end = os.path.splitext(file_list[0])[-1]

    for x in file_list:
        try:
            index = int(os.path.splitext(x)[0])
        except ValueError:
            print("Error File Name")
            continue
        try:
            name = str(reader[index][0]) + "_" + str(reader[index][1]) + "_" + str(reader[index][2]) + file_end
            os.rename(os.path.join(path, x), os.path.join(path, name))
        except IndexError:
            print("Not Exist in Csv File")
            continue
    print("rename done")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Rename file according to csv file')
    parser.add_argument('-csv', dest='csv', type=str, help='Path of csv file')
    parser.add_argument('-file', dest='file', type=str, help='Path of file needs to be renamed')
    args = parser.parse_args()

    rr(args.file, args.csv)
