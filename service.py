import pandas as pd
import json
import datetime
import vk
import SecretData
import dateutil.relativedelta
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)


def main_service1(params):
    client_data = pd.read_csv('data_client.csv')

    sex = params.sex
    ages = [[2022-int(i.split('-')[0]),2022-int(i.split('-')[1])] for i in params.age]
    cash = [[int(k.split('-')[0]),int(k.split('-')[1])] for k in params.cash ]
    interest = params.interest

    sex_gen = {}
    all_sample = {}
    age_gen = {}
    favor_gen = {}

    filters = []
    filter_cash = []

    for i in ages:
        q = f"birth_date>{i[1]} & birth_date<{i[0]}"
        filters.append(q)

    for k in cash:
        q1 = f"current_credit_turn_sum>{i[1]} & current_credit_turn_sum<{i[0]}"
        filter_cash.append(q1)

    sex_gen['female'] = int(client_data[(client_data['gender']=='Ж')]['client_id'].count())
    sex_gen['male'] = int(client_data[(client_data['gender']=='М')]['client_id'].count())


    for f in list(range(0, len(filters))):
        age_gen[params.age[f]] = int(client_data.query(filters[f])['client_id'].count())


    for f1 in list(range(0, len(filter_cash))):
        all_sample[params.cash[f1]] = int(client_data.query(filter_cash[f1])['client_id'].count())


    response = {
        'sex':sex_gen,
        'age':age_gen,
        'cash':all_sample,
        'favor_gen':{}
    }

    return response



def metedata_groups(top_of_groups):
    token = SecretData.token
    conector = vk.api.Session(access_token=token)
    vkapi = vk.API(conector)
    # info_box = {}
    front = []
    for gr_ip in top_of_groups.index:
        data  = vkapi.groups.getById(v='5.131',group_id=gr_ip,fields=['links','members_count'],count=500)[0]

        members_count = data['members_count']
        group_name = data['name']
        photo = data['photo_100']
        coverage = int(members_count*0.27)

        front.append([members_count,group_name,coverage])
    return front

def get_data_from_vk(topic_value):
    print('--------------',topic_value)
    output_result = []
    topic = {
            "автолюбитель":["data_dumps/data_hunter/usr_data_autolovers.scv"],
            "кафе и доставки":["data_dumps/data_hunter/usr_data_restoran.scv"],
            "финансы и инвестиции":["data_dumps/data_hunter/usr_data_fin_gramotnost.scv"]
            }

    tag = topic[topic_value][0]
    usr = pd.read_csv(f'{tag}')
    ############################################

    # ########## фильтр неактивных пользователей ##################################
    usr['date_last_seen']= pd.to_datetime(usr['date_last_seen'])
    delta = datetime.datetime.now() - dateutil.relativedelta.relativedelta(months=1)
    usr = usr[(usr['date_last_seen'] > delta)]
    # ############################################


    ########### пользователи состоящие в более чем 3 и менее чем в 10 группах ###################################
    m = usr.groupby(['id'])['id'].transform('size')
    usr = usr.loc[m.between(3, 10)]
    ##############################################


    # ########## Топ 10 финал ########################
    top_of_groups = usr['group_id'].value_counts().nlargest(n=10)
    # ##################################

    print('-------------',tag,'-------------')
    front = metedata_groups(top_of_groups)
    print(front)

    return front

# print(get_data_from_vk("финансы и инвестиции"))
