# RetrieveAnswerRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**question** | **str** | Natural language query to retrieve or answer. | [optional] 
**domain** | **str** | The name of a group of documents. | [optional] 
**llm** | **str** | This is the model that will generate answers to questions based on the retrieved search results. Options: - gpt-3.5-turbo-16k-0613 - mistral:mistral-large-2402 - anthropic:claude-3-5-sonnet-20240620 - replicate:meta-llama-3-70b-instruct  | [optional] 
**prompt** | **str** | The prompt used for RAG, with placeholders like {{LANGUAGE}} for the language in which the question was asked, and {{SOURCES}} for listing the relevant chunks. For example &#x60;&#x60;&#x60;plaintext You&#39;re a bot-assistant that answers the questions.  When answering the question, use the following rules: - always answer in {{LANGUAGE}} language; - use ONLY the information from the sources below; - answer briefly in just a few sentences, strictly in accordance with the sources, and do not make any assumptions; - reference the source if you use it in the answer, e.g. [#1] or [#2][#4]; - if there is no information on the question in the sources: say that you can&#39;t find the answer and ask the user to try to reformulate the question.  Sources: {{SOURCES}} &#x60;&#x60;&#x60;  | [optional] 
**answer_prompt_size** | **int** | The length of the response in tokens. This parameter defines the maximum number of tokens that the model can use to generate its answer. | [optional] 
**prompt_total_size** | **int** | The maximum length of the prompt in tokens. This sets the upper limit for how many tokens can be used for the combined input to the model, including the user&#39;s query and the retrieved document context. | [optional] 
**document_relevance_weights** | [**RetrieveAnswerRequestDocumentRelevanceWeights**](RetrieveAnswerRequestDocumentRelevanceWeights.md) |  | [optional] 
**chunk_relevance_weights** | [**RetrieveAnswerRequestDocumentRelevanceWeights**](RetrieveAnswerRequestDocumentRelevanceWeights.md) |  | [optional] 
**user_info** | [**RetrieveAnswerRequestUserInfo**](RetrieveAnswerRequestUserInfo.md) |  | [optional] 

## Example

```python
from quepasa.models.retrieve_answer_request import RetrieveAnswerRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RetrieveAnswerRequest from a JSON string
retrieve_answer_request_instance = RetrieveAnswerRequest.from_json(json)
# print the JSON string representation of the object
print(RetrieveAnswerRequest.to_json())

# convert the object into a dict
retrieve_answer_request_dict = retrieve_answer_request_instance.to_dict()
# create an instance of RetrieveAnswerRequest from a dict
retrieve_answer_request_from_dict = RetrieveAnswerRequest.from_dict(retrieve_answer_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


