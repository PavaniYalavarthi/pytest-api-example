from jsonschema import validate
import pytest
import schemas
import api_helpers
from hamcrest import assert_that, contains_string, is_

'''
TODO: Finish this test by...
1) Creating a function to test the PATCH request /store/order/{order_id}
2) *Optional* Consider using @pytest.fixture to create unique test data for each run
2) *Optional* Consider creating an 'Order' model in schemas.py and validating it in the test
3) Validate the response codes and values
4) Validate the response message "Order and pet status updated successfully"
'''
def test_patch_order_by_id():
    order_id = 1
    test_endpoint = f"/store/order/{order_id}"

    patch_payload = {
        "status" : "delivered",
        "pet_status": "available"
    }

    response = api_helpers.patch_api_data(test_endpoint, patch_payload)
    assert response.status_code == 200, f"Expected 200, got {response.status_code}: {response.text}"

    response_data = response.json()

    assert "Order and pet status updated successfully" in response_data.get("message",""), f"Expected success message, got: {response_data.get('message')}"

    if hasattr(schemas, "order"):
        validate(instance=response_data, schema=schemas.order)
