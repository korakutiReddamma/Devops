file = open('docker.txt','r')
filedata = file.readlines()
key1 = 'RUN'
key2 = 'USER'
count = 0
for number, line in enumerate(filedata,1):
    
    if key1 in line:
        count+=1
        print(f'{key1} is at line {number}')
    if 'COPY' in line:
        COPY="add"
        print(COPY)
if count > 1:
    print('There are more then one RUN')
elif 'USER\n' in filedata:
    print('USER Exist')
elif ('USER\n' not in filedata) and ('RUN\n' not in filedata):
    print('Other words are there in data')
elif 'USER\n' not in filedata:
    print('User is not found')
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
# if count > 1:
#     raise runError("There are more RUN in the file data",count)
# elif key1 != 'RUN' or key2 != 'USER':
#     raise otherError("There are other words except RUN and USER")

# if key2  in filedata:
#     print("USER is existing in the file data")
# else:
#     raise userError("USER is not found in the file data")
    
    
    
    
    
    
    
    
    
    
    
    
# print(len(filedata))
# print(filedata.count('RUN\n'))
# for i in range(len(filedata)):
#     a=filedata[i]
    # print(a)
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      