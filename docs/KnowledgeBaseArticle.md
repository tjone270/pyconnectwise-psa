# KnowledgeBaseArticle


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**board** | [**BoardReference**](BoardReference.md) |  | [optional] 
**business_unit_id** | **int** |  | [optional] 
**category_id** | **int** |  | [optional] 
**created_by** | **str** |  | [optional] 
**date_created** | **str** |  | [optional] 
**id** | **int** |  | [optional] 
**issue** | **str** |  | 
**location_id** | **int** |  | [optional] 
**resolution** | **str** |  | 
**sub_category_id** | **int** |  | [optional] 
**title** | **str** |  | 

## Example

```python
from connectwise_psa.models.knowledge_base_article import KnowledgeBaseArticle

# TODO update the JSON string below
json = "{}"
# create an instance of KnowledgeBaseArticle from a JSON string
knowledge_base_article_instance = KnowledgeBaseArticle.from_json(json)
# print the JSON string representation of the object
print KnowledgeBaseArticle.to_json()

# convert the object into a dict
knowledge_base_article_dict = knowledge_base_article_instance.to_dict()
# create an instance of KnowledgeBaseArticle from a dict
knowledge_base_article_form_dict = knowledge_base_article.from_dict(knowledge_base_article_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


