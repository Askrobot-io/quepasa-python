# BatchStatus


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** | Status of the batch (e.g., \&quot;uploaded\&quot;, \&quot;backlog\&quot;, \&quot;in_progress\&quot;, \&quot;done\&quot;). Possible values: - Batch state: uploaded - Batch state: backlog - Batch state: in_progress - Batch state: done  | 
**data** | [**BatchStatusData**](BatchStatusData.md) |  | [optional] 

## Example

```python
from quepasa.models.batch_status import BatchStatus

# TODO update the JSON string below
json = "{}"
# create an instance of BatchStatus from a JSON string
batch_status_instance = BatchStatus.from_json(json)
# print the JSON string representation of the object
print(BatchStatus.to_json())

# convert the object into a dict
batch_status_dict = batch_status_instance.to_dict()
# create an instance of BatchStatus from a dict
batch_status_from_dict = BatchStatus.from_dict(batch_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


