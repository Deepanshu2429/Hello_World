



def findTop4PsychologistwithLessLinkOpenings(Dict):
   if len(Dict)<4:
       list3=list(Dict.keys())
       return list3
   else:
       list3=list(Dict.keys())
       list1 = list(Dict.values())
       list2=sorted(list1)
       x=[]
       ind1=list1.index(list2[0])
       x.append(list3[ind1])
       list1.remove(list2[0])
       list3.remove(list3[ind1])
       ind2=list1.index(list2[1])
       x.append(list3[ind2])
       list1.remove(list2[1])
       list3.remove(list3[ind2])
       ind3=list1.index(list2[2])
       x.append(list3[ind3])
       list1.remove(list2[2])
       list3.remove(list3[ind3])
       ind4=list1.index(list2[3])
       x.append(list3[ind4])
       list1.remove(list2[3])
       list3.remove(list3[ind4])
       return x