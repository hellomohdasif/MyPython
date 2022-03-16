datanew = ["a","b","c","d","e"]
for element in datanew:
    with open('C:\\Users\\Asif\\Desktop\\base.txt',"r+") as f:
        if element in f.read():
            print("Already Exits")
        else:
            with open('C:\\Users\\Asif\\Desktop\\nameheap.txt', "a") as myfile:
                myfile.write(element + "\n")

                f.write(element + "\n")

                print("SAVED!!")



