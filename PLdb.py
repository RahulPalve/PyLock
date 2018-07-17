def db_w(nac , npwd):
    try:
        db = open('pl.db','a+')
        n = nac + ':' + npwd + '\n'
        db.write(n)
    except IOError:
        print('unable to process pl.db')
    finally:
        db.close()
    return '\nNew Account successfully added to the DATABASE'

def db_r(ac):
    db=open('pl.db','r')
    ex=0
    for line in db:
        try:
            idn=line.index(':')
            if line[:idn]==ac:
                return (line[idn+1:])
                break
        except:
            print("Pwd separator not found")
        
        
    

