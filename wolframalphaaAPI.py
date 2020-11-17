import wolframalpha

client = wolframalpha.Client('U8T7R3-RP9T968R42')
 
 
while True:
    query = str(input('Query: '))
    res = client.query(query)
    output = next(res.results).text
    print(output)