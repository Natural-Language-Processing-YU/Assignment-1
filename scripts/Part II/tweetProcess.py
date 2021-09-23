#!/usr/bin/env python
# coding: utf-8

# In[9]:


def getTweets(query,result_type, count, lang = 'en'):
    """
    input: 
        query: a string to pass 
        result_type: popular or recent are the only options
        count: the number of tweets to return, max is 100
        lang: default is english or 'en'
    output: 
        Tweets
    
    """
    import requests
    import json
    import base64
    client_key = 'WT2ZgK9mYqOYWFuvYxwrwSBBA'
    client_secret = 'zcwTn9PjAx49Y32FULq8J4RaVxki6ROrM2vOuwukVRtU7lzwZH'
    #you will need to import this into your lib path to implement the following code

    get_ipython().run_line_magic('config', 'IPCompleter.greedy=True')
    key_secret = '{}:{}'.format(client_key, client_secret).encode('ascii')
    b64_encoded_key = base64.b64encode(key_secret)
    b64_encoded_key = b64_encoded_key.decode('ascii')

    #identify base url and oauth token path
    base_url = 'https://api.twitter.com/' #base url for authentication
    auth_url = '{}oauth2/token'.format(base_url)

    #share header information -- encoding is ascii
    auth_headers = {
        'Authorization': 'Basic {}'.format(b64_encoded_key),
        'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8'
    }

    #pass clientcredentials
    auth_data = {
        'grant_type': 'client_credentials'
    }

    #send authentication using requests - POST request
    auth_resp = requests.post(auth_url, headers=auth_headers, data=auth_data)

    #check response status. 200 = OK
    #print("Response Code: ", auth_resp.status_code)

    #Keys in data response are token_type (bearer) and access_token (your access token)
    access_token = auth_resp.json()['access_token']

    search_headers = {
        'Authorization': 'Bearer {}'.format(access_token)    
    }

    #enter search parameters
    query_params = {
        'q': query, #inputs the query parameter to filter tweets. 
        'result_type': result_type, #filters by most popular tweets
        'count': count, #provides the top 15 results, defaults to 15
        'lang': 'en' #filters by english language only
    }

    #identify search url path and save 
    search_url = '{}1.1/search/tweets.json'.format(base_url)
    #run search using get request
    search_resp = requests.get(search_url, headers=search_headers, params=query_params)

    #send request and print results 
    #print( count, "tweets returned: ")
    twitter_data = search_resp.json()
    for x in twitter_data['statuses']:
        print(x['text'] + '\n')


# In[ ]:


def preprocess_tweet(tweet):
    """Process tweet function.
    Input:
        tweet: a string containing a tweet
    Output:
        tweets_clean: a list of words containing the processed tweet

    """
    stemmer = PorterStemmer()
    stopwords_english = stopwords.words('english')
    # remove stock market tickers like $GE
    tweet = re.sub(r'\$\w*', '', tweet)
    # remove old style retweet text "RT"
    tweet = re.sub(r'^RT[\s]+', '', tweet)
    # remove hyperlinks
    tweet = re.sub(r'https?:\/\/.*[\r\n]*', '', tweet)
    # remove hashtags
    # only removing the hash # sign from the word
    tweet = re.sub(r'#', '', tweet)
    # tokenize tweets
    tokenizer = TweetTokenizer(preserve_case=False, strip_handles=True,
                               reduce_len=True)
    tweet_tokens = tokenizer.tokenize(tweet)

    tweets_clean = []
    for word in tweet_tokens:
        if (word not in stopwords_english and  # remove stopwords
                word not in string.punctuation):  # remove punctuation
            # tweets_clean.append(word)
            stem_word = stemmer.stem(word)  # stemming word
            tweets_clean.append(stem_word)
            
    return tweets_clean

