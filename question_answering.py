import nltk 

class QA_System: 
    def __init__(self): 
        self.conditions = {
            "italian" : "cuisine",
            "breakfast" : "food type"
        }
    
    def load_conditions(): 
        # go through csv 
        # for each col, set key = val in col, value = col name
        pass
    
    def get_conditions(self, sentence): 
        where_condition = ""
        for word in nltk.word_tokenize(sentence): 
            if word in self.conditions: 
                column = self.conditions[word]
                if len(where_condition) == 0: 
                    where_condition +=  column + ' = ' + word
                else: 
                    where_condition += " AND " +  column + ' = ' + word               
        return where_condition



# COLS: Location, Open, Close, Cuisine, Diet, MealType 

# What restaurant serves italian* and when does it open*? -> Name* opens at time* 

# SELECT restaurant FROM Name, Time 


def main(): 
    qa = QA_System()
    sentence = "What restaurants serve italian and serves breakfast?"
    sentence = "What time does Brunch open?" 
    sentence = "WHen does Brunch open?"
    sentence = "What restaurants is open at 5pm"
    # see open or close, then go to end until you see a number g
    # Have a special query to see if between a time 


    print(qa.get_conditions(sentence))




if __name__ == "__main__": 
    main()