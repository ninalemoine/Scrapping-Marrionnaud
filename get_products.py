import requests
import json
import time 

# URL de base
base_url = 'https://api.marionnaud.fr/api/v2/mfr/search?fields=PLP%2Cproducts(couponCodeValue%2CisAgec)&categoryCode=P0100&lang=fr_FR&curr=EUR'

cookies = {
    '_pcid': '%7B%22browserId%22%3A%22m2m0mp3h5uy3jhrr%22%2C%22_t%22%3A%22miahpc7m%7Cm2m0mp3m%22%7D',
    '_pctx': '%7Bu%7DN4IgrgzgpgThIC4B2YA2qA05owMoBcBDfSREQpAeyRCwgEt8oBJAE0RXSwH18yBbeoQAWABwDGAdiQAffgCZ%2BABn6iAzDQC%2BQA',
    'OptanonAlertBoxClosed': '2024-10-23T15:14:50.215Z',
    '__pr.bdjbl0': 'rD5tVLtOzH',
    '_abck': '964A43D8BD16992277FC0369847323F9~0~YAAQoeJIF1Cg9wmTAQAA1uFgIAyVRxV9HMLe3AFSLwS6TbrxOzo/PJ4sz0F4j0u/yuFXO6LugbWTyin5tDU/SYQ5RdJRTQkhJ6n7GtDjS8sWBvVYHaA6lJk9eOaYgBaoLtXFp+1xE7nBw1pgwYQ2Wu7IG1/UV4i7POPllsuCXQ5Qw1MRXRdgP71tiGNk1HD1gigxFR/IIv5kKNklo08Yfmlvbjri57DLOJntXPoVMMVAgjf+g9Po8azOEdvTKIJR6QxGoIsoQIIZ0KYC9GClPpna9P34iFDEiDbqiHXAlwoW8cLdgaD1bXfz1VLBxInr0Z6i3VVS1FaRaO2hg64tBUU31O9HM9UEFw1CtGfuIlRyk76dfNslfRpa0aZ+qeF/vhz45bCDtp+fimNkyW2DxuXcnDlavYkTcnvaAbRWeo8+9xL8Ug0ayumCGVKVdUiB5VQ9pjFqI2qJecZZgbgNkwOm9pwSym67h3s9u0JGx0a4gMI=~-1~-1~-1',
    'PIM-SESSION-ID': 'd3hZ6hxd6n7Mlj2i',
    'ak_bmsc': 'DF9FA54179FA00EF0D6C3D33F79599FF~000000000000000000000000000000~YAAQoeJIF4Kg9wmTAQAAauVgIBmpHoBnkWs5zimKkggcX63NEplYg6HJPKod7nBLH2gbCYBit+0eJWKXtHczBbjGsrl2cQ1/GOnYog55+ltPI8LyZCUL4OYNL9VMtGYzuRSUMBZrbYrb6m4zC6W9HbTsug6UFWBcFGuHz1jKaz+YjCblzMu+ADEDbo5NIFqqDmpHzUobzS05SP7u7rD38LadkroRdNCqrLXo+0rTGi17Z0TTyCVUnov955IJ0eF9tTTKAWzNnXuQtUwjHxIu7mTrHOYaoUsTo1Ud+w9qjJXVMouVUAU4YaoDAI0sNC/JCC9ab0rfQjq/FRH0m9iPljtV1bT3xsdhiyvfWzqHVDPHQSkD0HiySbwHSm3IVK4aPzyudViYzzvsZFVHiKbNdblBuNs5G4AmPK1hnGOxoKeJSHvkiBG5S0JISVGhdjwARxbIfTI1qrjEdEko23Yk4aU=',
    'ROUTE': '.accstorefront-69774dc757-h9sgt',
    'QueueITAccepted-SDFrts345E-V3_marionnaud': 'EventId%3Dmarionnaud%26QueueId%3D893d27ab-921f-4a92-b7a8-4d5e4336ac39%26RedirectType%3Dsafetynet%26IssueTime%3D1731415045%26Hash%3D6ed2119127b5ef673423501a48dacc1e0aa79f88b5e7b8810db26b238d46c874',
    '_pprv': 'eyJjb25zZW50Ijp7IjAiOnsibW9kZSI6ImVzc2VudGlhbCJ9LCI3Ijp7Im1vZGUiOiJvcHQtaW4ifX0sInB1cnBvc2VzIjp7IjAiOiJBTSIsIjciOiJETCJ9LCJfdCI6Im1pYWhwYzdrfG0ybTBtcDNrIn0%3D',
    'OptanonConsent': 'isGpcEnabled=0&datestamp=Tue+Nov+12+2024+14%3A06%3A04+GMT%2B0100+(Central+European+Standard+Time)&version=202410.1.0&browserGpcFlag=0&isIABGlobal=false&hosts=&consentId=d4b00950-159f-47e8-9d38-40557279b67f&interactionCount=1&isAnonUser=1&landingPath=NotLandingPage&groups=C0001%3A1%2CC0003%3A0%2CC0009%3A0&intType=2&geolocation=FR%3BIDF&AwaitingReconsent=false',
    'gaManual_originalLocation': 'https://www.marionnaud.fr/parfum/parfum-femme/c/P0100?currentPage=1',
    'bm_sv': '1E075CA4499DBEEE38BC7880DED0E14F~YAAQoeJIF1rH+AmTAQAAUn97IBlH1bNMc4ueLN8HEKGyG/zAzWUWSTwF9/+k18k+CqiK0i6pThkaB/uY+nX5oKJuu4B+V5IWD5jRj3sf0Rl2Cu3uG7uBzqxebfEhZj23pYmM9vb56LgyTK9tK2fS3zL+GIPuZdya2IN+BjIa5ep4EruRJFrthr37mFuFAXyh2klrd9XCIZ3wArB61dyabAxCGLTSNgFUMX58xpCoisPjPPOYbXnUsd9+k8qZrDsTH4Nu+w==~1',
    'bm_sz': '4095F8427EBA8F8D348F9D18E6EA810C~YAAQoeJIF1vH+AmTAQAAUn97IBm7kk9Y0c/rtEUwi2C5oKJpJ9lBlb9eybtrLrHOme3E4LQdy8ICXaXEiGELT8lD0GCvmRopM6lYoLm6zPOw5rfsAtK+wJgMTC3nliBYdBOzJnMy1epeurNUt3LoOvTJ7VMd+4DnkvrIS0goewc16f6ulBtSMWlVQlzpt+DlV/3vMUPGVmr4LytqdDSrKhVdTM3z38X/G6WdHOh8h9S+K4NzvVzaAjHUEbmi0JNHXkMDqvWdCUThPHjqO2AuJJJZUvzBMGCjii0uDKZFavz6Hu4hlgWrETrRiDFxS9dEGyaNq3jBZVhQ/BcHcqbn5i5SMy13D6KNAgPWdbZ8JZi3l3e8NVxkNu9jle1q8EJYIrY0USnc1C6D10ZcrdZKCjLJUaAnWRfYV6Ygz6ow/s0a/FgRkRMq8SqBSxRidg==~3289411~3753028',
}

headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.7',
    # 'cookie': '_pcid=%7B%22browserId%22%3A%22m2m0mp3h5uy3jhrr%22%2C%22_t%22%3A%22miahpc7m%7Cm2m0mp3m%22%7D; _pctx=%7Bu%7DN4IgrgzgpgThIC4B2YA2qA05owMoBcBDfSREQpAeyRCwgEt8oBJAE0RXSwH18yBbeoQAWABwDGAdiQAffgCZ%2BABn6iAzDQC%2BQA; OptanonAlertBoxClosed=2024-10-23T15:14:50.215Z; __pr.bdjbl0=rD5tVLtOzH; _abck=964A43D8BD16992277FC0369847323F9~0~YAAQoeJIF1Cg9wmTAQAA1uFgIAyVRxV9HMLe3AFSLwS6TbrxOzo/PJ4sz0F4j0u/yuFXO6LugbWTyin5tDU/SYQ5RdJRTQkhJ6n7GtDjS8sWBvVYHaA6lJk9eOaYgBaoLtXFp+1xE7nBw1pgwYQ2Wu7IG1/UV4i7POPllsuCXQ5Qw1MRXRdgP71tiGNk1HD1gigxFR/IIv5kKNklo08Yfmlvbjri57DLOJntXPoVMMVAgjf+g9Po8azOEdvTKIJR6QxGoIsoQIIZ0KYC9GClPpna9P34iFDEiDbqiHXAlwoW8cLdgaD1bXfz1VLBxInr0Z6i3VVS1FaRaO2hg64tBUU31O9HM9UEFw1CtGfuIlRyk76dfNslfRpa0aZ+qeF/vhz45bCDtp+fimNkyW2DxuXcnDlavYkTcnvaAbRWeo8+9xL8Ug0ayumCGVKVdUiB5VQ9pjFqI2qJecZZgbgNkwOm9pwSym67h3s9u0JGx0a4gMI=~-1~-1~-1; PIM-SESSION-ID=d3hZ6hxd6n7Mlj2i; ak_bmsc=DF9FA54179FA00EF0D6C3D33F79599FF~000000000000000000000000000000~YAAQoeJIF4Kg9wmTAQAAauVgIBmpHoBnkWs5zimKkggcX63NEplYg6HJPKod7nBLH2gbCYBit+0eJWKXtHczBbjGsrl2cQ1/GOnYog55+ltPI8LyZCUL4OYNL9VMtGYzuRSUMBZrbYrb6m4zC6W9HbTsug6UFWBcFGuHz1jKaz+YjCblzMu+ADEDbo5NIFqqDmpHzUobzS05SP7u7rD38LadkroRdNCqrLXo+0rTGi17Z0TTyCVUnov955IJ0eF9tTTKAWzNnXuQtUwjHxIu7mTrHOYaoUsTo1Ud+w9qjJXVMouVUAU4YaoDAI0sNC/JCC9ab0rfQjq/FRH0m9iPljtV1bT3xsdhiyvfWzqHVDPHQSkD0HiySbwHSm3IVK4aPzyudViYzzvsZFVHiKbNdblBuNs5G4AmPK1hnGOxoKeJSHvkiBG5S0JISVGhdjwARxbIfTI1qrjEdEko23Yk4aU=; ROUTE=.accstorefront-69774dc757-h9sgt; QueueITAccepted-SDFrts345E-V3_marionnaud=EventId%3Dmarionnaud%26QueueId%3D893d27ab-921f-4a92-b7a8-4d5e4336ac39%26RedirectType%3Dsafetynet%26IssueTime%3D1731415045%26Hash%3D6ed2119127b5ef673423501a48dacc1e0aa79f88b5e7b8810db26b238d46c874; _pprv=eyJjb25zZW50Ijp7IjAiOnsibW9kZSI6ImVzc2VudGlhbCJ9LCI3Ijp7Im1vZGUiOiJvcHQtaW4ifX0sInB1cnBvc2VzIjp7IjAiOiJBTSIsIjciOiJETCJ9LCJfdCI6Im1pYWhwYzdrfG0ybTBtcDNrIn0%3D; OptanonConsent=isGpcEnabled=0&datestamp=Tue+Nov+12+2024+14%3A06%3A04+GMT%2B0100+(Central+European+Standard+Time)&version=202410.1.0&browserGpcFlag=0&isIABGlobal=false&hosts=&consentId=d4b00950-159f-47e8-9d38-40557279b67f&interactionCount=1&isAnonUser=1&landingPath=NotLandingPage&groups=C0001%3A1%2CC0003%3A0%2CC0009%3A0&intType=2&geolocation=FR%3BIDF&AwaitingReconsent=false; gaManual_originalLocation=https://www.marionnaud.fr/parfum/parfum-femme/c/P0100?currentPage=1; bm_sv=1E075CA4499DBEEE38BC7880DED0E14F~YAAQoeJIF1rH+AmTAQAAUn97IBlH1bNMc4ueLN8HEKGyG/zAzWUWSTwF9/+k18k+CqiK0i6pThkaB/uY+nX5oKJuu4B+V5IWD5jRj3sf0Rl2Cu3uG7uBzqxebfEhZj23pYmM9vb56LgyTK9tK2fS3zL+GIPuZdya2IN+BjIa5ep4EruRJFrthr37mFuFAXyh2klrd9XCIZ3wArB61dyabAxCGLTSNgFUMX58xpCoisPjPPOYbXnUsd9+k8qZrDsTH4Nu+w==~1; bm_sz=4095F8427EBA8F8D348F9D18E6EA810C~YAAQoeJIF1vH+AmTAQAAUn97IBm7kk9Y0c/rtEUwi2C5oKJpJ9lBlb9eybtrLrHOme3E4LQdy8ICXaXEiGELT8lD0GCvmRopM6lYoLm6zPOw5rfsAtK+wJgMTC3nliBYdBOzJnMy1epeurNUt3LoOvTJ7VMd+4DnkvrIS0goewc16f6ulBtSMWlVQlzpt+DlV/3vMUPGVmr4LytqdDSrKhVdTM3z38X/G6WdHOh8h9S+K4NzvVzaAjHUEbmi0JNHXkMDqvWdCUThPHjqO2AuJJJZUvzBMGCjii0uDKZFavz6Hu4hlgWrETrRiDFxS9dEGyaNq3jBZVhQ/BcHcqbn5i5SMy13D6KNAgPWdbZ8JZi3l3e8NVxkNu9jle1q8EJYIrY0USnc1C6D10ZcrdZKCjLJUaAnWRfYV6Ygz6ow/s0a/FgRkRMq8SqBSxRidg==~3289411~3753028',
    'occ-personalization-id': 'c57ec2f2-fb00-4770-b4f4-867e46810014',
    'occ-personalization-time': '1731416759131',
    'origin': 'https://www.marionnaud.fr',
    'priority': 'u=1, i',
    'referer': 'https://www.marionnaud.fr/',
    'sec-ch-ua': '"Chromium";v="130", "Google Chrome";v="130", "Not?A_Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36',
    'x-anonymous-consents': '%5B%5D',
}


# Liste pour stocker tous les résultats
tous_les_resultats = []

# Boucle sur les pages jusqu'à ce qu'il n'y ait plus de données
page = 1
while True:
    # Construire l'URL avec le numéro de page actuel
    url = f"{base_url}&currentPage={page}"
    response = requests.get(url, cookies=cookies, headers=headers)

    # Vérifier le code de réponse
    if response.status_code != 200:
        print(f"Erreur lors de la récupération de la page {page}. Code de statut:", response.status_code)
        break

    # Charger la réponse en JSON
    response_json = response.json()

    # Vérifier s'il y a des produits dans la réponse
    if not response_json.get("products"):
        print(f"Aucune donnée trouvée à la page {page}. Fin de la récupération.")
        break

    # Ajouter les produits de la page actuelle à la liste des résultats
    tous_les_resultats.extend(response_json["products"])

    print(f"Données de la page {page} récupérées avec succès.")

    # Incrémenter la page et attendre un délai avant la prochaine requête
    page += 1
    time.sleep(5)

# Affichage de tous les résultats
print("Nombre total de produits récupérés :", len(tous_les_resultats))

with open('resultats.json', 'w', encoding='utf-8') as f:
    json.dump(tous_les_resultats, f, ensure_ascii=False, indent=4)

print("Les résultats ont été enregistrés dans 'resultats.json'.")



