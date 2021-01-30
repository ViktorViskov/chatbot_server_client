# 
# Calculator Bot
# 

# function take message (string), bot expressions and return message (string)
def say_bot(message:str) -> str:


    # 
    # Variables
    # 

    # math expression control (allowed symbols)
    allowed_symbols = ' ()/*-+0123456789'

    # message for math expression error
    error_message = 'Please elaborate.'

    # dict with bot expressions
    # question is key and value is answer
    bot_expressions = {
    'hello':'Hello World! This is my favorite phrase.',
    'what are you?':'A calculator.',
    'thank you :)':'Please elaborate.',
    }



    # 
    # Strint proccessing and check for bot expression
    # 

    # delete spaces and lower case
    message = message.strip().lower()

    # check answer in dict and catch errors
    try:
        answer = bot_expressions[message]



    # 
    # Check for math expression if key not exist
    # 

    except KeyError:

        # variable for control math expression
        is_math_expression = True

        # loop for checking allowed symbols
        for symbol in message:   
            if not (symbol in allowed_symbols):
                is_math_expression = False
                break

        # check for allowed symbols
        if is_math_expression:
            
            # catch errors
            try:
                # exec code
                answer = eval(message)
            
            # math expression is not correct  
            except SyntaxError:
                answer = error_message
            
            # division by 0
            except ZeroDivisionError:
                answer = error_message

        # if not put string
        else:
            answer = error_message

    # convert to str and return result 
    return str(answer)
    # return message