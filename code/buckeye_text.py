#importing corpus tool
import buckeye 

# Generating corpus
corpus = buckeye.corpus('/home/ansost/buckeye_corpus')

#iterating over all 40 speakers form corpus
for speaker in corpus:
    
    #init word_list
    word_list = []
    #print('speaker here!')
    
    #each speaker has up to 6 tracks (interviews)
    #iterating over each interview of a speaker
    for track in speaker:
        
        #iterating over each word for wach interview to append it to the dataframe
        for word in track.words: 
            
            #the word attribute has two attributes: word and pause. 
            #We dont want the pauses and they dont have an orthography attribute
            if hasattr(word, 'orthography'): 
                word_list.append(word.orthography)

    #writing the word_list to new file 
    new_file = open('/home/ansost/buck_me/' + speaker.name + ".txt", "w")
    for line in word_list:
        new_file.write(line +'\n')
    new_file.close()