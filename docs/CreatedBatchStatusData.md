# CreatedBatchStatusData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**batch_id** | **str** | Batch ID | [optional] 
**processed_ids** | **List[str]** |  | [optional] 

## Example

```python
from quepasa.models.created_batch_status_data import CreatedBatchStatusData

# TODO update the JSON string below
json = "{}"
# create an instance of CreatedBatchStatusData from a JSON string
created_batch_status_data_instance = CreatedBatchStatusData.from_json(json)
# print the JSON string representation of the object
print(CreatedBatchStatusData.to_json())

# convert the object into a dict
created_batch_status_data_dict = created_batch_status_data_instance.to_dict()
# create an instance of CreatedBatchStatusData from a dict
created_batch_status_data_from_dict = CreatedBatchStatusData.from_dict(created_batch_status_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


