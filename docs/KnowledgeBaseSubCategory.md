# KnowledgeBaseSubCategory


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**category** | [**KBCategoryReference**](KBCategoryReference.md) |  | 
**department** | [**SystemDepartmentReference**](SystemDepartmentReference.md) |  | [optional] 
**id** | **int** |  | [optional] 
**location** | [**SystemLocationReference**](SystemLocationReference.md) |  | [optional] 
**name** | **str** |  Max length: 50; | 

## Example

```python
from connectwise_psa.models.knowledge_base_sub_category import KnowledgeBaseSubCategory

# TODO update the JSON string below
json = "{}"
# create an instance of KnowledgeBaseSubCategory from a JSON string
knowledge_base_sub_category_instance = KnowledgeBaseSubCategory.from_json(json)
# print the JSON string representation of the object
print KnowledgeBaseSubCategory.to_json()

# convert the object into a dict
knowledge_base_sub_category_dict = knowledge_base_sub_category_instance.to_dict()
# create an instance of KnowledgeBaseSubCategory from a dict
knowledge_base_sub_category_form_dict = knowledge_base_sub_category.from_dict(knowledge_base_sub_category_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


