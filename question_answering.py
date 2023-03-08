import nltk 
import re

class QA_System: 
    def __init__(self): 
        self.conditions = {
            "italian" : "cuisine",
            "breakfast" : "food_type"
        }
        self.question_translations = {
            "restaurant" : "name",
            "restaurants" : "name",
            "where": "name",

        }
    
    def load_conditions(): 
        # go through csv 
        # for each col, set key = val in col, value = col name
        pass

    def get_select_condition(self,sentence):
        tokens = nltk.word_tokenize(sentence)
        desired = None
        for i in range(0,len(tokens)):
            word = tokens[i]
            if "open" in word:
                time_check = self.get_time_condition(tokens[i:])
                print("open_check: ", time_check)

                if time_check is None:
                    #assume we are looking for a time
                    desired = "open"
                    tokens[i] = "-used-"

            if "clos" in word:
                time_check = self.get_time_condition(tokens[i:])
                if time_check is None:
                    #assume we are looking for a time
                    desired = "close"
                    tokens[i] = "-used-"
                    
                    
            if word in self.question_translations: #if 'resuraunt' is in the question, it will know it is looking for the resuraunt name
                desired = self.question_translations[word]
                tokens[i] = "-used-"
            if desired:
                return [desired,tokens]

    def get_time_condition(self,tokens):
        for j in range(0, len(tokens)):
                    wordAfterTime = tokens[j]
                    if wordAfterTime.isdigit():
                        return str(int(wordAfterTime) + 12)
                    if wordAfterTime.strip("pm").isdigit():
                        return str(int(wordAfterTime.strip("pm")) + 12)

    def get_conditions(self, tokens): 
        where_condition = ""
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
    sentence1 = "What restaurants serve italian, serve breakfast and is open at 2?"
    sentence4 = "What time does Brunch open?" 
    sentence = "When does Brunch open?"
    sentence2 = "What restaurants are open at 5pm"
    sentence3 = "where serves italian breakfast?"
    # see open or close, then go to end until you see a number g
    # Have a special query to see if between a time 
    sentences = [sentence1, sentence2, sentence3, sentence4]
    print('\n')
    for test in sentences:
        print(test )
        select_tuple = qa.get_select_condition(test)
        select_statement = select_tuple[0]
        tokens_after_select = select_tuple[1]
        print("SELECT " + select_statement)
        print(" FROM t WHERE " + qa.get_conditions(tokens_after_select), '\n')




if __name__ == "__main__": 
    main()