def text_deciphered(text_message,abbrevs):
    """
    Function to decipher the text using given dictionary
    Parameters:
        text_message : text message to decipher
        abbrevs : dictionary
    Returns:
        returns a string of deciphered text
    """
    # spliting the text_message to words based on spaces
    
    words = text_message.split(" ")
    
    # iterating through the words using indices 
    for i in range(len(words)):
        # getting key and values from the abbrevs using items method
        for k,v in abbrevs.items():
            # if words[i] matches with the value
            if words[i] == v:
                # then replace the value by key as key it the original deciphered value
                words[i] = k
    
    # finally using join method to convert words to string again and returning it
    return " ".join(words) 

text_message = "Hey, wat r our plans for tn"
abbrevs = {"what": "wat", "are": "r", "tonight": "tn"}
print(text_deciphered(text_message, abbrevs))