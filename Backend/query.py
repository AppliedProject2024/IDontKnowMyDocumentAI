from Backend.UserAuth import api_request

def get_query(query_text):
    #send request with question to server
    response = api_request("/ask/query", "POST", {"query_text": query_text})
    #retrieve AI response
    return response["data"].get("response", ""), response["data"].get("context", "")

def get_summary(query_text, word_num, complexity):
    #send request with question to server
    response = api_request("/ask/summary", "POST", {"query_text": query_text, "word_num": word_num, "complexity": complexity})
    #retrieve AI response
    return response["data"].get("response", ""), response["data"].get("context", "")

def get_mcq(query_text):
    #send request with question to server
    response = api_request("/ask/mcq", "POST", {"query_text": query_text})
    #retrieve AI response
    return response["data"].get("response", ""), response["data"].get("context", "")
