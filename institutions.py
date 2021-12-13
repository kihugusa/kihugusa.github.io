### Assignment 21

# 1) Print number of institutions in the file based on state
        
def getState():
    state = input("Enter the two character abbreviation for the state: ").upper()
    while len(state) != 2 or not state.isalpha():
        print("Error - invalid input")
        state = input("Enter the two character abbreviation for the state: ").upper()
    
    return state


def allStates():
    states = ["AL","AK","AZ","AR","CA","CO","CT","DE","FL","GA","HI","ID","IL","IN",
          "IA","KS","KY","LA","ME","MD","MA","MI","MN","MS","MO","MT","NE","NV",
          "NH","NJ","NY","NM","NC","ND","OH","OK","OR","PA","RI","SC","SD","TN",
          "TX","UT","VT","VA","WA","WV","WI","WY"]

    return states

def summary(state, count, percent):
    print("The number of universities in",state,"is",count,"which is",percent,"% of all schools.")
    

def main():  
    with open("UniversitiesWithStates.txt","r") as uni:
        count = 0
        lines = 0
        state = getState()

        for line in uni:
            line = line.rstrip()
            if line.endswith(state):
                count = count + 1
            lines = lines + 1

        if count > 0:
            percent = round(float(count*100/lines),1)
            summary(state,count,percent)
        else:
            print("There are no universities listed in "+str(state)+". Check your spelling.") 

main()


# 2) UniversitiesWithStates2.txt: City value is comma separated
# No. 1 Revision

def getState():
    state = input("Enter the two character abbreviation for the state: ").upper()
    while len(state) != 2 or not state.isalpha():
        print("Error - invalid input")
        state = input("Enter the two character abbreviation for the state: ").upper()
    
    return state


def allStates():
    states = ["AL","AK","AZ","AR","CA","CO","CT","DE","FL","GA","HI","ID","IL","IN",
          "IA","KS","KY","LA","ME","MD","MA","MI","MN","MS","MO","MT","NE","NV",
          "NH","NJ","NY","NM","NC","ND","OH","OK","OR","PA","RI","SC","SD","TN",
          "TX","UT","VT","VA","WA","WV","WI","WY"]

    return states

def summary(state, count, percent):
    print("The number of universities in",state,"is",count,"which is",percent,"% of all schools.")
    

def main():  
    with open("UniversitiesWithStates2.txt","r") as uni:
        count = 0
        lines = 0
        state = getState()

        for line in uni:
            line = line.rstrip()
            line = line.split(", ")
            if (len(line) == 3 and line[2] == state) or (len(line) == 2 and line[1] == state):
                count = count + 1
            lines = lines + 1
        
        if count > 0:
            percent = round(float(count*100/lines),1)
            summary(state,count,percent)
        else:
            print("There are no universities listed in "+str(state)+". Check your spelling.") 

main()





