from time import sleep
import sys
import numpy as np
import pandas as pd
OKGREEN = '\033[92m'
ENDC = '\033[0m'

#################################################
# helper functions
#################################################
def correct_assertion():
    print(f"\n{OKGREEN}All tests passed!!!"+ ENDC)

def loader():
    for i in range(10):
        sys.stdout.write("\r{0}>".format("="*i))
        sys.stdout.flush()
        sleep(0.1)

#################################################
# exercise tests
#################################################

def hint_create_dataframe():
    print("we can use the pd.DataFrame function")

def test_create_dataframe(f):
    loader()
    data = {'X':[78,85,96,80,86], 'Y':[84,94,89,83,86],'Z':[86,97,96,72,83]}
    df_test = pd.DataFrame(data)
    assert(df_test.equals(f(data)))
    correct_assertion()

def hint_remove_nan():
    print("We can use .isnull() method for a DataFrame to give the indices which have nan values.")

def hint_checkerboard_pattern():
    print("first we can initialize our board using board = np.zeros((y, x), dtype=int)")
    print("then we can use some smart index to assign 1 using:")
    print("board[1::2, ::2] = 1")
    print("board[::2, 1::2] = 1")

def test_remove_nan(f):
    loader()
    exam_data = {
      'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
      'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19]
      }
    df = pd.DataFrame(exam_data)
    df_test = df[~df.isnull().any(axis=1)]
    assert(df_test.equals(f(df)))
    correct_assertion()

def test_checkerboard_pattern(f):
    loader()
    x = 5
    y = 5
    result = np.zeros((y, x), dtype=int)
    result[1::2, ::2] = 1
    result[::2, 1::2] = 1
    assert(f(5, 5) == result)
    correct_assertion()

