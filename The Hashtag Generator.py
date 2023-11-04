def generate_hashtag(s):
    #your code here
    r = "#"+ "".join([word.capitalize() for word in s.split(" ") if word != ""]) if len(s.strip(" ")) != 0 else False  
    try:
        return r if len(r) < 140 else False
    except:
        return False

print(generate_hashtag("   "))