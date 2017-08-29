import bcrypt as bcrypt
from eve import Eve
from eve.auth import BasicAuth


class BCryptAuth(BasicAuth):
    def check_auth(self, username, password, allowed_roles, resource, method):
        # use Eve's own db driver; no additional connections/resources are used
        accounts = app.data.driver.db['accounts']
        account = accounts.find_one({'username': username})
        return account and \
            bcrypt.hashpw(password, account['password']) == account['password']


app = Eve()
app.run()

@app.route('/agencies')
def agencies():
    return ['grt', 'translink']
