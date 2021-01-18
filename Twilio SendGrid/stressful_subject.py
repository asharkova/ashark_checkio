#!/usr/bin/env checkio --domain=py run stressful-subject

# 
# END_DESC

def is_stressful(subj):
    """
        recognize stressful subject
    """
    red_words = ["help", "asap", "urgent"]
    if "!!!" in subj: return True
    subj = ''.join(char for char in subj.lower() if char.isalnum())
    subj.replace('.','', subj.count('.'))
    for word in red_words:
        if word in subj:
            return True
            
    return False

if __name__ == '__main__':
    #These "asserts" are only for self-checking and not necessarily for auto-testing
    assert is_stressful("Hi") == False, "First"
    assert is_stressful("I neeed HELP") == True, "Second"
    assert is_stressful("We need you A.S.A.P.!!") == True
    print('Done! Go Check it!')