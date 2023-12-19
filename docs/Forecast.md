# Forecast


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**agreement_revenue** | [**AgreementRevenueReference**](AgreementRevenueReference.md) |  | [optional] 
**billing_terms** | [**BillingTermsReference**](BillingTermsReference.md) |  | [optional] 
**currency** | [**CurrencyReference**](CurrencyReference.md) |  | [optional] 
**expected_probability** | **int** |  | [optional] 
**expense_revenue** | [**ExpenseRevenueReference**](ExpenseRevenueReference.md) |  | [optional] 
**forecast_items** | [**List[ForecastItem]**](ForecastItem.md) |  | [optional] 
**forecast_revenue_totals** | [**ForecastRevenueReference**](ForecastRevenueReference.md) |  | [optional] 
**forecast_total_with_taxes** | **float** |  | [optional] 
**id** | **int** |  | [optional] 
**inclusive_revenue_totals** | [**InclusiveRevenueReference**](InclusiveRevenueReference.md) |  | [optional] 
**lost_revenue** | [**LostRevenueReference**](LostRevenueReference.md) |  | [optional] 
**open_revenue** | [**OpenRevenueReference**](OpenRevenueReference.md) |  | [optional] 
**other_revenue1** | [**Other1RevenueReference**](Other1RevenueReference.md) |  | [optional] 
**other_revenue2** | [**Other2RevenueReference**](Other2RevenueReference.md) |  | [optional] 
**product_revenue** | [**ProductRevenueReference**](ProductRevenueReference.md) |  | [optional] 
**recurring_total** | **float** |  | [optional] 
**sales_tax_revenue** | **float** |  | [optional] 
**service_revenue** | [**ServiceRevenueReference**](ServiceRevenueReference.md) |  | [optional] 
**tax_code** | [**TaxCodeReference**](TaxCodeReference.md) |  | [optional] 
**time_revenue** | [**TimeRevenueReference**](TimeRevenueReference.md) |  | [optional] 
**won_revenue** | [**WonRevenueReference**](WonRevenueReference.md) |  | [optional] 

## Example

```python
from connectwise_psa.models.forecast import Forecast

# TODO update the JSON string below
json = "{}"
# create an instance of Forecast from a JSON string
forecast_instance = Forecast.from_json(json)
# print the JSON string representation of the object
print Forecast.to_json()

# convert the object into a dict
forecast_dict = forecast_instance.to_dict()
# create an instance of Forecast from a dict
forecast_form_dict = forecast.from_dict(forecast_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


