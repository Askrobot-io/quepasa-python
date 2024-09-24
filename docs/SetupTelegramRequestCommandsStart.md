# SetupTelegramRequestCommandsStart

Telegram /start command.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Menu label. | [optional] 
**message** | **str** | Message details. | [optional] 

## Example

```python
from quepasa.models.setup_telegram_request_commands_start import SetupTelegramRequestCommandsStart

# TODO update the JSON string below
json = "{}"
# create an instance of SetupTelegramRequestCommandsStart from a JSON string
setup_telegram_request_commands_start_instance = SetupTelegramRequestCommandsStart.from_json(json)
# print the JSON string representation of the object
print(SetupTelegramRequestCommandsStart.to_json())

# convert the object into a dict
setup_telegram_request_commands_start_dict = setup_telegram_request_commands_start_instance.to_dict()
# create an instance of SetupTelegramRequestCommandsStart from a dict
setup_telegram_request_commands_start_from_dict = SetupTelegramRequestCommandsStart.from_dict(setup_telegram_request_commands_start_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


