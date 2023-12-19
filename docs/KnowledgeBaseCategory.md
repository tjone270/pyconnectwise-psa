# KnowledgeBaseCategory


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**approver** | [**MemberReference**](MemberReference.md) |  | [optional] 
**department** | [**SystemDepartmentReference**](SystemDepartmentReference.md) |  | [optional] 
**id** | **int** |  | [optional] 
**location** | [**SystemLocationReference**](SystemLocationReference.md) |  | [optional] 
**name** | **str** |  Max length: 50; | 

## Example

```python
from connectwise_psa.models.knowledge_base_category import KnowledgeBaseCategory

# TODO update the JSON string below
json = "{}"
# create an instance of KnowledgeBaseCategory from a JSON string
knowledge_base_category_instance = KnowledgeBaseCategory.from_json(json)
# print the JSON string representation of the object
print KnowledgeBaseCategory.to_json()

# convert the object into a dict
knowledge_base_category_dict = knowledge_base_category_instance.to_dict()
# create an instance of KnowledgeBaseCategory from a dict
knowledge_base_category_form_dict = knowledge_base_category.from_dict(knowledge_base_category_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


