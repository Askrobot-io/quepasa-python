# ReplaceDocumentsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domain** | **str** | The name of a group of documents. Defaults to \&quot;default\&quot;. | [optional] 
**documents** | [**List[Document]**](Document.md) | List of documents to replace. | 

## Example

```python
from quepasa.models.replace_documents_request import ReplaceDocumentsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ReplaceDocumentsRequest from a JSON string
replace_documents_request_instance = ReplaceDocumentsRequest.from_json(json)
# print the JSON string representation of the object
print(ReplaceDocumentsRequest.to_json())

# convert the object into a dict
replace_documents_request_dict = replace_documents_request_instance.to_dict()
# create an instance of ReplaceDocumentsRequest from a dict
replace_documents_request_from_dict = ReplaceDocumentsRequest.from_dict(replace_documents_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


