import json
import warnings
import sys


def eval_function(target_dict, test_dict):
    '''
    This function calculates accuracy based on the participant's answer and true values.
    Pay attention, that if for one key several values are given in participant's suggestion, then accuracy equals 0.


    Parameters
    ----------
    target_dict: dictionary with true values
    test_dict: dictionary with participant's answer

    Returns
    -------
    float
        accuracy score

    '''
    correct_matches_count = 0

    if len(target_dict) > len(test_dict):
        warnings.warn("Not all contexts are mapped with sketches.")


    elif len(target_dict) < len(test_dict):
        warnings.warn("There are additional contexts given, which are not presented in the test data")

    for target_key in target_dict:
        if (target_key in test_dict) and (type(test_dict[
                                                   target_key]) != str):  # Checks if participant tried to match one context with several sketches
            raise Exception('More then one sketch found for one context.')

        if (target_key in test_dict) and (target_dict[target_key] == test_dict[target_key]):
            correct_matches_count += 1

    accuracy = correct_matches_count / len(target_dict)
    return accuracy

if __name__ == '__main__':

    with open(sys.argv[1], 'r') as myfile:
        if len(myfile.readlines()) != 0:
            myfile.seek(0)
            trial = json.load(myfile)

    with open(sys.argv[2], 'r') as myfile:
        if len(myfile.readlines()) != 0:
            myfile.seek(0)
            test = json.load(myfile)

    accuracy = eval_function(trial, test)
    print ('Your accuracy score is', accuracy)


