DEVICE = {
    'deviceId': 'c71f2973-4f10-42eb-bef1-5feb02985919',
    'pairingCode': 'ucMdwRJ',
    'manufacturerName': 'LightBerry',
    'friendlyName': 'SwitchBerry',
    'type': 'switch',
    'description': 'A simple on and off switch',
    'alexa': {
        'displayCategories': ['SWITCH'],
        'additionalDetails': {},
        'capabilities': [
            {
                "type": "AlexaInterface",
                "interface": "Alexa.PowerController",
                "version": "3",
                "properties": {
                    "supported": [
                        { "name": "powerState" }
                    ],
                    "proactivelyReported": False,
                    "retrievable": True
                }
            },
            {
                "type": "AlexaInterface",
                "interface": "Alexa.EndpointHealth",
                "version": "3",
                "properties": {
                    "supported":[
                        { "name":"connectivity" }
                    ],
                    "proactivelyReported": False,
                    "retrievable": True
                }
            },
            {
                "type": "AlexaInterface",
                "interface": "Alexa",
                "version": "3"
            }
        ]
    }
}
