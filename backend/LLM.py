def portfolio(data):
    text=f"{data['company']} operates in the {data['industry']} industry with revenue of {data['revenue']} and employee strength of {data['employees']}. The company maintains strong market presence and competitive positioning."
    
    if data["summary"]!="Summary unavailable":
        text+=f" Company Summary:{data['summary']}"
    
    return text