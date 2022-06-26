# https://github.com/blakeembrey/code-problems/tree/master/problems/balanced-brackets

bracket_pairs = {
    "[":"]",
    "(": ")",
    "{": "}"
}

def is_opening(bracket):
    return bracket in bracket_pairs

def is_pair(bracket1, bracket2):
    return bracket_pairs[bracket1] == bracket2

def is_ballanced(bracket_string):
    arr_1 = []
    for i in range(len(bracket_string)):
        current_bracket = bracket_string[i]
        previous_bracket = '' if not arr_1 else arr_1[len(arr_1) - 1]
        if(is_opening(current_bracket)):
            arr_1.append(current_bracket)
        elif previous_bracket != '' and is_pair(previous_bracket, current_bracket):
            arr_1.pop()
        else:
            return False
            
    return not arr_1 

def test_is_ballanced():
    assert is_ballanced('()[]{}(([])){[()][]}') == True
    assert is_ballanced('())[]{}') == False
    assert is_ballanced('}()[]{}') == False