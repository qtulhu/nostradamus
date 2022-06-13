import vk
import SecretData
import math
import pandas as pd
import time
import requests
import json
import ast
import datetime
import dateutil.relativedelta
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)


start_time = time.time()

token = "vk1.a.piJJdmqvqrFBwsZobsP2OsGwV5tfOm26Y-l4D2aLFglZGIl2LamgHOECZJw0p7fzGPfhqEdNt6fws5X81PifbVJUM52CwYgqcySVE6M4C3yCU8RO5DTVrI1PjHuV2ggvwYLlp4OmXLkdD3b5LAQ3vRvM4k_pr9cCdgHRs_vFR_Cu4dS1BKsVwNOjKIxllRt2"
conector = vk.api.Session(access_token=token)
vkapi = vk.API(conector)
data = vkapi.groups.search(q='кооператив',v='5.131',offset=0,sort=6,count=1000)
# data  = vkapi.groups.getMembers(v='5.131',group_id=98384292,fields=['last_seen','bdate','sex'],count=500)

# print(members['count'])
# print(members['items'][0].keys())



def get_reques(code):
    url = "https://api.vk.com/method/execute?"
    params = dict(v=5.131,code=code, access_token=token)

    execute = requests.post(url=url, data=params)
    out = json.loads(execute.text)
    return out


def split_arr(arr, size):
     arrs = []
     while len(arr) > size:
         pice = arr[:size]
         arrs.append(pice)
         arr   = arr[size:]
     arrs.append(arr)
     return arrs

def listToStringReturn(s):
    out = ','.join(map(str, s))
    return out

def listToStringRequests(s):
    out = '\n'.join(map(str, s))
    return out


def get_members_from_gr(gr_id):
    members = vkapi.groups.getMembers(v='5.131',group_id=gr_id,fields=['last_seen','bdate','sex'],count=500)
    print('was ----- ',members['count'])
    if members['count'] < 700:
        return pd.DataFrame()
    pages = list(range(0, members['count'], 1000))
    count_code_blocks = math.ceil(len(pages)/25)

    ultimate = split_arr(pages, 25)
    func_code = ''
    return_code = ''

    for block in ultimate:
        for page in block:
            data = json.dumps({"group_id":gr_id,"offset":page,"fields":['last_seen','bdate','sex'],"count":1000})
            var = f"var a{page} = API.groups.getMembers({data});"
            func_code = func_code+var+'\n'
            return_code = return_code+ f"a{page},"

    blocks_api_requests = split_arr(func_code.split('\n'), 25)
    block_return = split_arr(return_code.split(',')[0:-1:], 25)


    out = []
    for item in range(count_code_blocks):
        return_vars = "["+listToStringReturn(block_return[item])+"]"
        exect_vars = listToStringRequests(blocks_api_requests[item])

        request_code = f"{exect_vars} \nreturn {return_vars};"

        data = get_reques(request_code)

        for response in data['response']:
            for item in response['items']:
                item['group_id'] = gr_id
                out.append(item)

    df = pd.DataFrame(out).dropna()

    data = df['last_seen'].to_dict()
    cp_counter = []
    for p in data.keys():
        date = datetime.datetime.fromtimestamp(data[p]['time'])
        cp_counter.append(date)

    df['date_last_seen'] = cp_counter

    # df.to_csv('data_hunter/big_data.scv')

    return df


def get_usr_g():
    all_users = pd.DataFrame()

    all_res = []
    for i in data['items']:
        try:
            id_group = i['id']
            time.sleep(0.35)
            members = get_members_from_gr(id_group)
            print('id_group for get users', id_group)
        except Exception as e:
            print(e)

        if members.empty:
            all_users = pd.concat(all_res,ignore_index=True)
            return all_users

        all_res.append(members)
    all_users = pd.concat(all_res)
    return all_users





#############################################
# data = get_members_from_gr(207593202)
# usr = get_usr_g()
# usr.to_csv('data_hunter/usr_data_g.scv')
#############################################


usr = pd.read_csv('data_hunter/usr_data_g.scv')
usr['date_last_seen']= pd.to_datetime(usr['date_last_seen'])


delta = datetime.datetime.now() - dateutil.relativedelta.relativedelta(months=1)
usr = usr[(usr['date_last_seen'] > delta)]
print(usr['group_id'].value_counts().nlargest(n=10))




# my_string = "05.02.2022"
# my_dt = datetime.datetime.strptime(my_string, '%d.%m.%Y')
# diff = datetime.datetime.now().date() - my_dt.date()
# print(diff)


# print("--- %s seconds ---" % (time.time() - start_time))
