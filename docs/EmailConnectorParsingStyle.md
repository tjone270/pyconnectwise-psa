# EmailConnectorParsingStyle


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**id** | **int** |  | [optional] 
**parse_rule** | **str** |  Max length: 500; | 
**parsing_type** | [**EmailConnectorParsingTypeReference**](EmailConnectorParsingTypeReference.md) |  | [optional] 
**priority** | **int** |  | 

## Example

```python
from connectwise_psa.models.email_connector_parsing_style import EmailConnectorParsingStyle

# TODO update the JSON string below
json = "{}"
# create an instance of EmailConnectorParsingStyle from a JSON string
email_connector_parsing_style_instance = EmailConnectorParsingStyle.from_json(json)
# print the JSON string representation of the object
print EmailConnectorParsingStyle.to_json()

# convert the object into a dict
email_connector_parsing_style_dict = email_connector_parsing_style_instance.to_dict()
# create an instance of EmailConnectorParsingStyle from a dict
email_connector_parsing_style_form_dict = email_connector_parsing_style.from_dict(email_connector_parsing_style_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


