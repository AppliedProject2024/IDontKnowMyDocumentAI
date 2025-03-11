from Backend.UserAuth import api_request

def get_query(query_text):
    #send request with question to server
    response = api_request("/ask/query", "POST", {"query_text": query_text})
    #retrieve AI response
    return response['data']