import json

#Open the dictionary file
dictfile = open('dictionary.json',)

#load the dictionary file into a database 
database = json.load(dictfile)

#Close the file now that I am done with it
dictfile.close()

# for each entry in the dictionary
for entry in database:
    print("========================\n")
    #print the entry
    print(entry)
    #get the definition of for the entry
    definition = database[entry]
    #print the definition
    print(definition)

