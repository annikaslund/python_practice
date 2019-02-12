def list_manipulation(li, cmd, loca, val=None):
    if cmd == 'remove': 
        if loca == 'end': 
            return li.pop()
        elif loca == 'beginning': 
            return li.pop(0)
    elif cmd == 'add': 
        if loca == 'beginning': 
            li.insert(0, val)
            return li 
        elif loca == 'end': 
            li.append(val)
            return li 
