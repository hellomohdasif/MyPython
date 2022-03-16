

from csv import reader



for i in range(0,20):
    for j in range(0, 19):
        with open("C:/Users/Asif/Desktop/1.csv", 'r') as f:
            lines = f.readlines()
            f = ''.join(f)
            f = f.replace('[', '  ')

            with open("C:/Users/Asif/Desktop/2.csv", 'r') as k:
                lines2 = k.readlines()
                k = ''.join(k)
                k = k.replace('[', '  ')
                if lines[i] !== lines2[j]:
                    print(lines[i])









