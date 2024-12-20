# RetrieveChunksRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**question** | **str** | Natural language query to retrieve or answer. | [optional] 
**domain** | **str** | The name of a group of documents. | [optional] 
**kind** | **str** | (Experimental) Specifies the type of chunk. Can be \&quot;text\&quot; for raw text chunks, \&quot;summary\&quot; for chunks that are summaries of raw text, or \&quot;all\&quot; to include both types. | [optional] 
**relevance_weights** | [**RetrieveAnswerRequestRelevanceWeights**](RetrieveAnswerRequestRelevanceWeights.md) |  | [optional] 
**document_relevance_weights** | [**RetrieveAnswerRequestDocumentRelevanceWeights**](RetrieveAnswerRequestDocumentRelevanceWeights.md) |  | [optional] 
**chunk_relevance_weights** | [**RetrieveAnswerRequestDocumentRelevanceWeights**](RetrieveAnswerRequestDocumentRelevanceWeights.md) |  | [optional] 
**reranker_prompt** | **str** | A prompt template used by the reranking model to prioritize and reorder both documents and chunks based on their relevance to a query. This prompt guides the model in assessing the importance of each document and refining the ranking output.  | [optional] 
**document_reranker_prompt** | **str** | A prompt template used by the reranking model to prioritize and reorder documents based on their relevance to a query. This prompt guides the model in assessing the importance of each document and refining the ranking output.  | [optional] 
**chunk_reranker_prompt** | **str** | A prompt template used by the reranking model to prioritize and reorder chunks based on their relevance to a query. This prompt guides the model in assessing the importance of each document and refining the ranking output.  | [optional] 
**user_info** | [**RetrieveAnswerRequestUserInfo**](RetrieveAnswerRequestUserInfo.md) |  | [optional] 

## Example

```python
from quepasa.models.retrieve_chunks_request import RetrieveChunksRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RetrieveChunksRequest from a JSON string
retrieve_chunks_request_instance = RetrieveChunksRequest.from_json(json)
# print the JSON string representation of the object
print(RetrieveChunksRequest.to_json())

# convert the object into a dict
retrieve_chunks_request_dict = retrieve_chunks_request_instance.to_dict()
# create an instance of RetrieveChunksRequest from a dict
retrieve_chunks_request_from_dict = RetrieveChunksRequest.from_dict(retrieve_chunks_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


