-- cuisines

CREATE TABLE cuisines(
   name    VARCHAR(20) NOT NULL PRIMARY KEY
  ,cuisine VARCHAR(10) NOT NULL
);
INSERT INTO cuisines(name,cuisine) VALUES ('balance cafe','american');
INSERT INTO cuisines(name,cuisine) VALUES ('brunch','american');
INSERT INTO cuisines(name,cuisine) VALUES ('hearth','italian');
INSERT INTO cuisines(name,cuisine) VALUES ('jamba','smoothies');
INSERT INTO cuisines(name,cuisine) VALUES ('mingle and nosh','american');
INSERT INTO cuisines(name,cuisine) VALUES ('noodles','asian');
INSERT INTO cuisines(name,cuisine) VALUES ('streats','american');
INSERT INTO cuisines(name,cuisine) VALUES ('sweet bar','bakery');
INSERT INTO cuisines(name,cuisine) VALUES ('vista grande express','american');
INSERT INTO cuisines(name,cuisine) VALUES ('scout coffee','coffee');
INSERT INTO cuisines(name,cuisine) VALUES ('mustang station','burgers');
INSERT INTO cuisines(name,cuisine) VALUES ('red radish','salads');
INSERT INTO cuisines(name,cuisine) VALUES ('shake smart','smoothies');
INSERT INTO cuisines(name,cuisine) VALUES ('starbucks','coffee');
INSERT INTO cuisines(name,cuisine) VALUES ('health shack','wraps');
INSERT INTO cuisines(name,cuisine) VALUES ('julians','coffee');
INSERT INTO cuisines(name,cuisine) VALUES ('mustang eats','italian');
INSERT INTO cuisines(name,cuisine) VALUES ('subway','sandwiches');
INSERT INTO cuisines(name,cuisine) VALUES ('chick fil a','american');
INSERT INTO cuisines(name,cuisine) VALUES ('einstein','american');

-- diets


CREATE TABLE diets(
   name VARCHAR(15) NOT NULL PRIMARY KEY
  ,diet VARCHAR(11) NOT NULL
);
INSERT INTO diets(name,diet) VALUES ('balance cafe','vegetarian');
INSERT INTO diets(name,diet) VALUES ('balance cafe','vegan');
INSERT INTO diets(name,diet) VALUES ('balance cafe','halal');
INSERT INTO diets(name,diet) VALUES ('balance cafe','gluten free');
INSERT INTO diets(name,diet) VALUES ('brunch','vegetarian');
INSERT INTO diets(name,diet) VALUES ('brunch','vegan');
INSERT INTO diets(name,diet) VALUES ('brunch','halal');
INSERT INTO diets(name,diet) VALUES ('brunch','gluten free');
INSERT INTO diets(name,diet) VALUES ('hearth','vegetarian');
INSERT INTO diets(name,diet) VALUES ('hearth','vegan');
INSERT INTO diets(name,diet) VALUES ('hearth','halal');
INSERT INTO diets(name,diet) VALUES ('mingle and nosh','gluten free');
INSERT INTO diets(name,diet) VALUES ('mingle and nosh','vegetarian');
INSERT INTO diets(name,diet) VALUES ('mingle and nosh','vegan');
INSERT INTO diets(name,diet) VALUES ('noodles','gluten free');
INSERT INTO diets(name,diet) VALUES ('noodles','vegetarian');
INSERT INTO diets(name,diet) VALUES ('noodles','vegan');
INSERT INTO diets(name,diet) VALUES ('streats','vegetarian');
INSERT INTO diets(name,diet) VALUES ('streats','vegan');
INSERT INTO diets(name,diet) VALUES ('scout coffee','vegan');
INSERT INTO diets(name,diet) VALUES ('scout coffee','vegetarian');
INSERT INTO diets(name,diet) VALUES ('mustang station','vegan');
INSERT INTO diets(name,diet) VALUES ('mustang station','vegetarian');
INSERT INTO diets(name,diet) VALUES ('red radish','gluten free');
INSERT INTO diets(name,diet) VALUES ('red radish','vegetarian');
INSERT INTO diets(name,diet) VALUES ('red radish','vegan');
INSERT INTO diets(name,diet) VALUES ('health shack','gluten free');
INSERT INTO diets(name,diet) VALUES ('health shack','vegetarian');
INSERT INTO diets(name,diet) VALUES ('health shack','vegan');
INSERT INTO diets(name,diet) VALUES ('julians','vegetarian');
INSERT INTO diets(name,diet) VALUES ('julians','vegan');
INSERT INTO diets(name,diet) VALUES ('mustang eats','vegan');
INSERT INTO diets(name,diet) VALUES ('einstein','vegan');
INSERT INTO diets(name,diet) VALUES ('einstein','vegetarian');

-- meal types

CREATE TABLE meal_types(
   name      VARCHAR(20) NOT NULL PRIMARY KEY
  ,food_type VARCHAR(9) NOT NULL
);
INSERT INTO meal_types(name,food_type) VALUES ('balance cafe','breakfast');
INSERT INTO meal_types(name,food_type) VALUES ('balance cafe','lunch');
INSERT INTO meal_types(name,food_type) VALUES ('balance cafe','dinner');
INSERT INTO meal_types(name,food_type) VALUES ('brunch','breakfast');
INSERT INTO meal_types(name,food_type) VALUES ('brunch','lunch');
INSERT INTO meal_types(name,food_type) VALUES ('brunch','dinner');
INSERT INTO meal_types(name,food_type) VALUES ('hearth','lunch');
INSERT INTO meal_types(name,food_type) VALUES ('hearth','dinner');
INSERT INTO meal_types(name,food_type) VALUES ('jamba','drink');
INSERT INTO meal_types(name,food_type) VALUES ('mingle and nosh','lunch');
INSERT INTO meal_types(name,food_type) VALUES ('mingle and nosh','dinner');
INSERT INTO meal_types(name,food_type) VALUES ('noodles','lunch');
INSERT INTO meal_types(name,food_type) VALUES ('noodles','dinner');
INSERT INTO meal_types(name,food_type) VALUES ('streats','lunch');
INSERT INTO meal_types(name,food_type) VALUES ('streats','dinner');
INSERT INTO meal_types(name,food_type) VALUES ('sweet bar','dessert');
INSERT INTO meal_types(name,food_type) VALUES ('vista grande express','breakfast');
INSERT INTO meal_types(name,food_type) VALUES ('vista grande express','lunch');
INSERT INTO meal_types(name,food_type) VALUES ('vista grande express','dinner');
INSERT INTO meal_types(name,food_type) VALUES ('scout coffee','drink');
INSERT INTO meal_types(name,food_type) VALUES ('mustang station','lunch');
INSERT INTO meal_types(name,food_type) VALUES ('mustang station','dinner');
INSERT INTO meal_types(name,food_type) VALUES ('red radish','lunch');
INSERT INTO meal_types(name,food_type) VALUES ('red radish','dinner');
INSERT INTO meal_types(name,food_type) VALUES ('shake smart','drink');
INSERT INTO meal_types(name,food_type) VALUES ('starbucks','drink');
INSERT INTO meal_types(name,food_type) VALUES ('health shack','lunch');
INSERT INTO meal_types(name,food_type) VALUES ('julians','drink');
INSERT INTO meal_types(name,food_type) VALUES ('mustang eats','lunch');
INSERT INTO meal_types(name,food_type) VALUES ('subway','lunch');
INSERT INTO meal_types(name,food_type) VALUES ('subway','dinner');
INSERT INTO meal_types(name,food_type) VALUES ('chick fil a','lunch');
INSERT INTO meal_types(name,food_type) VALUES ('chick fil a','dinner');
INSERT INTO meal_types(name,food_type) VALUES ('einstein','breakfast');
INSERT INTO meal_types(name,food_type) VALUES ('einstein','lunch');
INSERT INTO meal_types(name,food_type) VALUES ('einstein','dinner');

-- hours

CREATE TABLE hours(
   name  VARCHAR(20) NOT NULL PRIMARY KEY
  ,open  NUMERIC(4,1) NOT NULL
  ,close NUMERIC(4,1) NOT NULL
);
INSERT INTO hours(name,open,close) VALUES ('balance cafe',7.0,21.0);
INSERT INTO hours(name,open,close) VALUES ('brunch',7.0,21.0);
INSERT INTO hours(name,open,close) VALUES ('hearth',10.0,21.0);
INSERT INTO hours(name,open,close) VALUES ('jamba',6.5,21.0);
INSERT INTO hours(name,open,close) VALUES ('mingle and nosh',10.0,21.0);
INSERT INTO hours(name,open,close) VALUES ('noodles',10.0,21.0);
INSERT INTO hours(name,open,close) VALUES ('streats',10.0,21.0);
INSERT INTO hours(name,open,close) VALUES ('sweet bar',10.0,21.0);
INSERT INTO hours(name,open,close) VALUES ('vista grande express',7.0,21.0);
INSERT INTO hours(name,open,close) VALUES ('scout coffee',6.5,17.0);
INSERT INTO hours(name,open,close) VALUES ('mustang station',10.5,20.0);
INSERT INTO hours(name,open,close) VALUES ('red radish',10.5,20.0);
INSERT INTO hours(name,open,close) VALUES ('shake smart',7.0,22.0);
INSERT INTO hours(name,open,close) VALUES ('starbucks',6.5,20.0);
INSERT INTO hours(name,open,close) VALUES ('health shack',9.0,16.0);
INSERT INTO hours(name,open,close) VALUES ('julians',8.0,15.0);
INSERT INTO hours(name,open,close) VALUES ('mustang eats',11.0,14.0);
INSERT INTO hours(name,open,close) VALUES ('subway',0.0,0.0);
INSERT INTO hours(name,open,close) VALUES ('chick fil a',11.0,20.0);
INSERT INTO hours(name,open,close) VALUES ('einstein',7.0,17.5);
