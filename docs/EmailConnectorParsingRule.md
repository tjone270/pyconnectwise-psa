# EmailConnectorParsingRule


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**id** | **int** |  | [optional] 
**parsing_style** | [**EmailConnectorParsingStyleReference**](EmailConnectorParsingStyleReference.md) |  | [optional] 
**parsing_variable** | [**EmailConnectorParsingVariableReference**](EmailConnectorParsingVariableReference.md) |  | [optional] 
**priority** | **int** |  | 
**search_term** | **str** |  Max length: 250; | 
**service_board** | [**BoardReference**](BoardReference.md) |  | [optional] 
**service_item** | [**ServiceItemReference**](ServiceItemReference.md) |  | [optional] 
**service_priority** | [**PriorityReference**](PriorityReference.md) |  | [optional] 
**service_status** | [**ServiceStatusReference**](ServiceStatusReference.md) |  | [optional] 
**service_sub_type** | [**ServiceSubTypeReference**](ServiceSubTypeReference.md) |  | [optional] 
**service_type** | [**ServiceTypeReference**](ServiceTypeReference.md) |  | [optional] 

## Example

```python
from connectwise_psa.models.email_connector_parsing_rule import EmailConnectorParsingRule

# TODO update the JSON string below
json = "{}"
# create an instance of EmailConnectorParsingRule from a JSON string
email_connector_parsing_rule_instance = EmailConnectorParsingRule.from_json(json)
# print the JSON string representation of the object
print EmailConnectorParsingRule.to_json()

# convert the object into a dict
email_connector_parsing_rule_dict = email_connector_parsing_rule_instance.to_dict()
# create an instance of EmailConnectorParsingRule from a dict
email_connector_parsing_rule_form_dict = email_connector_parsing_rule.from_dict(email_connector_parsing_rule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


