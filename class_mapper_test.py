from sqlalchemy.orm import class_mapper
def model_to_dict(model):
    model_dict = {}
    #logging.info("model_to_dict"+str(model.__class__))
    for key, column in class_mapper(model.__class__).c.items():
        model_dict[column.name] = getattr(model, key, None)
    return model_dict



a = [ 'name','fengkaiwen','age',35]
print(model_to_dict(a))
