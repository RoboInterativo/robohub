import datetime
import jwt
import logging

def create_token(user,secret):

    payload={
    'username':user.get('user'),
    'id':user.get('id')}
    payload['exp']=datetime.datetime.now(tz=datetime.timezone.utc) + datetime.timedelta(seconds=600)

    encoded_jwt = jwt.encode(payload, secret, algorithm="HS256")
    #encoded_jwt=encoded_jwt.strip('(').strip(')').strip("'")

    logging.info("user",encoded_jwt,type(encoded_jwt))


    return encoded_jwt

async def validate(request):
    # res = request.app['conf']data
    # jstr = await request.read()
    # jstr=str(jstr,'UTF8')
    conf=request.app['config']
    token=request.cookies.get('token')
    if token:
        token=eval(token)[0]
    salt=conf['salt']
    salt=salt.decode('UTF8')
    if (not token):
        logging.info("no token validate  ")
        #exc=web.HTTPUnauthorized(body='not HTTPUnauthorized')
        #raise exc
        return {'auth':False}


    try:
        data=jwt.decode(token, key=salt, algorithms=['HS256', ])
        if data:
            #body=None, text=None, content_type=None

            logging.info("validate  ",data)
            return {'auth':True,'data':data}

        else:
            #exc = web.HTTPUnauthorized(location='/',body="{'auth':'no'})")
            logging.info("noValidate  ")
            return {'auth':False}

            #raise exc

    except Exception as err:
        #exc=web.HTTPUnauthorized(body=str(err))
        logging.info(token,type(token))
        logging.info(str(err))
        return {'auth':False,'err':str(err)}
