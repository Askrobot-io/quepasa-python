# DocumentDetailData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier for the document. | 
**url** | **str** | Original URL of the document. | 
**domain** | **str** | The name of a group of documents. Defaults to \&quot;default\&quot;. | 
**title** | **str** | Optional keywords for search optimization. | 
**keywords** | **str** | Optional keywords for search optimization. | 
**pages** | [**List[DocumentDetailDataPagesInner]**](DocumentDetailDataPagesInner.md) |  | 
**languages** | **List[str]** |  | 
**created_at** | **datetime** | Creation date in ISO 8601 format. | 
**updated_at** | **datetime** | Update date in ISO 8601 format. | 

## Example

```python
from quepasa.models.document_detail_data import DocumentDetailData

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentDetailData from a JSON string
document_detail_data_instance = DocumentDetailData.from_json(json)
# print the JSON string representation of the object
print(DocumentDetailData.to_json())

# convert the object into a dict
document_detail_data_dict = document_detail_data_instance.to_dict()
# create an instance of DocumentDetailData from a dict
document_detail_data_from_dict = DocumentDetailData.from_dict(document_detail_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


