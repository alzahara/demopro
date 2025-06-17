def sentence_check(sentence):
    words=sentence.lower().split()
    result={}

    for word in words:
        if word not in result:
            result[word]={'length':len(word),'is_palindrome':word==word[::-1],'count':1}
        else:
            result[word]['count']+=1
    return result
sentence="madam and racecar are level racecar madam"
output=sentence_check(sentence)
print(output)