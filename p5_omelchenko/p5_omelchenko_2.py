try:
    word_list = []
     
    while True:
        word_list.append((input()))
        
except:
    for i in range(len(word_list)):
        if(i == len(word_list) - 2): print(word_list[i], end = ' and ') 
        elif(i == len(word_list) - 1): print(word_list[i])
        else: print(word_list[i], end = ', ') 

#"ctrl+z" to finish input