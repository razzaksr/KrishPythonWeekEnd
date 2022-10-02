# dictionary : {"key":value}

hi={
    "2012":"VTV",
    "2021":2.0,
    "2020":True,
}

print(hi)

say={
    "appName":"flipkart",
    "appCategory":"E-Commerce",
    "appDownloads":10000000,
    "appRating":4.1,
    "isAppVoiceSearch":True,
    "appRecentDeals":['Big billion days','diwali festival sale'],
    "appSaleSponsers":{
        "bb":"noise",
        "diwali":"boat",
        "2021bb":"realme"
    }
}

print(say)

print(say['appCategory'])
print(say['appDownloads'])
print(say['appRating'])


print("Using loop")
for x in say:
    print(x,say[x])
    
print("using for with items functions")
for x,y in say.items():
    print(x,y)

print("only keys")
for x in say.keys():
    print(x)
    
print("only values")
for x in say.values():
    print(x)
    
# adding
say['appModes']=['website','app']

print(say)

#update
say['appRating']=3.8
print(say)

# deletion
del say['appDownloads']
print(say)

# deletion using pop
say.pop('appSaleSponsers')
print(say)

# delete last pair by default
say.popitem()
print(say)