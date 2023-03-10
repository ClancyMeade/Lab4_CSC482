import nltk 
import time
import re
from getpass import getpass
from mysql.connector import connect, Error

class QA_System: 
    def __init__(self):
        # Translates words to corresponding SQL column
        # to be used in WHERE clause of SQL query
        self.table_name = "dining"
        self.test_file = "test_sentences.txt"
        self.conditions = {}
        # Translates words to corresponding SQL column 
        # to be used in SELECT of SQL query 
        self.question_translations = {
        # TABLE COLS: name, cuisine, diet, food_type, open, close            
            "restaurant" : "name",
            "restaurants" : "name",
            "which" : "name", 
            "where": "name",
            "places" : "name",
            "dining" : "name", 
            "food" : "cuisine", 
            "type" : "food_type",             
            "meals" : "food_type",                                              
        }
        self.load_conditions() # load the conditions when initialized
        
        
    # Loads conditions table with data from csv files 
    def load_conditions(self):
        # Read cuisine types 
        cuisine_file = open("./data/cuisine.csv", 'r')
        for line in cuisine_file: 
            tuple = line.strip().split(",")
            name = tuple[0]
            cuisine = tuple[1] 
            self.conditions[cuisine] = "cuisine" 
            # add name also 
            self.conditions[name] = "name"
        # Read diet types 
        diet_file = open("./data/diet.csv", 'r')
        for line in diet_file:
            tuple = line.strip().split(",")
            diet = tuple[1]
            self.conditions[diet] = "diet"
        # Read meal types
        meal_types_file = open("./data/meal_type.csv", 'r')
        for line in meal_types_file:
            tuple = line.strip().split(",")
            meal_type = tuple[1]
            self.conditions[meal_type] = "food_type"                                         


    # Returns tokens in sentence 
    # Removes punctuation and converts to lower case
    def get_tokens(self, sentence): 
        sentence = re.sub(r"[^a-zA-Z0-9\s]", "", sentence)
        tokens = [w.lower() for w in nltk.word_tokenize(sentence)]
        return tokens         


    # Returns the SELECT condition for the query
    # obtained by converting words in tokens to SQL 
    def get_select_condition(self, sentence):
        tokens = self.get_tokens(sentence)
        desired_cols = []
        for i in range(0,len(tokens)):
            word = tokens[i]
            if "open" in word:
                time_check = self.get_time_condition(tokens[i:])
                #print("open_check: ", time_check)
                if time_check is None:
                    #assume we are looking for a time
                    desired_cols.append("open")
                    tokens[i] = "-used-"                    
            elif "clos" in word:
                time_check = self.get_time_condition(tokens[i:])
                if time_check is None:
                    #assume we are looking for a time
                    desired_cols.append("close")
                    tokens[i] = "-used-"
            # Look for translation from question word to SQL 
            elif word in self.question_translations: 
                desired_cols.append(self.question_translations[word])
                tokens[i] = "-used-"
        if len(desired_cols) > 0:
            from_statement = "SELECT "
            from_statement += ", ".join(desired_cols)
            return [from_statement,tokens]


    # Given the end of a sentence, looks for a number representing a time
    # Returns a string representing the 24 hour time
    def get_time_condition(self, tokens):
        for j in range(0, len(tokens)):
            wordAfterTime = tokens[j]
            if wordAfterTime.isdigit():
                return str(int(wordAfterTime) + 12)
            if wordAfterTime.strip("pm").isdigit():
                return str(int(wordAfterTime.strip("pm")) + 12)


    # Adds quotes to strings used in SQL query 
    def add_quotes(self, condition):
        if "=" in condition:
            orig_condition = condition[: condition.index("=") + 2] 
            condition = condition[condition.index("=") + 1 : ]
            condition = condition.strip()
            if condition.isnumeric():
                return
            new_cond =  "'" + condition + "'"
            where_cond = orig_condition + new_cond
            return where_cond
        else:
            return condition


    # Returns the WHERE clause for the query 
    # obtained by converting words in tokens to SQL 
    def get_where_clause(self, tokens): 
        where_clause = "WHERE "
        for i in range(0,len(tokens)): 
            word = tokens[i]
            new_condition = None
            # Check if word can be converted to column in SQL table, and set new_condition if it can
            if word in self.conditions: 
                column = self.conditions[word]
                new_condition = column + ' = ' + word            
            # Check if word relates to opening
            elif "open" in word or (word == 'now' and "open" not in tokens[i-1]):
                # If time given later in sentence, use it. If not given, use current time. 
                time_condition = self.get_time_condition(tokens[i:])
                if time_condition is None: # no time given, use current time 
                    t = time.localtime(time.time())
                    time_condition = round(t.tm_hour + t.tm_min/60, 2)
                new_condition = str(time_condition) + " BETWEEN open AND close" 
            # Check if word relates to closing 
            elif "clos" in word or (word == 'now' and "open" not in tokens[i-1]):
                # If time given later in sentence, use it. If not given, use current time. 
                time_condition = self.get_time_condition(tokens[i:])
                if time_condition is None: # curr time 
                    t = time.localtime(time.time())
                    time_condition = round(t.tm_hour + t.tm_min/60, 2)
                new_condition = str(time_condition) + " NOT BETWEEN open AND close"             
            if new_condition :
                if where_clause == "WHERE ": 
                    where_clause += self.add_quotes(new_condition)
                else: 
                    where_clause += " AND " +  self.add_quotes(new_condition)
        return where_clause


    # Reads in test questions from file and prints their corresponding SQL statements 
    def test(self): 
        test_file = open(self.test_file, 'r') 
        for sentence in test_file: 
            question = sentence.strip()
            print(question)
            select_tuple = self.get_select_condition(question)
            select_statement = select_tuple[0]
            tokens_after_select = select_tuple[1]
            query = select_statement + \
                    " FROM " + self.table_name + " " \
                    + self.get_where_clause(tokens_after_select)
            print(query)
            # Query database 
            output = []
            try:
                with connect(
                    host="localhost",
                    user="root",
                    password="",
                    database="lab4",
                ) as connection:
                    with connection.cursor() as cursor:
                        cursor.execute(query)
                        result = cursor.fetchall()
                        for row in result:
                            if row not in output:
                                output.append(row)
            except Error as e:
                print(e)

            answer = "Here's what we found."
            for row in output:
                ans = ", ".join([str(val) for val in row])
                answer = answer + "\n" + ans

            print()
            print(answer)
            print()
            print("###########################################")
            print()

    # Returns the answer to question 
    # Converts question to SQL and queries the database 
    def get_answer(self, question):
        select_tuple = self.get_select_condition(question)
        select_statement = select_tuple[0]
        tokens_after_select = select_tuple[1]
        query = select_statement + \
                " FROM " + self.table_name + " " \
                + self.get_where_clause(tokens_after_select)
        print(query)
        # Query database 
        output = []
        try:
            with connect(
                host="localhost",
                user="root",
                password="",
                database="lab4",
            ) as connection:
                with connection.cursor() as cursor:
                    cursor.execute(query)
                    result = cursor.fetchall()
                    for row in result:
                        if row not in output:
                            output.append(row)
        except Error as e:
            print(e)

        answer = "Here's what we found."
        for row in output:
            ans = ", ".join([str(val) for val in row])
            answer = answer + "\n" + ans    
        return answer 
