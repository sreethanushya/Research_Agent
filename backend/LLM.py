def portfolio(data):
    text=f"{data['company']} operates in the {data['industry']} industry with revenue of {data['revenue']} and employee strength of {data['employees']}.
    The company maintains strong market presence and competitive positioning. Company Summary:{data['summary']}"
    return text