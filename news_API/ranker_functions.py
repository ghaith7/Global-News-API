

#favorite_count
def top5liked(tweets):
    dic ={t:t.favorite_count for t in tweets}
    sorted_list=sorted(dic.items(), key=lambda item: item[1])
    return sorted_list[-5:]


#reply_count
#available only for premium accounts
def top5replied(tweets):
    dic ={t:t.reply_count for t in tweets}
    sorted_list=sorted(dic.items(), key=lambda item: item[1])
    return sorted_list[-5:]


#retweet_count
def top5retweeted(tweets):
    dic ={t:t.retweet_count for t in tweets}
    sorted_list=sorted(dic.items(), key=lambda item: item[1])
    return sorted_list[-5:]


#quote_count
def top5quoted(tweets):
    dic ={t:t.quote_count for t in tweets if t.is_quote_status==True}
    sorted_list=sorted(dic.items(), key=lambda item: item[1])
    return sorted_list[-5:]

def top5absolute(tweets):
    dic ={t: (t.favorite_count + t.retweet_count) for t in tweets }
    sorted_list=sorted(dic.items(), key=lambda item: item[1])
    return sorted_list[-5:]
    