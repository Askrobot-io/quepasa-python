# quepasa.DefaultApi

All URIs are relative to *https://api.quepasa.ai/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**upsert_files**](DefaultApi.md#upsert_files) | **POST** /upload/data/files/{domain} | Upsert files
[**upsert_documents**](DefaultApi.md#upsert_documents) | **POST** /upload/data/documents/{domain} | Upsert documents
[**upsert_urls**](DefaultApi.md#upsert_urls) | **POST** /upload/data/urls/{domain} | Upsert urls
[**replace_documents**](DefaultApi.md#replace_documents) | **PUT** /upload/data/documents/{domain} | Replace documents
[**get_batch_status**](DefaultApi.md#get_batch_status) | **GET** /upload/data/batches/{id} | Get batch status
[**get_document**](DefaultApi.md#get_document) | **GET** /upload/data/documents/{domain}/{id} | Get document details
[**list_all_documents**](DefaultApi.md#list_all_documents) | **GET** /upload/data/documents | List all documents
[**list_documents**](DefaultApi.md#list_documents) | **GET** /upload/data/documents/{domain} | List documents
[**remove_document**](DefaultApi.md#remove_document) | **DELETE** /upload/data/documents/{domain}/{id} | Remove document
[**remove_domain**](DefaultApi.md#remove_domain) | **DELETE** /upload/data/documents/{domain} | Remove domain
[**retrieve_answer**](DefaultApi.md#retrieve_answer) | **POST** /retrieve/answer | Retrieve answers
[**retrieve_chunks**](DefaultApi.md#retrieve_chunks) | **POST** /retrieve/chunks | Retrieve search results
[**setup_telegram**](DefaultApi.md#setup_telegram) | **PATCH** /upload/data/telegram | Setup Telegram integration


# **upsert_files**
> CreatedBatchStatus upsert_files(domain, file, language=language)

Upsert files

Upload and upsert files into the document system.

Supported formats: txt, md, html, pdf, doc, docx, xls, xlsx, ppt, pptx

### Example

* Bearer (Opaque) Authentication (bearerAuth):

```python
import quepasa
from quepasa.models.created_batch_status import CreatedBatchStatus
from quepasa.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.quepasa.ai/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = quepasa.Configuration(
    host = "https://api.quepasa.ai/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (Opaque): bearerAuth
configuration = quepasa.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with quepasa.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    client = quepasa.DefaultApi(api_client)
    domain = 'default' # str | The name of a group of documents. Defaults to "default".
    file = 'filename.pdf' # Supported formats: txt, md, html, pdf, doc, docx, xls, xlsx, ppt, pptx
    language = 'en' # str | Two-character language code (e.g., "en"). (optional)

    try:
        # Upsert files
        response = client.upsert_files(domain, file, language=language)
        print("The response of client.upsert_files:\n")
        pprint(response)
    except Exception as e:
        print("Exception when calling client.upsert_files: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain** | **str**| The name of a group of documents. By default, if the field is left empty, the domain name is "default". |
 **file** | **str**| Path to the file to be uploaded. |
 **language** | **str**| Two-character language code (e.g., "en" for English). If the language is not specified, it will be detected automatically. | [optional]

### Return type

[**CreatedBatchStatus**](CreatedBatchStatus.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Operation accepted. Batch ID returned. |  -  |
**500** | Operation failed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)



# **upsert_documents**
> CreatedBatchStatus upsert_documents(domain, documents)

Upsert documents

Insert new documents or update existing ones based on the ID.

### Example

* Bearer (Opaque) Authentication (bearerAuth):

```python
import quepasa
from quepasa.models.created_batch_status import CreatedBatchStatus
from quepasa.models.document import Document
from quepasa.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.quepasa.ai/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = quepasa.Configuration(
    host = "https://api.quepasa.ai/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (Opaque): bearerAuth
configuration = quepasa.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with quepasa.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    client = quepasa.DefaultApi(api_client)
    domain = 'default' # str | The name of a group of documents. Defaults to "default".
    documents = [
        {
            # Required fields
            'id': 'llm-text', # string
            'url': "https://en.wikipedia.org/wiki/Large_language_model",

            'title': "Large language model",
            'language': "en", # two-char language code in lowercase
            'text': """
    A large language model (LLM) is a computational model capable of language generation or other natural language processing tasks. As language models, LLMs acquire these abilities by learning statistical relationships from vast amounts of text during a self-supervised and semi-supervised training process.

    The largest and most capable LLMs, as of August 2024, are artificial neural networks built with a decoder-only transformer-based architecture, which enables efficient processing and generation of large-scale text data. Modern models can be fine-tuned for specific tasks or can be guided by prompt engineering.
    These models acquire predictive power regarding syntax, semantics, and ontologies inherent in human language corpora, but they also inherit inaccuracies and biases present in the data they are trained on.

    Some notable LLMs are OpenAI's GPT series of models (e.g., GPT-3.5, GPT-4 and GPT-4o; used in ChatGPT and Microsoft Copilot), Google's Gemini (the latter of which is currently used in the chatbot of the same name), Meta's LLaMA family of models, IBM's Granite models initially released with Watsonx, Anthropic's Claude models, and Mistral AI's models.
            """.strip(),
            # 'html': "", # or send text
            # 'markdown': "", # or send markdown

            # Optional fields:
            # - 'keywords': document keywords, string, by default empty
            # - 'created_at': "2024-05-20T07:26:06Z", # document creation datetime, by default datetime of first creation of this document via API
            # - 'updated_at': "2024-05-20T07:26:06Z", # document last update datetime, by default datetime of last update of this document via API
        },

        {
            # Required fields
            'id': 'llm-chunks', # string
            'url': "https://en.wikipedia.org/wiki/Large_language_model",

            'title': "Large language model",

            'pages': [
                {                    
                    'language': "en", # two-char language code in lowercase
                    'text': """
    A large language model (LLM) is a computational model capable of language generation or other natural language processing tasks. As language models, LLMs acquire these abilities by learning statistical relationships from vast amounts of text during a self-supervised and semi-supervised training process. and Mistral AI's models.
                    """.strip(),
                },
                {                    
                    'language': "en", # two-char language code in lowercase
                    'text': """
    The largest and most capable LLMs, as of August 2024, are artificial neural networks built with a decoder-only transformer-based architecture, which enables efficient processing and generation of large-scale text data. Modern models can be fine-tuned for specific tasks or can be guided by prompt engineering.
    These models acquire predictive power regarding syntax, semantics, and ontologies inherent in human language corpora, but they also inherit inaccuracies and biases present in the data they are trained on.
                    """.strip(),
                },
                {                    
                    'language': "en", # two-char language code in lowercase
                    'text': """
    Some notable LLMs are OpenAI's GPT series of models (e.g., GPT-3.5, GPT-4 and GPT-4o; used in ChatGPT and Microsoft Copilot), Google's Gemini (the latter of which is currently used in the chatbot of the same name), Meta's LLaMA family of models, IBM's Granite models initially released with Watsonx, Anthropic's Claude models, and Mistral AI's models.
                    """.strip(),
                },
            ],

            # Optional fields:
            # - 'keywords': document keywords, string, by default empty
            # - 'created_at': "2024-05-20T07:26:06Z", # document creation datetime, by default datetime of first creation of this document via API
            # - 'updated_at': "2024-05-20T07:26:06Z", # document last update datetime, by default datetime of last update of this document via API
        },
    ]

    try:
        # Upsert documents
        response = client.upsert_documents(domain, documents)
        print("The response of client.upsert_documents:\n")
        pprint(response)
    except Exception as e:
        print("Exception when calling client.upsert_documents: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain** | **str**| The name of a group of documents. By default, if the field is left empty, the domain name is "default". |
 **documents** | [**List[Document]**](Document.md)|  |

### Return type

[**CreatedBatchStatus**](CreatedBatchStatus.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Operation accepted. Batch ID returned. |  -  |
**500** | Operation failed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)



# **upsert_urls**
> CreatedBatchStatus upsert_urls(domain, urls)

Upsert urls

Upsert urls into the document system.

Supported formats: txt, md, html, pdf, doc, docx, xls, xlsx, ppt, pptx, Youtube transcripts (form Youtube videos)

### Example

* Bearer (Opaque) Authentication (bearerAuth):

```python
import quepasa
from quepasa.models.created_batch_status import CreatedBatchStatus
from quepasa.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.quepasa.ai/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = quepasa.Configuration(
    host = "https://api.quepasa.ai/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (Opaque): bearerAuth
configuration = quepasa.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with quepasa.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    client = quepasa.DefaultApi(api_client)
    domain = 'default' # str | The name of a group of documents. Defaults to "default".
    urls = [
        'https://quepasa.ai',
        'https://docs.quepasa.ai',
        'https://www.youtube.com/watch?v=dQw4w9WgXcQ',
    ]

    try:
        # Upsert urls
        response = client.upsert_urls(domain, urls)
        print("The response of client.upsert_urls:\n")
        pprint(response)
    except Exception as e:
        print("Exception when calling client.upsert_urls: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain** | **str**| The name of a group of documents. By default, if the field is left empty, the domain name is "default". |
 **urls** | [**List[str]**](str.md)|  |

### Return type

[**CreatedBatchStatus**](CreatedBatchStatus.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Operation accepted. Batch ID returned. |  -  |
**500** | Operation failed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)



# **replace_documents**
> CreatedBatchStatus replace_documents(domain, documents)

Replace documents

Replace all documents in the specified domain with the provided documents.

### Example

* Bearer (Opaque) Authentication (bearerAuth):

```python
import quepasa
from quepasa.models.created_batch_status import CreatedBatchStatus
from quepasa.models.document import Document
from quepasa.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.quepasa.ai/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = quepasa.Configuration(
    host = "https://api.quepasa.ai/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (Opaque): bearerAuth
configuration = quepasa.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with quepasa.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    client = quepasa.DefaultApi(api_client)
    domain = 'default' # str | The name of a group of documents. Defaults to "default".
    documents = [
        {
            # Required fields
            'id': 'llm-text', # string
            'url': "https://en.wikipedia.org/wiki/Large_language_model",

            'title': "Large language model",
            'language': "en", # two-char language code in lowercase
            'text': """
    A large language model (LLM) is a computational model capable of language generation or other natural language processing tasks. As language models, LLMs acquire these abilities by learning statistical relationships from vast amounts of text during a self-supervised and semi-supervised training process.

    The largest and most capable LLMs, as of August 2024, are artificial neural networks built with a decoder-only transformer-based architecture, which enables efficient processing and generation of large-scale text data. Modern models can be fine-tuned for specific tasks or can be guided by prompt engineering.
    These models acquire predictive power regarding syntax, semantics, and ontologies inherent in human language corpora, but they also inherit inaccuracies and biases present in the data they are trained on.

    Some notable LLMs are OpenAI's GPT series of models (e.g., GPT-3.5, GPT-4 and GPT-4o; used in ChatGPT and Microsoft Copilot), Google's Gemini (the latter of which is currently used in the chatbot of the same name), Meta's LLaMA family of models, IBM's Granite models initially released with Watsonx, Anthropic's Claude models, and Mistral AI's models.
            """.strip(),
            # 'html': "", # or send text
            # 'markdown': "", # or send markdown

            # Optional fields:
            # - 'keywords': document keywords, string, by default empty
            # - 'created_at': "2024-05-20T07:26:06Z", # document creation datetime, by default datetime of first creation of this document via API
            # - 'updated_at': "2024-05-20T07:26:06Z", # document last update datetime, by default datetime of last update of this document via API
        },

        {
            # Required fields
            'id': 'llm-chunks', # string
            'url': "https://en.wikipedia.org/wiki/Large_language_model",

            'title': "Large language model",

            'pages': [
                {                    
                    'language': "en", # two-char language code in lowercase
                    'text': """
    A large language model (LLM) is a computational model capable of language generation or other natural language processing tasks. As language models, LLMs acquire these abilities by learning statistical relationships from vast amounts of text during a self-supervised and semi-supervised training process. and Mistral AI's models.
                    """.strip(),
                },
                {                    
                    'language': "en", # two-char language code in lowercase
                    'text': """
    The largest and most capable LLMs, as of August 2024, are artificial neural networks built with a decoder-only transformer-based architecture, which enables efficient processing and generation of large-scale text data. Modern models can be fine-tuned for specific tasks or can be guided by prompt engineering.
    These models acquire predictive power regarding syntax, semantics, and ontologies inherent in human language corpora, but they also inherit inaccuracies and biases present in the data they are trained on.
                    """.strip(),
                },
                {                    
                    'language': "en", # two-char language code in lowercase
                    'text': """
    Some notable LLMs are OpenAI's GPT series of models (e.g., GPT-3.5, GPT-4 and GPT-4o; used in ChatGPT and Microsoft Copilot), Google's Gemini (the latter of which is currently used in the chatbot of the same name), Meta's LLaMA family of models, IBM's Granite models initially released with Watsonx, Anthropic's Claude models, and Mistral AI's models.
                    """.strip(),
                },
            ],

            # Optional fields:
            # - 'keywords': document keywords, string, by default empty
            # - 'created_at': "2024-05-20T07:26:06Z", # document creation datetime, by default datetime of first creation of this document via API
            # - 'updated_at': "2024-05-20T07:26:06Z", # document last update datetime, by default datetime of last update of this document via API
        },
    ]

    try:
        # Replace documents
        response = client.replace_documents(domain, documents)
        print("The response of client.replace_documents:\n")
        pprint(response)
    except Exception as e:
        print("Exception when calling client.replace_documents: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain** | **str**| The name of a group of documents. By default, if the field is left empty, the domain name is "default". |
 **documents** | [**List[Document]**](Document.md)|  |

### Return type

[**CreatedBatchStatus**](CreatedBatchStatus.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Operation accepted. Batch ID returned. |  -  |
**500** | Operation failed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)



# **get_batch_status**
> BatchStatus get_batch_status(id)

Get batch status

Retrieve the status of a batch using its batch ID.

### Example

* Bearer (Opaque) Authentication (bearerAuth):

```python
import quepasa
from quepasa.models.batch_status import BatchStatus
from quepasa.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.quepasa.ai/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = quepasa.Configuration(
    host = "https://api.quepasa.ai/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (Opaque): bearerAuth
configuration = quepasa.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with quepasa.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    client = quepasa.DefaultApi(api_client)
    id = '1234567890.12345' # str

    try:
        # Get batch status
        response = client.get_batch_status(id)
        print("The response of client.get_batch_status:\n")
        pprint(response)
    except Exception as e:
        print("Exception when calling client.get_batch_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

### Return type

[**BatchStatus**](BatchStatus.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Batch status retrieved. Status of the batch (e.g., "uploaded", "backlog", "in_progress", "done"). Possible values: "Batch state: uploaded", "Batch state: backlog", "Batch state: in_progress", "Batch state: done" |  -  |
**404** | Batch not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)



# **get_document**
> DocumentDetail get_document(domain, id)

Get document details

Retrieve details of a document by its domain and ID.

### Example

* Bearer (Opaque) Authentication (bearerAuth):

```python
import quepasa
from quepasa.models.document_detail import DocumentDetail
from quepasa.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.quepasa.ai/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = quepasa.Configuration(
    host = "https://api.quepasa.ai/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (Opaque): bearerAuth
configuration = quepasa.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with quepasa.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    client = quepasa.DefaultApi(api_client)
    domain = 'default' # str | The name of a group of documents. Defaults to "default".
    id = 'document_id' # str

    try:
        # Get document details
        response = client.get_document(domain, id)
        print("The response of client.get_document:\n")
        pprint(response)
    except Exception as e:
        print("Exception when calling client.get_document: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain** | **str**| The name of a group of documents. By default, if the field is left empty, the domain name is "default". |
 **id** | **str**|  |

### Return type

[**DocumentDetail**](DocumentDetail.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Document details retrieved. |  -  |
**404** | Document not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_all_documents**
> DomainListDetail list_all_documents()

List all documents

List all document IDs in all available domains.

### Example

* Bearer (Opaque) Authentication (bearerAuth):

```python
import quepasa
from quepasa.models.domain_list_detail import DomainListDetail
from quepasa.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.quepasa.ai/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = quepasa.Configuration(
    host = "https://api.quepasa.ai/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (Opaque): bearerAuth
configuration = quepasa.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with quepasa.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    client = quepasa.DefaultApi(api_client)

    try:
        # List all documents
        response = client.list_all_documents()
        print("The response of client.list_all_documents:\n")
        pprint(response)
    except Exception as e:
        print("Exception when calling client.list_all_documents: %s\n" % e)
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**DomainListDetail**](DomainListDetail.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Operation accepted. Batch ID returned. |  -  |
**500** | Operation failed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)



# **list_documents**
> DomainDetail list_documents(domain)

List documents

List all document IDs in the specified domain.

### Example

* Bearer (Opaque) Authentication (bearerAuth):

```python
import quepasa
from quepasa.models.domain_detail import DomainDetail
from quepasa.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.quepasa.ai/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = quepasa.Configuration(
    host = "https://api.quepasa.ai/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (Opaque): bearerAuth
configuration = quepasa.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with quepasa.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    client = quepasa.DefaultApi(api_client)
    domain = 'default' # str | The name of a group of documents. Defaults to "default".

    try:
        # List documents
        response = client.list_documents(domain)
        print("The response of client.list_documents:\n")
        pprint(response)
    except Exception as e:
        print("Exception when calling client.list_documents: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain** | **str**| The name of a group of documents. By default, if the field is left empty, the domain name is "default". |

### Return type

[**DomainDetail**](DomainDetail.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Operation accepted. Batch ID returned. |  -  |
**500** | Operation failed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)



# **remove_document**
> CreatedBatchStatus remove_document(domain, id)

Remove document

Remove a specific document by its domain and ID.

### Example

* Bearer (Opaque) Authentication (bearerAuth):

```python
import quepasa
from quepasa.models.created_batch_status import CreatedBatchStatus
from quepasa.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.quepasa.ai/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = quepasa.Configuration(
    host = "https://api.quepasa.ai/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (Opaque): bearerAuth
configuration = quepasa.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with quepasa.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    client = quepasa.DefaultApi(api_client)
    domain = 'default' # str | The name of a group of documents. Defaults to "default".
    id = 'document_id' # str

    try:
        # Remove document
        response = client.remove_document(domain, id)
        print("The response of client.remove_document:\n")
        pprint(response)
    except Exception as e:
        print("Exception when calling client.remove_document: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain** | **str**| The name of a group of documents. By default, if the field is left empty, the domain name is "default". |
 **id** | **str**|  |

### Return type

[**CreatedBatchStatus**](CreatedBatchStatus.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Operation accepted. Batch ID returned. |  -  |
**500** | Operation failed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)



# **remove_domain**
> CreatedBatchStatus remove_domain(domain)

Remove domain

Remove all documents from the specified domain.

### Example

* Bearer (Opaque) Authentication (bearerAuth):

```python
import quepasa
from quepasa.models.created_batch_status import CreatedBatchStatus
from quepasa.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.quepasa.ai/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = quepasa.Configuration(
    host = "https://api.quepasa.ai/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (Opaque): bearerAuth
configuration = quepasa.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with quepasa.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    client = quepasa.DefaultApi(api_client)
    domain = 'default' # str | The name of a group of documents. Defaults to "default".

    try:
        # Remove domain
        response = client.remove_domain(domain)
        print("The response of client.remove_domain:\n")
        pprint(response)
    except Exception as e:
        print("Exception when calling client.remove_domain: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain** | **str**| The name of a group of documents. By default, if the field is left empty, the domain name is "default". |

### Return type

[**CreatedBatchStatus**](CreatedBatchStatus.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Operation accepted. Batch ID returned. |  -  |
**500** | Operation failed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)



# **retrieve_answer**
> AnswerDetail retrieve_answer(retrieve_answer_request)

Retrieve answers

Generate an answer based on your data.

### Example

* Bearer (Opaque) Authentication (bearerAuth):

```python
import quepasa
from quepasa.models.answer_detail import AnswerDetail
from quepasa.models.retrieve_answer_request import RetrieveAnswerRequest
from quepasa.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.quepasa.ai/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = quepasa.Configuration(
    host = "https://api.quepasa.ai/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (Opaque): bearerAuth
configuration = quepasa.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with quepasa.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    client = quepasa.DefaultApi(api_client)

    retrieve_answer_request = {
        'question': "What is LLM?",
    }

    # OR

    retrieve_answer_request = {
        'question': "What is LLM?",
        'domain': "default",
    }

    # OR

    retrieve_answer_request = {
        'question': "What is LLM?",
        'domain': ["default", "another"],
    }

    # OR

    retrieve_answer_request = {
        'question': "What is LLM?",
        'llm': "mistral:mistral-large-2402",
    }

    # OR

    retrieve_answer_request = {
        'question': "What is LLM?",
        'prompt': """
You're a bot-assistant that answers the questions.

When answering the question, use the following rules:
- always answer in {{LANGUAGE}} language;
- use ONLY the information from the sources below;
- answer briefly in just a few sentences, strictly in accordance with the sources, and do not make any assumptions;
- reference the source if you use it in the answer, e.g. [#1] or [#2][#4];
- if there is no information on the question in the sources: say that you can't find the answer and ask the user to try to reformulate the question.

Sources:
{{SOURCES}}
        """.strip(),
    }

    # OR

    retrieve_answer_request = {
        'question': "What is LLM?",
        'document_relevance_weights': {
            "text": 1.0,
            "semantic": 0.0
        },
        'chunk_relevance_weights': {
            "text": 1.0,
            "semantic": 0.0
        }
    }

    try:
        # Retrieve answers
        response = client.retrieve_answer(retrieve_answer_request)
        print("The response of client.retrieve_answer:\n")
        pprint(response)
    except Exception as e:
        print("Exception when calling client.retrieve_answer: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **retrieve_answer_request** | [**RetrieveAnswerRequest**](RetrieveAnswerRequest.md)|  |

### Return type

[**AnswerDetail**](AnswerDetail.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)



# **retrieve_chunks**
> ChunksDetail retrieve_chunks(retrieve_chunks_request)

Retrieve search results

This endpoint allows you to perform a search on your data.

### Example

* Bearer (Opaque) Authentication (bearerAuth):

```python
import quepasa
from quepasa.models.chunks_detail import ChunksDetail
from quepasa.models.retrieve_chunks_request import RetrieveChunksRequest
from quepasa.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.quepasa.ai/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = quepasa.Configuration(
    host = "https://api.quepasa.ai/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (Opaque): bearerAuth
configuration = quepasa.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with quepasa.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    client = quepasa.DefaultApi(api_client)

    retrieve_chunks_request = {
        'question': "What is LLM?",
    }

    # OR

    retrieve_chunks_request = {
        'question': "What is LLM?",
        'domain': "default",
    }

    # OR

    retrieve_chunks_request = {
        'question': "What is LLM?",
        'domain': ["default", "another"],
    }

    # OR

    retrieve_chunks_request = {
        'question': "What is LLM?",
        'document_relevance_weights': {
            "text": 1.0,
            "semantic": 0.0
        },
        'chunk_relevance_weights': {
            "text": 1.0,
            "semantic": 0.0
        }
    }

    try:
        # Retrieve search results
        response = client.retrieve_chunks(retrieve_chunks_request)
        print("The response of client.retrieve_chunks:\n")
        pprint(response)
    except Exception as e:
        print("Exception when calling client.retrieve_chunks: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **retrieve_chunks_request** | [**RetrieveChunksRequest**](RetrieveChunksRequest.md)|  |

### Return type

[**ChunksDetail**](ChunksDetail.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)



# **setup_telegram**
> TelegramStatus setup_telegram(setup_telegram_request)

Setup Telegram integration

Configure Telegram for notifications or integrations.

### Example

* Bearer (Opaque) Authentication (bearerAuth):

```python
import quepasa
from quepasa.models.setup_telegram_request import SetupTelegramRequest
from quepasa.models.telegram_status import TelegramStatus
from quepasa.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.quepasa.ai/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = quepasa.Configuration(
    host = "https://api.quepasa.ai/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (Opaque): bearerAuth
configuration = quepasa.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with quepasa.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    client = quepasa.DefaultApi(api_client)
    setup_telegram_request = {
        'token': "--TELEGRAM-BOT-TOKEN---",
        'commands': {
            'start': {
                'name': "Bot info",
                'message': "Hello, this is bot for my data",
            },
            'ask': {
                'name': "Ask a question",
                'message': "Ask any question",
            },
        },
    }

    try:
        # Setup Telegram integration
        response = client.setup_telegram(setup_telegram_request)
        print("The response of client.setup_telegram:\n")
        pprint(response)
    except Exception as e:
        print("Exception when calling client.setup_telegram: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **setup_telegram_request** | [**SetupTelegramRequest**](SetupTelegramRequest.md)|  |

### Return type

[**TelegramStatus**](TelegramStatus.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Telegram successfully set up. |  -  |
**500** | Operation failed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
