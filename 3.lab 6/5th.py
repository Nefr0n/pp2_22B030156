names = ['Rolan', 'Thorfinn', 'White', 'Thorkell', 'Canute', 'Askeladd']
with open('abc.txt', "w") as myfile:
        for i in names :
                myfile.write("%s\n" % i)

content = open('legend.txt')
print(content.read())
