from tests.integration import asserts
from tests.integration.conftest import backend
from threescale_api.resources import Backend


def test_backend_usage_can_be_created(backend_usage, backend_usage_params):
    asserts.assert_resource(backend_usage)
    asserts.assert_resource_params(backend_usage, backend_usage_params)


def test_backend_usages_list(api, backend_usage, backend):
    backend : Backend = api.backends.get(backend['id'])
    backend_usages = backend.usages()
    assert  len(backend_usages) >= 1


def test_backend_usage_update(backend_usage, backend, backend_usage_update_params):
    updated_backend_usage = backend_usage.update(backend_usage_update_params)
    asserts.assert_resource(updated_backend_usage)
    asserts.assert_resource_params(updated_backend_usage, backend_usage_update_params)
