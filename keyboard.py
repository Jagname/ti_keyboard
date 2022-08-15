normal={'f(x)':73,'fenetre':72,'zoom':46,'trace':90,'graphe':68,'mode':69,'suppr':10,'UP':3,'RIGHT':1,'DOWN':4,'LEFT':2,'X,T,theta,n':180,'stats':49,'math':50,'matrice':55,'prgm':45,'var':53,'annul':9,'<>':64018,'trig':64017,'resol':64020,':/:':64458,'^':132,'xÂ²':189,',':139,'(':133,')':134,'/':131,'log':193,'7':149,'8':150,'9':151,'*':130,'ln':191,'4':146,'5':147,'6':148,'-':129,'sto':138,'1':143,'2':144,'3':145,'+':128,'on':0,'0':142,'.':141,'(-)':140,'entrer':5}
second={'f(x)':48,'fenetre':75,'zoom':87,'trace':59,'graphe':74,'mode':64,'suppr':11,'RIGHT':15,'LEFT':14,'X,T,theta,n':65,'stats':58,'math':51,'matrice':182,'prgm':47,'var':56,'<>':57,'trig':181,'resol':44,':/:':64016,'xÂ²':190,',':152,'(':236,')':237,'/':239,'log':194,'7':249,'8':250,'9':251,'*':135,'ln':192,'4':246,'5':247,'6':248,'-':136,'sto':12,'1':243,'2':244,'3':245,'+':54,'0':62,'.':238,'(-)':197,'entrer':13}
alpha={'math':154,'matrice':155,'prgm':156,'<>':157,'trig':158,'resol':159,':/:':160,'^':161,'xÂ²':162,',':163,'(':164,')':165,'/':166,'log':167,'7':168,'8':169,'9':170,'*':171,'ln':172,'4':173,'5':174,'6':175,'-':176,'sto':177,'1':178,'2':179,'3':204,'+':203,'0':153,'.':198,'(-)':202}
import ti_system
import time
def get_key(k):
 key=[i for i,val in normal.items()if val==k]
 if not key:
  key=[i for i,val in second.items()if val==k]
  if not key:
   key=[i for i,val in alpha.items()if val==k]
   if not key:
    raise ValueError("This key doesn't match!")
   return 'alpha '+str().join(key)
  return 'second '+str().join(key)
 return str().join(key)
def key_pressed():
 return get_key(ti_system.wait_key())
def check_type(keys):
 for i in range(len(keys)):
  if type(keys[i])is int:
   keys[i]=str(keys[i])
 return keys
def still_time(start_time,duration):
 if time.monotonic()<=(start_time+duration):
  return True
 return False
def is_pressed(k,duration=float('inf'),mode=normal):
 k=check_type(k)
 start_time=time.monotonic()
 if ti_system.wait_key()==mode[k]:
  if still_time(start_time,duration):
   return True
 return False
def combo(combo_keys,duration=float('inf'),kp=None):
 combo_keys=check_type(combo_keys)
 if kp==combo_keys[0]:
  combo_keys=combo_keys[1:]
 elif not kp:
  pass
 else:
  return False
 start_time=time.monotonic()
 for key in combo_keys:
  if key_pressed()==combo_keys[combo_keys.index(key)]:
   pass
  else:
   return False
 if still_time(start_time,duration):
  return True
 return False