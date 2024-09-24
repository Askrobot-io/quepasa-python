# UpsertDocumentsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domain** | **str** | The name of a group of documents. Defaults to \&quot;default\&quot;. | [optional] 
**documents** | [**List[Document]**](Document.md) | List of documents to upsert. | 

## Example

```python
from quepasa.models.upsert_documents_request import UpsertDocumentsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpsertDocumentsRequest from a JSON string
upsert_documents_request_instance = UpsertDocumentsRequest.from_json(json)
# print the JSON string representation of the object
print(UpsertDocumentsRequest.to_json())

# convert the object into a dict
upsert_documents_request_dict = upsert_documents_request_instance.to_dict()
# create an instance of UpsertDocumentsRequest from a dict
upsert_documents_request_from_dict = UpsertDocumentsRequest.from_dict(upsert_documents_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


