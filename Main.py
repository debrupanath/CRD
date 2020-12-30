

import code as debi 
#importing the main file("code" is the name of the file I have used) as a library 


x.create("Debi",99)
#to create a key with key_name,value given and with no time-to-live property


x.create("source",10,48000) 
#to create a key with key_name,value given and with time-to-live property value given(number of seconds)


x.read("Debi")
#it returns the value of the respective key in Jasonobject format 'key_name:value'


x.read("source")
#it returns the value of the respective key in Jasonobject format if the TIME-TO-LIVE IS NOT EXPIRED else it returns an ERROR


x.create("Debi",100)
#it returns an ERROR since the key_name already exists in the database
#To overcome this error 
#either use modify operation to change the value of a key
#or use delete operation and recreate it


x.modify("Debi",95)
#it replaces the initial value of the respective key with new value 

 
x.delete("Debi")
#it deletes the respective key and its value from the database(memory is also freed)


#the code also returns other errors like 
#"invalidkey" if key_length is greater than 32 or key_name contains any numeric,special characters etc.,
#"key doesnot exist" if key_name was mis-spelt or deleted earlier
#"File memory limit reached" if file memory exceeds 1GB
