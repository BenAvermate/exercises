with open('input.txt') as file:
    with open('output.txt','w') as out:
        for line in file:
            name,points = line.split(':')
            point,change = points.split(' ')
            #cashed, total = map(int, points.split('/'))
            cashed,total = point.split('/')
            cashed = int(cashed)
            total = int(total)

            #total += change.count('+')
            #cashed += change.count('-')
            for c in change:
                if c == "+":
                    total+=1
                if c == "-":
                    cashed+=1
            
            out.write(f'{name}:{cashed}/{total}\n')