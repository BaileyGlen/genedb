def removespecchar(test):
    """Function to Clean Up Strings.

    Specifically gets rid of quotes,tabs,new lines, and evens out the spaces."""
    import re
    if type(test) == str:
        test=re.sub('\t',' ',test)
        test=re.sub('\"',' ',test)
        test=re.sub('\n',' ',test)
        test=re.sub('\r',' ',test)
        test=re.sub(' +',' ',test)
    return(test)