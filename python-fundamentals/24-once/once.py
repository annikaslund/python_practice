def once(fn):
    def invoke_once():
        invoked = False 
        while not invoked:
            invoke_once
            invoked = True
            
    return invoke_once