# import requests
import grequests

limit_req = 550


def firstresponse():
    rs1 = (grequests.get('http://localhost:5000/work/asia/1') for u in range(1,2))
    rs2 = (grequests.get('http://localhost:5000/work/asia/0')for u in range(1,2))
    rs3 = (grequests.get('http://localhost:5000/work/emea/0')for u in range(1,2))
    rs4 = (grequests.get('http://localhost:5000/work/us/0')for u in range(1,2))
    rs5 = (grequests.get('http://localhost:5000/work/us/1')for u in range(1,2))

    all_backrs1 = grequests.map(rs1)
    all_backrs2 = grequests.map(rs2)
    all_backrs3 = grequests.map(rs3)
    all_backrs4 = grequests.map(rs4)
    all_backrs5 = grequests.map(rs5)

    aa = [all_backrs1, all_backrs2, all_backrs3, all_backrs4, all_backrs5]


    ok=0
    not_ok=0
    f1=True
    f2=True
    f3=True
    f4=True
    f5=True
    for r in all_backrs1:
        if  r:
            if f1:
                a=r.json()
                print(a)
                f1=False
            # print(a['region'])
            ok+=1
        else:
            not_ok+=1
    print("ASIA 1: ")
    # print("Ok: "+str(ok))
    print("Not: "+ str(not_ok))

    ok=0
    not_ok=0
    for r in all_backrs2:
        if  r:
            if f2:
                a=r.json()
                print(a)
                f2=False
            # print(a['region'])
            ok+=1
        else:
            not_ok+=1
    print("ASIA 0: ")
    # print("Ok: "+str(ok))
    print("Not: "+ str(not_ok))

    ok=0
    not_ok=0
    for r in all_backrs3:
        if  r:
            if f3:
                a=r.json()
                print(a)
                f3=False
            # print(a['region'])
            ok+=1
        else:
            not_ok+=1
    print("EMEA: ")
    # print("Ok: "+str(ok))
    print("Not: "+ str(not_ok))

    ok=0
    not_ok=0
    for r in all_backrs4:
        if  r:
            if f4:
                a=r.json()
                print(a)
                f4=False
            # print(a['region'])
            ok+=1
        else:
            not_ok+=1
    print("US 0: ")
    # # print("Ok: "+str(ok))
    print("Not: "+ str(not_ok))

    ok=0
    not_ok=0
    for r in all_backrs5:
        if  r:
            if f5:
                a=r.json()
                print(a)
                f5=False
            # print(a['region'])
            ok+=1
        else:
            not_ok+=1
    print("US 1: ")
    # print("Ok: "+str(ok))
    print("Not: "+ str(not_ok))

    return aa


def sendtoall(r1, r2, r3, r4, r5):
    rs1 = (grequests.get('http://localhost:5000/work/asia/1')
           for u in range(1, int(r1)))
    rs2 = (grequests.get('http://localhost:5000/work/asia/0')
           for u in range(1, int(r2)))
    rs3 = (grequests.get('http://localhost:5000/work/emea/0')
           for u in range(1, int(r3)))
    rs4 = (grequests.get('http://localhost:5000/work/us/0')
           for u in range(1, int(r4)))
    rs5 = (grequests.get('http://localhost:5000/work/us/1')
           for u in range(1, int(r5)))

    all_backrs1 = grequests.map(rs1)
    all_backrs2 = grequests.map(rs2)
    all_backrs3 = grequests.map(rs3)
    all_backrs4 = grequests.map(rs4)
    all_backrs5 = grequests.map(rs5)

    ok=0
    not_ok=0
    f1=True
    f2=True
    f3=True
    f4=True
    f5=True
    for r in all_backrs1:
        if  r:
            if f1:
                a=r.json()
                print(a)
                f1=False
            # print(a['region'])
            ok+=1
        else:
            not_ok+=1
    print("ASIA 1: ")
    # print("Ok: "+str(ok))
    print("Not: "+ str(not_ok))

    ok=0
    not_ok=0
    for r in all_backrs2:
        if  r:
            if f2:
                a=r.json()
                print(a)
                f2=False
            # print(a['region'])
            ok+=1
        else:
            not_ok+=1
    print("ASIA 0: ")
    # print("Ok: "+str(ok))
    print("Not: "+ str(not_ok))

    ok=0
    not_ok=0
    for r in all_backrs3:
        if  r:
            if f3:
                a=r.json()
                print(a)
                f3=False
            # print(a['region'])
            ok+=1
        else:
            not_ok+=1
    print("EMEA: ")
    # print("Ok: "+str(ok))
    print("Not: "+ str(not_ok))

    ok=0
    not_ok=0
    for r in all_backrs4:
        if  r:
            if f4:
                a=r.json()
                print(a)
                f4=False
            # print(a['region'])
            ok+=1
        else:
            not_ok+=1
    print("US 0: ")
    # # print("Ok: "+str(ok))
    print("Not: "+ str(not_ok))

    ok=0
    not_ok=0
    for r in all_backrs5:
        if  r:
            if f5:
                a=r.json()
                print(a)
                f5=False
            # print(a['region'])
            ok+=1
        else:
            not_ok+=1
    print("US 1: ")
    # print("Ok: "+str(ok))
    print("Not: "+ str(not_ok))


    pass


def sendtoregions(r1, r2, r3):
    rs1 = (grequests.get('http://localhost:5000/work/asia')
           for u in range(1, int(r1)))
    rs2 = (grequests.get('http://localhost:5000/work/emea')
           for u in range(1, int(r2)))
    rs3 = (grequests.get('http://localhost:5000/work/us')
           for u in range(1, int(r3)))
    all_backrs1 = grequests.map(rs1)
    all_backrs2 = grequests.map(rs2)
    all_backrs3 = grequests.map(rs3)

    ok=0
    not_ok=0
    f1=True
    f2=True
    f3=True
    for r in all_backrs1:
        if  r:
            if f1:
                a=r.json()
                print(a)
                f1=False
            # print(a['region'])
            ok+=1
        else:
            not_ok+=1
    print("ASIA 1: ")
    # print("Ok: "+str(ok))
    print("Not: "+ str(not_ok))

    ok=0
    not_ok=0
    for r in all_backrs2:
        if  r:
            if f2:
                a=r.json()
                print(a)
                f2=False
            # print(a['region'])
            ok+=1
        else:
            not_ok+=1
    print("ASIA 0: ")
    # print("Ok: "+str(ok))
    print("Not: "+ str(not_ok))

    ok=0
    not_ok=0
    for r in all_backrs3:
        if  r:
            if f3:
                a=r.json()
                print(a)
                f3=False
            # print(a['region'])
            ok+=1
        else:
            not_ok+=1
    print("EMEA: ")
    # print("Ok: "+str(ok))
    print("Not: "+ str(not_ok))

    


    pass


def sendtoallregions(nr):
    rs5 = (grequests.get('http://localhost:5000/work') for u in range(1, int(nr)))
    all_backrs1 = grequests.map(rs5)

    ok=0
    f3=True
    not_ok=0
    for r in all_backrs1:
        if  r:
            if f3:
                a=r.json()
                print(a)
                f3=False
            # print(a['region'])
            ok+=1
        else:
            not_ok+=1
    print("EMEA: ")
    # print("Ok: "+str(ok))
    print("Not: "+ str(not_ok))

    pass


def policy1(N):
    # trimit mod egal la toate pe seturi,
    chunk = 0
    left_N = N
    while left_N > 0:
        if left_N > limit_req*5:
            left_N -= limit_req*5
            sendtoall(limit_req, limit_req, limit_req, limit_req, limit_req)
        else:
            chunk = left_N/5
            rest = left_N-(chunk*5)
            # idk aici, unde sa trim rest?
            sendtoall(chunk+rest, chunk, chunk, chunk, chunk)
            left_N = 0
            break
    pass


def policy2(N):
    # verific dupa time response si trimit in limita catre acel server cu <
    # prioriyatatea va fi timeresponse

    first_resps = firstresponse()
    response_times = []
    # sortam  dupa time reponse
    # for r in first_resps:
    #     a=r[0].json()  #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    #     response_times.append(int(a['response_time']))
    # response_times.sort()
    
    left_N = N
    while left_N > 0:
        
        if len(response_times)==0:
            for r in first_resps:
                a=r[0].json()  #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
                response_times.append(int(a['response_time']))
            response_times.sort()

        curr_prio = response_times.pop(0)
        for r in first_resps:
            a=r[0].json()
            if a["response_time"] == curr_prio:
                if a['machine'] == "Machine 0":
                    machine_nr = '0'
                else:
                    machine_nr = '1'
                if left_N > limit_req:
                    rs = (grequests.get('http://localhost:5000/work/' +
                                    a['region']+'/'+machine_nr) for u in range(1, int(limit_req)))
                else:
                     rs = (grequests.get('http://localhost:5000/work/' +
                                a['region']+'/'+machine_nr) for u in range(1, int(left_N)))
                all_backrs1 = grequests.map(rs)

                ok=0
                not_ok=0
                f3=True
                for r in all_backrs1:
                    if  r:
                        if f3:
                            a=r.json()
                            print(a)
                            f3=False
                        # print(a['region'])
                        ok+=1
                    else:
                        not_ok+=1
                print(a['region'])
                # print("Ok: "+str(ok))
                print("Not: "+ str(not_ok))

                left_N -= limit_req
                break

    pass


def policy3(N):
    # impart pe bucati 550 si trimit random
    left_N = N

    while left_N > 0:

        if left_N > limit_req*5:
            left_N -= limit_req*5
            for i in range(0, 5):
                sendtoallregions(limit_req)
        elif left_N > limit_req:
            sendtoallregions(limit_req)
            left_N -= limit_req
        else:
            sendtoallregions(left_N)
            left_N = 0
            break

    pass


def policy4(N):
    # verific dupa worktime si fac prioritate

    first_resps = firstresponse()
    response_times = []
    # sortam  dupa time reponse
    # for r in first_resps:
    #     a=r[0].json()  #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    #     response_times.append(int(a['work_time']))
    # response_times.sort()
    
    left_N = N
    while left_N > 0:
        if len(response_times)==0:
            for r in first_resps:
                a=r[0].json()  #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
                response_times.append(int(a['work_time']))
            response_times.sort()
    
        curr_prio = response_times.pop(0)
       
        for r in first_resps:
            a=r[0].json()
            if a["work_time"] == curr_prio:
                if a['machine'] == "Machine 0":
                    machine_nr = '0'
                else:
                    machine_nr = '1'
                if left_N > limit_req:
                    rs = (grequests.get('http://localhost:5000/work/' +
                                    a['region']+'/'+machine_nr) for u in range(1, int(limit_req)))
                else:
                    rs = (grequests.get('http://localhost:5000/work/' +
                                a['region']+'/'+machine_nr) for u in range(1, int(left_N)))
        
                all_backrs1 = grequests.map(rs)

                ok=0
                not_ok=0
                f3=True
                for r in all_backrs1:
                    if  r:
                        if f3:
                            a=r.json()
                            print(a)
                            f3=False
                        # print(a['region'])
                        ok+=1
                    else:
                        not_ok+=1
                print(a['region'])
                # # print("Ok: "+str(ok))
                print("Not: "+ str(not_ok))

                left_N -= limit_req
                break

    pass


def policy5(N):
    # trimit tot pachetul la o regiune cea mai aprop
    # daca ramane < decat nr maz suportat trimit random in orice reg nefol
    # se trimite mereu secvetial, in bucati
    left_N = N
    while left_N > 0:
        if left_N >= 3000:
            sendtoregions(1000, 1000, 1000)
            left_N -= 3000
        elif left_N >= 2000:
            sendtoregions(1000, 0, 1000)
            left_N -= 2000
        elif left_N >= 1000:
            sendtoregions(1000, 0, 0)
            left_N -= 1000
        else:
            sendtoall(left_N, 0, 0,0,0)
            left_N = 0
            break

    pass


if __name__ == "__main__":
    N =600
    policy1(N)
   

# max de nr trimis random e 1000
    # rs1 = (grequests.get('http://localhost:5000/work/asia') for u in range(1,1000))
    # all_backrs1=grequests.map(rs1)

    # ok=0
    # not_ok=0
    # for r in all_backrs1:
    #     if  r:
    #         a=r.json()
    #         print(a)
    #         print(a['work_time'])
    #         ok+=1
    #     else:
    #         not_ok+=1
    # print("ASIA 1: ")
    # # print("Ok: "+str(ok))    
    # print("Not: "+ str(not_ok))

    # a={'machine': 'Machine 0', 'region': 'us', 'response_time': 8284, 'work_time': 21}
    # print(a['machine'])

    pass


# rs1 = (grequests.get('http://localhost:5000/work/asia/1') for u in range(1,1000))
# rs2 = (grequests.get('http://localhost:5000/work/asia/0') for u in range(1,1000))
# rs3 = (grequests.get('http://localhost:5000/work/emea/0') for u in range(1,1000))
# rs4 = (grequests.get('http://localhost:5000/work/us/0') for u in range(1,1000))
# rs5= (grequests.get('http://localhost:5000/work/us/1') for u in range(1,1000))

# all_backrs1=grequests.map(rs1)
# all_backrs2=grequests.map(rs2)
# all_backrs3=grequests.map(rs3)
# all_backrs4=grequests.map(rs4)
# all_backrs5=grequests.map(rs5)

# # asia 1
# ok=0
# not_ok=0
# for r in all_backrs1:
#     if ok==0 and r:
#         print(r.json())
#     if r:
#         # print("ok")
#         ok+=1
#     else:
#         not_ok+=1
# print("ASIA 1: ")
# print("Ok: "+str(ok))
# print("Not: "+ str(not_ok))
# # asia 2
# ok=0
# not_ok=0
# for r in all_backrs2:
#     if ok==0 and r:
#         print(r.json())
#     if r:
#         # print("ok")
#         ok+=1
#     else:
#         not_ok+=1
# print("ASIA 0: ")
# print("Ok: "+str(ok))
# print("Not: "+ str(not_ok))
# # emea 0
# ok=0
# not_ok=0
# for r in all_backrs3:
#     if ok==0 and r:
#         print(r.json())
#     if r:
#         # print("ok")
#         ok+=1
#     else:
#         not_ok+=1
# print("EMEA 0: ")
# print("Ok: "+str(ok))
# print("Not: "+ str(not_ok))
# # us 0
# ok=0
# not_ok=0
# i=all_backrs1[-1]
# for r in all_backrs4:
#     if ok==0 and r:
#         print(r.json())
#     if r:
#         # print("ok")
#         ok+=1
#     else:
#         not_ok+=1
# if i:
#     print(i.json())
# print("US 0: ")
# print("Ok: "+str(ok))
# print("Not: "+ str(not_ok))
# # us 1
# ok=0
# not_ok=0
# for r in all_backrs5:
#     if ok==0 and r:
#         print(r.json())
#     if r:
#         # print("ok")
#         ok+=1
#     else:
#         not_ok+=1
# print("US 1: ")
# print("Ok: "+str(ok))
# print("Not: "+ str(not_ok))

# rs = (grequests.get('http://localhost:5000/work/asia/1') for u in range(1,1000))
# rs1 = (grequests.get('http://localhost:5000/work/asia/1') for u in range(1,1000))
# all_backrs=grequests.map(rs)
# # print(all_backrs)
# # print("APOOOOOOOOOOI")
# alt_rasp=grequests.map(rs1)
# print(alt_rasp)

# ok=0
# not_ok=0
# for r in all_backrs:
#     if r:
#         # print("ok")
#         ok+=1
#     else:
#         not_ok+=1
# for r in alt_rasp:
#     if r:
#         # print("ok")
#         ok+=1
#     else:
#         not_ok+=1
# print("Ok: "+str(ok))
# print("Not: "+ str(not_ok))
    # if r.status_code!=200:
    #     print("Response no more")
# print(raspuns)
# for r in raspuns:
#     if r.status_code==200:
#         print("raspuns ok")
#     print(r)
