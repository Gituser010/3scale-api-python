from tests.integration.asserts import assert_resource
from tests.integration.asserts import assert_resource_params


def test_account_plans_list(api, account_plan):
    account_plans = api.account_plans.list()
    assert len(account_plans) >= 1


def test_account_plan_can_be_created(api, account_plan, account_plans_params):
    assert_resource(account_plan)
    assert_resource_params(account_plan, account_plans_params)


def test_account_plan_update(account_plan, account_plans_update_params):
    updated_account_plan = account_plan.update(params=account_plans_update_params)
    assert_resource(updated_account_plan)
    assert_resource_params(updated_account_plan, account_plans_update_params)


def test_account_plan_can_be_read(api, account_plan, account_plans_params):
    read = api.account_plans.read(account_plan.entity_id)
    assert_resource(read)
    assert_resource_params(read, account_plans_params)
