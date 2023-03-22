def model_fill(model, data: dict = {}) -> None:
    
    for name, value in data.items():
        if(hasattr(model, name)):
            setattr(model, name, value)