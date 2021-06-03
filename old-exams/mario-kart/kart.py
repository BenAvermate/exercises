def scoreTelling(ranking):
    for i in range(100):
        score[ranking[i]]=score.get(ranking[i],0)+i+1

score= {}
with open("input.txt") as rankings:
    #lees per 100
    for race in range(100):
        begin=race*100
        end = (race+1) *100
        ranking=[]
        for racer in range(100):
            ranking.append(rankings.readline().strip())
        #geef punten via index reverse sorted
        scoreTelling(ranking[::-1])
    score = sorted(score.items(), key=lambda item: item[1], reverse=True)
with open("output.txt","w") as out:
    for racer,_ in score[0:10]:
        print(racer,file=out)