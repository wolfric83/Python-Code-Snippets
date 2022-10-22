def converttypetomodel(key,value):
    """
    Determine Model Data Type for value.
    Return Datatype

    Parameters
    ----------
    key : str (?)
        Key in dictionary to be modelled
    value : 
        Value to be checked for type and returned as preferred (highest compatible) SQLAlchemy type
    Returns
    -------
    str
        predicted text of suitable SQLAlchemyType
    """
    if type(value).__name__ == 'str':
        if 'date' in key and  "-" in value:
            if ":" in value:
                return "DateTime"
            else:
                return "Date"
        if 'time' in key and  "-" in value:
            return "DateTime"
        return "Text"
    if type(value).__name__ == 'int':
        return "BigInteger"
    if type(value).__name__ == 'float':
        return "Numeric"
    if type(value).__name__ == 'date':
        return "DateTime"
    if type(value).__name__ == 'bool':
        return "Boolean"
    return "Text"
                  
def generateclassfromdict(objectbody, ClassName):
    """
    Generate Python Class String for SQLAlchemy model from a flat dictionary
    First key-value pair in dict presumed to be the Primary Key

    Parameters
    ----------
    objectbody : dict
        single dict object to be converted to database table model
    ClassName : str
        String to name resultant class
    Returns
    -------
    str
        Full python text of the generated class
    """
    newline = "\n"                                      
    pythonclass  = f"class {ClassName}(db.model):{newline}"     
    pythonclass += f'    """{newline}    {ClassName} - Generated Class{newline}    """{newline}'      
    pythonclass += f"    __tablename__ = '{ClassName}'{newline}"
    first = ", primary_key=True"
    reprreturn = ""
    reprformat = ""
    for key, value in objectbody.items():
        valuetype = converttypetomodel(key, value)
        pythonclass += f"    {key:44} = db.Column(db.{valuetype}{first}){newline}"
        first = ""  # cheaty hack to have first value as primary key
        reprreturn += f"{key}:, {{}}, "
        reprformat += f"self.{key}, "
    reprreturn = reprreturn.strip(', ')
    reprformat = reprformat.strip(', ')
    pythonclass += f"{newline}    def __repr__(self):{newline}"
    pythonclass += f"        return '{reprreturn}'.format({reprformat}){newline}"
    return pythonclass
