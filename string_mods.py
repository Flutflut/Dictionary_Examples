mydefinitions = {
    "adam" : "the coolest guy ever. see amazing.",
    "yesha" : "amazing.",
    "cooker" : "cookies.",
    "yumyum" : "see cookies.",
    "cookies" : "a tasty treat.",
    "adamazing" : "better than amazing. see adam. see amazing.",
    "amazing" : "something really good.",
    "something broken" : "see something bad.",
    "something bad" : "A definition which does not work."
    }

print("== List Contents ==")  
  
for word in mydefinitions:
    print("-" + word)
    print(mydefinitions[word])

print("== Split definition ==") 

searchword = "adam"
definition = mydefinitions[searchword]
splitDefinition = definition.split()
print(splitDefinition)

print("== Singleword Definition ==") 

searchword = "cooker"
definition = mydefinitions[searchword]
splitDefinition = definition.split()
if( len(splitDefinition) == 1):
    print("Oneword")
else:
    print( str(len(splitDefinition)) + " words")
    
print("== Firstword match ==") 

searchword = "yumyum"
definition = mydefinitions[searchword]
splitDefinition = definition.split()

if( splitDefinition[0] == "see"):
    print("Lookup " + splitDefinition[1])

print("== Has a period test ==") 

testitem = "test."

if "." in testitem:
    print("Has a period")
else:
    print("No period")

print("== Remove period ==") 

testitem = "test."
testitem = testitem.replace('.','')
print(testitem)








