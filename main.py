file_name=input('ENTER THE FILE NAME ')
search_string=input('ENTER THE WORD YOU WANT TO SEARH ')
f=open(file_name)
file_lines=f.readlines()
found=False
counter=0
for line in file_lines:
    words=line.split()
    for word in words:
        if(word==search_string):
            found=True
            counter=counter+1
if(found==True):
    print('THE WORD IS PRESENT ',counter,'TIMES')
else:
    print('THE WORD IS NOT PRESENT')