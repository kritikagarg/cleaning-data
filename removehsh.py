#\B(\#[a-zA-Z]+\b)(?!;)

import re,string

def strip_links(text):
    link_regex    = re.compile('((https?):((//)|(\\\\))+([\w\d:#@%/;$()~_?\+-=\\\.&](#!)?)*)', re.DOTALL)
    links         = re.findall(link_regex, text)
    for link in links:
        text = text.replace(link[0], ', ')    
    return text

def strip_all_entities(text):
    entity_prefixes = ['#', '@']
    for separator in  string.punctuation:
        if separator not in entity_prefixes :
            text = text.replace(separator,' ')
    words = []
    for word in text.split():
        word = word.strip()
        if word:
            if word[0] not in entity_prefixes:
                words.append(word)
    return ' '.join(words)
    return text

with open ("2.txt", 'r') as f:
    b=f.read().split('\n')

tests = b
with open("ctweet.txt","w") as f2:
    for t in tests:
	tweet= strip_links(t)    #strip  url
        #tweet= strip_all_entities(strip_links(t))    #strips #hastags and @mentions 
	        
	f2.write("{}\n".format(tweet))
    

