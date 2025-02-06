import requests
import json
from classes.Company import Company
from classes.ReceitaWS_response import ReceitaWS_resp, ReceitaWS_errorResp

# NOTA: a API pública possui a limitação de 3 consultas por minuto... criar um message box informando em caso de erro
def consulta_cnpj(cnpj: str) -> ReceitaWS_resp | ReceitaWS_errorResp:
    url = f"https://receitaws.com.br/v1/cnpj/{cnpj}"

    querystring = {"token":"XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXX", "cnpj":"06990590000123", "plugin":"RF"}
    response = requests.get(url,params=querystring)

    result: ReceitaWS_resp | ReceitaWS_errorResp = None
    company: Company = None
    status = response.ok

    if response.ok:
        resp = json.loads(response.text)
        

        if "cnpj" in resp:
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

        result = ReceitaWS_resp(company=company, status_ok= status)

       
    else:
        result = ReceitaWS_errorResp(message= "Falha no server ou limite de consultas por minuto excedido.", status_ok=False)

    return result
