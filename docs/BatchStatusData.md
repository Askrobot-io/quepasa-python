# BatchStatusData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domain** | **str** | The name of a group of documents. | [optional] 
**processed_ids** | **List[str]** |  | [optional] 

## Example

```python
from quepasa.models.batch_status_data import BatchStatusData

# TODO update the JSON string below
json = "{}"
# create an instance of BatchStatusData from a JSON string
batch_status_data_instance = BatchStatusData.from_json(json)
# print the JSON string representation of the object
print(BatchStatusData.to_json())

# convert the object into a dict
batch_status_data_dict = batch_status_data_instance.to_dict()
# create an instance of BatchStatusData from a dict
batch_status_data_from_dict = BatchStatusData.from_dict(batch_status_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


