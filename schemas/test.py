from jsonschema import validate, RefResolver
import json
import os

# https://github.com/Julian/jsonschema/issues/313#issuecomment-269361225
sName = 'observation.schema.json'
# sName = '../totality.schema.json'
sHandle = open(sName)
s = json.loads(sHandle.read())
schemaAbs = 'file://' + os.path.abspath(sName)

class fixResolver(RefResolver):
    def __init__( self ):
        RefResolver.__init__( self,
            base_uri = schemaAbs, 
            referrer = None )
        self.store[ schemaAbs ] = s

newResolver = fixResolver()

j = {
    "observer": {
        "email": "beau.cronin@gmail.com"
    },
    "method": {
        "mode": "web",
        "platform": "orbital",
        "identity": "3rdparty",
        "encoding": "human"
    },
    "items": [{
        "time": "2019-12-06T08:15:00-08:00",
        "location": {
            "latitude": -33.854,
            "longitude": 116.071
        },
        "data": {
            "observableType": "facility",
            "commonName": "Greenbushes Mine",
            "description": "Open pit mine in the Greenbushes district of Western Australia",
            "capabilities": [{
                "name": "coltan extraction",
                "activity": {
                    "process": {
                        "nomenclature": "ISIC",
                        "code": "B0729"
                    }
                },
                "outputs": [{
                    "material": {
                        "nomenclature": "HS",
                        "code": "2615.90"
                    }
                }],
                "equipment": [{
                        "nomenclature": "CPC",
                        "code": "444"
                    },
                    {
                        "nomenclature": "HS",
                        "code": "8474"
                    }
                ]
            }]
        }
    }, {
        "time": "2019-12-06T08:15:00-08:00",
        "location": {
            "latitude": -33.86,
            "longitude": 116.065
        },
        "data": {
            "observableType": "facility",
            "commonName": "Tantalum primary processor",
            "capabilities": [{
                "inputs": [{
                    "material": {
                        "nomenclature": "HS",
                        "code": "2615.90"
                    }
                }],
                "outputs": [{
                    "material": {
                        "nomenclature": "HS",
                        "code": "2615.90"
                    }
                }],
                "activity": {
                    "process": {
                        "nomenclature": "ISIC",
                        "code": "B0729"
                    }
                }
            }]
        }
    }, {
        "time": "2019-12-06T08:15:00-08:00",
        "location": {
            "latitude": -33.86,
            "longitude": 116.055
        },
        "data": {
            "observableType": "facility",
            "commonName": "Tantalum secondary processor",
            "capabilities": [{
                "inputs": [{
                    "material": {
                        "nomenclature": "HS",
                        "code": "2615.90"
                    }
                }],
                "outputs": [{
                    "material": {
                        "nomenclature": "HS",
                        "code": "8103.20"
                    }
                }, {
                    "material": {
                        "nomenclature": "HS",
                        "code": "8103.30"
                    }
                }, {
                    "material": {
                        "nomenclature": "HS",
                        "code": "8103.90"
                    }
                }],
                "activity": {
                    "process": {
                        "nomenclature": "ISIC",
                        "code": "C2399"
                    }
                }
            }]
        }
    }, {
        "time": "2019-12-06T08:15:00-08:00",
        "location": {
            "latitude": -33.859,
            "longitude": 116.056
        },
        "data": {
            "observableType": "reservoir",
            "attributes": {
                "matterContents": "solid",
                "site": "uncovered",
                "support": "on-ground",
                "envelope": "pile",
                "shape": "irregular",
                "wall": "none"
            },
            "capacity": {
                "capacityNominal": {
                    "unit": "cu m",
                    "amount": 50000
                }
            },
            "purpose": {
                "usages": ["working supply"]
            }
        }
    }]
}

validate( j, s, resolver=newResolver )
