# -*- utf-8 -*-
import requests
import json


def generateCode():
    url = "http://10.202.128.170:8080/api/v1/mobile/auth/otp"
    headers = {'content-type': 'application/json'}
    for i in range(count):
        current_mobile = mobile+i
        print(current_mobile)
        payload = {"mobile": str(current_mobile)}
        requests.post(url, data=json.dumps(payload), headers=headers)


def getToken():
    url = "http://10.202.128.170:8080/api/v1/mobile/auth"
    headers = {'content-type': 'application/json'}
    token_list = []
    for i in range(count):
        current_mobile = mobile + i
        print(current_mobile)
        payload = {"mobile": str(current_mobile), "otpCode": code[i]}
        r = requests.post(url, data=json.dumps(payload), headers=headers)
        token = r.json()["token"]
        token_list.append(token)
    tokens = ",\n".join(token_list)
    saveToken(tokens)


def saveToken(tokens):
    file = open("token_need_encrpt.csv", "w+")
    file.write(tokens)
    file.close()

if __name__ == "__main__":
    mobile = 15900500300
    count = 110
    code = ["378109",
            "668006",
            "582914",
            "962474",
            "875084",
            "384255",
            "784079",
            "345306",
            "214523",
            "893922",
            "696825",
            "968266",
            "767913",
            "764963",
            "815335",
            "269189",
            "857987",
            "704433",
            "766402",
            "940032",
            "266542",
            "196074",
            "503469",
            "311591",
            "576200",
            "438508",
            "185761",
            "402165",
            "751987",
            "554680",
            "176241",
            "988378",
            "372788",
            "588165",
            "357611",
            "397281",
            "302439",
            "494715",
            "302154",
            "729607",
            "907045",
            "312364",
            "570161",
            "675103",
            "621295",
            "940901",
            "746804",
            "511085",
            "440434",
            "301794",
            "880286",
            "393640",
            "191483",
            "777162",
            "539390",
            "970264",
            "562876",
            "171548",
            "809559",
            "178504",
            "887467",
            "975264",
            "408703",
            "201334",
            "334100",
            "456476",
            "734477",
            "724403",
            "392501",
            "986391",
            "426613",
            "718935",
            "511705",
            "883746",
            "794154",
            "993700",
            "353007",
            "467370",
            "578969",
            "452270",
            "491785",
            "363561",
            "229135",
            "561667",
            "615665",
            "743063",
            "620210",
            "377346",
            "108943",
            "340282",
            "860010",
            "854738",
            "415633",
            "924017",
            "347906",
            "711243",
            "107408",
            "554552",
            "959070",
            "968431",
            "214690",
            "160790",
            "602859",
            "823451",
            "247975",
            "648726",
            "377399",
            "412903",
            "567825",
            "696769"]
    # generateCode()
    getToken()

