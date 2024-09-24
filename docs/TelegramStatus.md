# TelegramStatus


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** | Status of the operation. | 

## Example

```python
from quepasa.models.telegram_status import TelegramStatus

# TODO update the JSON string below
json = "{}"
# create an instance of TelegramStatus from a JSON string
telegram_status_instance = TelegramStatus.from_json(json)
# print the JSON string representation of the object
print(TelegramStatus.to_json())

# convert the object into a dict
telegram_status_dict = telegram_status_instance.to_dict()
# create an instance of TelegramStatus from a dict
telegram_status_from_dict = TelegramStatus.from_dict(telegram_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


