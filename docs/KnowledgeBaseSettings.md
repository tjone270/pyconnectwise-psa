# KnowledgeBaseSettings


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**default_approver** | [**MemberReference**](MemberReference.md) |  | [optional] 
**id** | **int** |  | [optional] 
**require_approval** | **bool** |  | 

## Example

```python
from connectwise_psa.models.knowledge_base_settings import KnowledgeBaseSettings

# TODO update the JSON string below
json = "{}"
# create an instance of KnowledgeBaseSettings from a JSON string
knowledge_base_settings_instance = KnowledgeBaseSettings.from_json(json)
# print the JSON string representation of the object
print KnowledgeBaseSettings.to_json()

# convert the object into a dict
knowledge_base_settings_dict = knowledge_base_settings_instance.to_dict()
# create an instance of KnowledgeBaseSettings from a dict
knowledge_base_settings_form_dict = knowledge_base_settings.from_dict(knowledge_base_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


