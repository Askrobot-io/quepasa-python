# Document


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier for the document. | 
**url** | **str** | Original URL of the document. | 
**text** | **str** | Raw text content of the document. | [optional] 
**html** | **str** | Raw HTML content of the document. | [optional] 
**markdown** | **str** | Raw Markdown content of the document. | [optional] 
**pages** | [**List[DocumentPagesInner]**](DocumentPagesInner.md) |  | [optional] 
**language** | **str** | Two-character language code (e.g., \&quot;en\&quot;). | [optional] 
**title** | **str** | Optional title of the document. | [optional] 
**keywords** | **str** | Optional keywords for search optimization. | [optional] 
**created_at** | **datetime** | Creation date in ISO 8601 format. | [optional] 
**updated_at** | **datetime** | Update date in ISO 8601 format. | [optional] 

## Example

```python
from quepasa.models.document import Document

# TODO update the JSON string below
json = "{}"
# create an instance of Document from a JSON string
document_instance = Document.from_json(json)
# print the JSON string representation of the object
print(Document.to_json())

# convert the object into a dict
document_dict = document_instance.to_dict()
# create an instance of Document from a dict
document_from_dict = Document.from_dict(document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


