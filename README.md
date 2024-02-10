# HelloFresh-assessment

For the first part of the assessment, please run the `HelloFresh assessment.py` code.

The code is run in the jupyter notebook, using version Python 3.9.13. 

The third-party module used in the code is pandas.

The final result is saved in the file `result.csv`.

### Instructions and explanations of the code
Q1: I downloaded the json file from the [link](https://bnlf-tests.s3.eu-central-1.amazonaws.com/recipes.json) and named it as `recipes.json`.

Q2: The json file consist of multiple recipes. To find the similar word of "chilies", first define the search term and use `re.compile` function to find the similar words in the recipe. As the word "chilies" should appear in the ingredients field, so the pattern is searched in the strings of ingredients. 

Q3: The first step is to remove the character "PT" from both `cookTime` and `prepTime` columns. 
The second step is to 
