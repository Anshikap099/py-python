#wap to fill in a letter template given below witth name and date
letter='''
 Dear <|Name|>,
 you are selected!
<|Date|>
 '''

print(letter.replace("<|Name|>","anshika").replace("<|Date|>", "17 jan 2027"))