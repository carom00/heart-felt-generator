# import config
import openai
import os

openai.api_key = "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"
    
def getResponse(value):
    tempValue = value
    value = value.replace('I\'m', 'you\'re')
    value = value.replace(' i ', ' you ')
    value = value.replace(' I ', ' you ')
    value = value.replace('I ', 'you ')
    value = value.replace('I\'ll', 'you\'ll')
    value = value.replace(' my ', ' your ')
    value = value.replace('My ', 'Your ')
    value = value.replace(' me ', ' you ')
    value = value.replace('I’m ', ' you’re ')
    value = value.replace('I am ', 'You are ')
    value = value.replace(' am ', ' are ')
    value = value.replace('I\'ve', 'You\'ve')
    value = value.replace('myself', 'yourself')

    myEntry = f"""Topic:{value}."""
    #Custom text input
    myPrompt = f"""Generates a poem on a given Topic. 
    Topic:I was such an asshole to her, I'll never forgive myself.
    We abuse our love
    Because we were taught
    By cities clawing at the neck of mother earth
    Passed on, we pass it on
    Remember this: none of it was your fault
    All is forgiven by those who can forgive\n
    Topic:I am just a worthless piece of garbage sometimes. I want so much more, but I just can't get even get out of bed or call people back. I've never done anything that keeps me from loving myself, I guess I've just never done anything that gives me a reason to.\n
    Hard to be anything, isn't it?
    To be that same thing every day
    To grow slowly, as slow as a tall tree
    Looking over and down and surprised
    Time has passed
    Time has yet to pass
    All is forgiven by those who can forgive
    Topic:fuk u nerd lol.
    All is forgiven by those who can forgive\n
    Topic:I don't really know, I just want a really cool NFT\n
    Some are here, some are not
    Some will be who haven't been
    It's quite alright
    All is forgiven by those who can forgive\n
    Topic:I'm afraid that people who know me as I usually am will discover I have another side, a better and finer side. I\u2019m afraid they\u2019ll mock me, think I\u2019m ridiculous and sentimental and not take me seriously. I\u2019m used to not being taken seriously, but only the \"lighthearted\" Anne is used to it and can put up with it; the \"deeper\" Anne is too weak. If I force the good Anne into the spotlight for even fifteen minutes, she shuts up like a clam the moment she\u2019s called upon to speak, and lets Anne number one do the talking. Before I realize it, she\u2019s disappeared.\n
    I replied to her with a short expression of encouragement which suggested that everything would be alright\n
    {myEntry}
    """

    #parameters
    myTokens = 60 # max length
    myEngine = "davinci"
    myTemp = 0.87 # creativity
    myTop_p = 1 
    myN=1
    myStream = None
    myLogProbs = None
    myStop = "\n\n"

    response = openai.Completion.create(
      engine=myEngine,
      prompt=myPrompt,
      max_tokens=myTokens,
      temperature=myTemp,
      top_p=myTop_p,
      n=myN,
      stream = myStream,
      logprobs=myLogProbs,
      stop = myStop
    )

    resp = response.choices[0].text + ''
    lines = resp.split('\n')
    res = ''
    for line in lines:
        line = line.strip()
        if (line.startswith('Topic:')):
            break
        else:
            res += line + '\n'
    res = res.strip()
    res = 'Topic: ' + tempValue.strip() + '\n' + res
    print(res)
    if (len(res) == 0 or res == value.strip()):
        getResponse(value)
        return
    with open('gpt3Poem.txt', 'a') as f:
        f.writelines("\n\n"+res)
    
    return res