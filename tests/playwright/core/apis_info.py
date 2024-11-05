from enum import Enum

class ApiAbbreviation(Enum):
    TheCatApi = "TCA"
    Reqres = "RRS"
    
apiNames = {
    ApiAbbreviation.TheCatApi: "The Cat API",
    ApiAbbreviation.Reqres: "Reqres"
}

apiUrls = { 
    ApiAbbreviation.TheCatApi: "https://api.thecatapi.com/v1",
    ApiAbbreviation.Reqres: "https://reqres.in/api"
}

apiIds = {
    ApiAbbreviation.TheCatApi: "1",
    ApiAbbreviation.Reqres: "2"
}