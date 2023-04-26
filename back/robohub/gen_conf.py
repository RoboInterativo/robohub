import bcrypt
import yaml

hsalt=bcrypt.gensalt(10)
user_list=[u'admin',u'user']
user_list_db=[]
id=1
for item in user_list:
    id +=1
    hashp=bcrypt.hashpw( item.encode('UTF8'),hsalt)
    row={
        'id':id,
        'user':item,
        'hash':hashp,
        
        }
    user_list_db.append(row)

db={}
db['salt']=hsalt
db['user_list']=user_list_db
print (yaml.dump(db ) )
f=open('./conf.yml','w')
f.write(yaml.dump(db ))
f.close()
