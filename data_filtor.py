
# mosified = []
# for line in readse:
#     if line not in mosified:

    
#         mosified.append(line.strip())


    
    # if line[-1]=='\n':
    #     mosified.append(line[:-1])

    # else:
    #     mosified.append(line)

# # foe = mosified.replace("[]","")
# filws = open("past.txt", "w")
# foe = filws.write(str(mosified))
# rt = file.readlines()


from speek import say

# txt = input("enter: ")
def brain(txt):
    file = open("databas\\chat_data.txt", "r")

    Qustion = " "
    Answer = " "
    # dr = ""
    split_words = " "
    count = 1
    while (Qustion):
        Qustion = file.readline()
        # l = readse.split()
        len_of_txt = len(txt)
        if len_of_txt>=7:
            if txt in Qustion:
                # print(readse)
                # ert = count+1
                reding_lines = file.readline()[0:]
                replace_Word = reding_lines.replace("Answer :", "")
                more_replace_word = replace_Word.replace("Luna:","")
                tf = f'"{more_replace_word}"'
                # trg = rt.replace("\n","")
                # print(f"{rt}\n")

                question_word_filter = Qustion.replace("You:","")
                more_question_word_filter = question_word_filter.replace("Question :", "")
                question_Words_spliting = more_question_word_filter.split()
                # print(sx)
                split_words = more_question_word_filter
                Answer = more_replace_word

                # print((more_question_word_filter,Answer))
                # kk = open("res.py","w")
                # kk.write(me)

    
        count+=1
    # print(split_words,Answer)
    return say(Answer)


    
# while True:
#     print(more_question_word_filter,Answer)
while True:
    print(brain(input("enter: ")))