# MemberDeactivationKnowledgebaseArticle


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | [optional] 
**re_assign_to_member** | [**MemberReference**](MemberReference.md) |  | [optional] 

## Example

```python
from connectwise_psa.models.member_deactivation_knowledgebase_article import MemberDeactivationKnowledgebaseArticle

# TODO update the JSON string below
json = "{}"
# create an instance of MemberDeactivationKnowledgebaseArticle from a JSON string
member_deactivation_knowledgebase_article_instance = MemberDeactivationKnowledgebaseArticle.from_json(json)
# print the JSON string representation of the object
print MemberDeactivationKnowledgebaseArticle.to_json()

# convert the object into a dict
member_deactivation_knowledgebase_article_dict = member_deactivation_knowledgebase_article_instance.to_dict()
# create an instance of MemberDeactivationKnowledgebaseArticle from a dict
member_deactivation_knowledgebase_article_form_dict = member_deactivation_knowledgebase_article.from_dict(member_deactivation_knowledgebase_article_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


