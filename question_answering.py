import nltk 
import re

class QA_System: 
    def __init__(self): 
        self.conditions = {
            "italian" : "cuisine",
            "breakfast" : "food_type"
        }
    
    def load_conditions(): 
        # go through csv 
        # for each col, set key = val in col, value = col name
        pass
    def get_time_condition(self,tokens):
        for j in range(0, len(tokens)):
                    wordAfterTime = tokens[j]
                    if wordAfterTime.isdigit():
                        return str(int(wordAfterTime) + 12)
                    if wordAfterTime.strip("pm").isdigit():
                        return str(int(wordAfterTime.strip("pm")) + 12)

    def get_conditions(self, sentence): 
        where_condition = ""
        tokens = nltk.word_tokenize(sentence)
        for i in range(0,len(tokens)): 
            word = tokens[i]
            new_condition = None
            if word == "open" or word == "opens":
                time_condition = self.get_time_condition(tokens[i:])
                new_condition = time_condition + " BETWEEN open AND close"  
            elif word == "close" or word == "closed":
                time_condition = self.get_time_condition(tokens[i:])
                new_condition = time_condition + " NOT BETWEEN open AND close" 
            
            if word in self.conditions: 
                column = self.conditions[word]
                new_condition = column + ' = ' + word

            if new_condition :
                if len(where_condition) == 0: 
                    where_condition +=  new_condition
                else: 
                    where_condition += " AND " +  new_condition              
        return where_condition



# COLS: Location, Open, Close, Cuisine, Diet, MealType 

# What restaurant serves italian* and when does it open*? -> Name* opens at time* 

# SELECT restaurant FROM Name, Time 


def main(): 
    qa = QA_System()
    sentence1 = "What restaurants serve italian and serve breakfast that is open at 2?"
    sentence = "What time does Brunch open?" 
    sentence = "When does Brunch open?"
    sentence2 = "What restaurants are open at 5pm"
    sentence3 = "where serves italian breakfast?"
    # see open or close, then go to end until you see a number g
    # Have a special query to see if between a time 
    sentences = [sentence1, sentence2, sentence3]
    print('\n')
    for test in sentences:
        print(test )
        print("SELECT * FROM t WHERE " + qa.get_conditions(test), '\n')




if __name__ == "__main__": 
    main()