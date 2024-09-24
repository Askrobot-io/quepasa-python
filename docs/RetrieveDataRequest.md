# RetrieveDataRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**engine** | **str** | Operation mode, either &#39;search&#39; to search data or &#39;answer&#39; to generate a response. | [optional] 
**question** | **str** | Natural language query to retrieve or answer. | [optional] 
**user_info** | [**RetrieveDataRequestUserInfo**](RetrieveDataRequestUserInfo.md) |  | [optional] 

## Example

```python
from quepasa.models.retrieve_data_request import RetrieveDataRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RetrieveDataRequest from a JSON string
retrieve_data_request_instance = RetrieveDataRequest.from_json(json)
# print the JSON string representation of the object
print(RetrieveDataRequest.to_json())

# convert the object into a dict
retrieve_data_request_dict = retrieve_data_request_instance.to_dict()
# create an instance of RetrieveDataRequest from a dict
retrieve_data_request_from_dict = RetrieveDataRequest.from_dict(retrieve_data_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


