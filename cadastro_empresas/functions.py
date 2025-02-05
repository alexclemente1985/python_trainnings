import requests
import json
from classes.Company import Company
from classes.ReceitaWS_response import ReceitaWS_resp, ReceitaWS_errorResp

# NOTA: a API pública possui a limitação de 3 consultas por minuto... criar um message box informando em caso de erro
def consulta_cnpj(cnpj: str) -> ReceitaWS_resp:
    url = f"https://receitaws.com.br/v1/cnpj/{cnpj}"

    querystring = {"token":"XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXX", "cnpj":"06990590000123", "plugin":"RF"}
    response = requests.request("GET", url, params=querystring)

    resp = json.loads(response.text)
    status = response.status_code

    print("##############")
    print('status code: ', status, type(status))
    company: Company = None
    print("#########$####")
    print("company: ", resp)

    result: ReceitaWS_resp | ReceitaWS_errorResp = None

    if status == 200 and "cnpj" in resp:
        company = Company(
        cnpj=resp["cnpj"],
        nome=resp["nome"],
        logradouro=resp["logradouro"],
        numero=resp["numero"],
        complemento=resp["complemento"],
        bairro=resp["bairro"],
        municipio=resp["municipio"],
        uf=resp["uf"],
        cep=resp["cep"],
        telefone=resp["telefone"],
        email=resp["email"]
        )

        result = ReceitaWS_resp(company=company, status= status)

    else:
        result = ReceitaWS_errorResp(status= status, message= resp["message"])

    print(result)
    return result

consulta_cnpj("44534483000189")