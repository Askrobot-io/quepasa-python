# SetupTelegramRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**token** | **str** | Telegram bot token. | [optional] 
**commands** | [**SetupTelegramRequestCommands**](SetupTelegramRequestCommands.md) |  | [optional] 

## Example

```python
from quepasa.models.setup_telegram_request import SetupTelegramRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SetupTelegramRequest from a JSON string
setup_telegram_request_instance = SetupTelegramRequest.from_json(json)
# print the JSON string representation of the object
print(SetupTelegramRequest.to_json())

# convert the object into a dict
setup_telegram_request_dict = setup_telegram_request_instance.to_dict()
# create an instance of SetupTelegramRequest from a dict
setup_telegram_request_from_dict = SetupTelegramRequest.from_dict(setup_telegram_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


