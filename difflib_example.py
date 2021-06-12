#inputs
lookupword = "dargo"
listordict = {"dago", "doggo" , "drago", "margo" }

#Use the difflib library to find close words
import difflib
closewords = difflib.get_close_matches(lookupword, listordict)

print(closewords)
#Optional, convert it to a string
print("Not in dictionary.")
print("Did you mean " + str(closesewords) + " ?")