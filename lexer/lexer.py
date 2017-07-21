import re


# READ FIRST!!!
# THIS IS UNFINISHED! THE LEXER SHOULD BE FINISHED BY TOMMAROW

def isfloat(value):
         try:
               float(value)
               return True
         except ValueError:

                  return False
def isint(value):
         try:
               int(value)
               return True
         except ValueError:

                  return False
def isreg(value):
         try:
               if(len(value) == 3 and isint(value)!=True and isfloat(value)!=True):

                return True
               else:
                return False
         except ValueError:

                  return False
def getbrackets(value):
    return re.compile( "\[(.*)\]" ).search( value ).group( 1 )
def getspikebrackets(value):
    return re.compile( "\{(.*)\}" ).search( value ).group( 1 )


class lexer:

   

   def lex(self,code):

     
 
     returnlex = []
     for c in code:

        split1 = c.split(',')
        #print(split1)
        errors = 0
        for i in range(0,len(split1)):
            #try:
             if(split1[i] == "NEW"):
                  #checks if its a int
                  if(isint(split1[i+2])):
                   val = int(split1[i+2])
                   returnlex.append("DECRG I,{0},{1}".format(val,split1[i+1]))
                  #checks if its a float
                  elif(isfloat(split1[i+2])):
                   val = float(split1[i+2])
                   returnlex.append("DECRG F,{0},{1}".format(val,split1[i+1]))
                  #else it is a string
                  else:
                   val = split1[i+2]
                   returnlex.append("DECRG S,{0},{1}".format(val,split1[i+1]))
                  i+=2
             #print
             elif(split1[i] == "PRT"):
                returnlex.append("PRINT ,{0}".format(split1[i+1]))
             #Swap
             elif(split1[i] == "SWP"):
                returnlex.append("SWAP ,{0},{1}".format(split1[i+1],split1[i+2]))
             #Delete
             elif(split1[i] == "DEL"):
                returnlex.append("DELETERG ,{0}".format(split1[i+1]))
             #Random
             elif(split1[i] == "RND"):
                returnlex.append("RANDOM ,{0},{1},{2}".format(split1[i+1],split1[i+2],split1[i+3]))
             #Math
             elif(split1[i] == "MAT"):
                #if its plus
                if(split1[i+1] == "+"):

                    returnlex.append("MATH ,+,{0},{1},{2}".format(split1[i+2],split1[i+3],split1[i+4]))
                #if its minus
                elif(split1[i+1] == "-"):

                    returnlex.append("MATH ,-,{0},{1},{2}".format(split1[i+2],split1[i+3],split1[i+4]))
                #if its multiplication
                elif(split1[i+1] == "*"):

                    returnlex.append("MATH ,*,{0},{1},{2}".format(split1[i+2],split1[i+3],split1[i+4]))
                #if its division
                elif(split1[i+1] == "/"):

                    returnlex.append("MATH ,/,{0},{1},{2}".format(split1[i+2],split1[i+3],split1[i+4]))
                #else it returns a error string
                else:
                    returnlex.append("MATH !{0}!".format(split1[i+1]))
             #Function
             elif(split1[i] == "FNC"):
                    e = i+2
                    functiontext = ""
                    arr = []

                    while(e < len(split1)):
                        print(split1[e])
                        if(e != len(split1)-1):

                            functiontext += split1[e]+","
                        else:
                            functiontext += split1[e]

                        e+=1

                    tolex = getspikebrackets( functiontext )
                    outtext = ""
                    arr = tolex.split("|")
                    np = 0
                    l = lexer()
                    arrd=l.lex(arr)
                    for n in arrd:
                        if(np != len(arr)-1):
                             
                            outtext+=n+"|"
                        else:
                            outtext+=n

                        np+=1
                    
                    returnlex.append("FUNCTION {0}, [{1}]".format(split1[i+1],outtext))


            #except:
              #errors+=1
              #pass  
         
    
     return returnlex

l = lexer()
print(l.lex(["FNC,ADA,{MAT,+,50,50,OUT|NEW,TXT,512}","NEW,HIT,321"]))

