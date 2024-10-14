from tests.integration.asserts import assert_resource, assert_resource_params


def test_accounts_list(api, account):
    accounts = api.accounts.list()
    assert len(accounts) >= 1


def test_account_can_be_created(api, account, account_params):
    assert_resource(account)
    assert_resource_params(account, account_params)


def test_account_update(api,account,update_account_params):
    updated_account = account.update(params=update_account_params)
    assert_resource(updated_account)
    assert_resource_params(updated_account,update_account_params)


def test_account_can_be_read(api, account, account_params):
    read = api.accounts.read(account.entity_id)
    assert_resource(read)
    assert_resource_params(read, account_params)


def test_account_can_be_read_by_name(api, account, account_params):
    account_name = account['org_name']
    read = api.accounts[account_name]
    assert_resource(read)
    assert_resource_params(read, account_params)


def test_users_list(api, account):
    assert len(account.users.list()) >= 1
