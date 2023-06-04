from Code.Data.crawling import crawling

with open('Data/Restaurant_Link.csv', 'r') as file:
    lines = file.read().split('\n')

name = []
link = []
for i in range(len(lines)):
    a, b =lines[i].split(',')
    name.append(a)
    link.append(b)


for i in range(25, len(lines)):
    print(name[i], link[i])
    crawling(name[i], link[i])
