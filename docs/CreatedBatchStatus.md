# CreatedBatchStatus


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** | Status of the batch (e.g., \&quot;uploaded\&quot;, \&quot;backlog\&quot;, \&quot;in_progress\&quot;, \&quot;done\&quot;). | 
**data** | [**CreatedBatchStatusData**](CreatedBatchStatusData.md) |  | 

## Example

```python
from quepasa.models.created_batch_status import CreatedBatchStatus

# TODO update the JSON string below
json = "{}"
# create an instance of CreatedBatchStatus from a JSON string
created_batch_status_instance = CreatedBatchStatus.from_json(json)
# print the JSON string representation of the object
print(CreatedBatchStatus.to_json())

# convert the object into a dict
created_batch_status_dict = created_batch_status_instance.to_dict()
# create an instance of CreatedBatchStatus from a dict
created_batch_status_from_dict = CreatedBatchStatus.from_dict(created_batch_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


