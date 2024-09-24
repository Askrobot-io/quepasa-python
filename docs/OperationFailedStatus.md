# OperationFailedStatus


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** | Status. | 

## Example

```python
from quepasa.models.operation_failed_status import OperationFailedStatus

# TODO update the JSON string below
json = "{}"
# create an instance of OperationFailedStatus from a JSON string
operation_failed_status_instance = OperationFailedStatus.from_json(json)
# print the JSON string representation of the object
print(OperationFailedStatus.to_json())

# convert the object into a dict
operation_failed_status_dict = operation_failed_status_instance.to_dict()
# create an instance of OperationFailedStatus from a dict
operation_failed_status_from_dict = OperationFailedStatus.from_dict(operation_failed_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


