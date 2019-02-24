import json
import gkeepapi

def create(event, context):
    query = event.get('queryStringParameters', {})
    email = query.get('email')
    password = query.get('password')
    
    data = json.loads(event['body'])
    title = data.get('title')
    text = data.get('text')

    keep = gkeepapi.Keep()
    keep.login(email, password)
    keep.createNote(title, text)
    keep.sync()
    
    response = {
        "statusCode": 201
    }

    return response

def get(event, context):
    query = event.get('queryStringParameters', {})
    email = query.get('email')
    password = query.get('password')
    
    keep = gkeepapi.Keep()
    keep.login(email, password)
    notes = keep.all()
    simplifiedNotes = list(map(lambda x: { 'title': x.title, 'text': x.text }, notes))

    response = {
        "statusCode": 200,
        "body": json.dumps(simplifiedNotes)
    }

    return response