# RetrieveDataRequestUserInfo

Optional user info to track requests.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique user ID. | [optional] 

## Example

```python
from quepasa.models.retrieve_data_request_user_info import RetrieveDataRequestUserInfo

# TODO update the JSON string below
json = "{}"
# create an instance of RetrieveDataRequestUserInfo from a JSON string
retrieve_data_request_user_info_instance = RetrieveDataRequestUserInfo.from_json(json)
# print the JSON string representation of the object
print(RetrieveDataRequestUserInfo.to_json())

# convert the object into a dict
retrieve_data_request_user_info_dict = retrieve_data_request_user_info_instance.to_dict()
# create an instance of RetrieveDataRequestUserInfo from a dict
retrieve_data_request_user_info_from_dict = RetrieveDataRequestUserInfo.from_dict(retrieve_data_request_user_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


