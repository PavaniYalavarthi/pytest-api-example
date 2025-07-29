from jsonschema import validate
import pytest
import schemas
import api_helpers
from hamcrest import assert_that, contains_string, is_

'''
TODO: Finish this test by...
1) Troubleshooting and fixing the test failure
The purpose of this test is to validate the response matches the expected schema defined in schemas.py
'''
def test_pet_schema():
    test_endpoint = "/pets/1"

    response = api_helpers.get_api_data(test_endpoint)

    assert response.status_code == 200, f"Expected 200, got {response.status_code}: {response.text}"

    # Validate the response schema against the defined schema in schemas.py
    response_data = response.json()
    validate(instance=response.json(), schema=schemas.pet)

'''
TODO: Finish this test by...
1) Extending the parameterization to include all available statuses
2) Validate the appropriate response code
3) Validate the 'status' property in the response is equal to the expected status
4) Validate the schema for each object in the response
'''
@pytest.mark.parametrize("status", [("available")])
def test_find_by_status_200(status):
    test_endpoint = "/pets/findByStatus"
    params = {
        "status": status
    }

    response = api_helpers.get_api_data(test_endpoint, params)
    # TODO...

    assert response.status_code == 200, f"Expected 200, got {response.status_code}:{response.text}"
    response_data = response.json()

    for pet in response_data:
        assert pet.get("status") == status, f"Expected status {status}, got {pet.get('status')}"
        validate(instance=pet, schema= schemas.pet)

'''
TODO: Finish this test by...
1) Testing and validating the appropriate 404 response for /pets/{pet_id}
2) Parameterizing the test for any edge cases
'''
def test_get_by_id_404(invalid_pet_id):
    # TODO...
    test_endpoint = f"/pets/{invalid_pet_id}"

    response = api_helpers.get_api_data(test_endpoint)

    assert response.status_code == 404, f"Expected 404, got {response.status_code}: {response.text}"

    assert_that(response.text.lower(), contains_string("not found"))