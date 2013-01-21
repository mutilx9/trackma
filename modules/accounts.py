import utils
import cPickle

class AccountManager(object):
    accountfile = utils.get_root_filename('accounts')
    accounts = {'default': None, 'accounts': []}
    filename = 'accounts'

    def __init__(self):
        self.filename = utils.get_root_filename('accounts')
        self._load()

    def _load(self):
        if utils.file_exists(self.filename):
            print self.filename
            with open(self.filename, 'rb') as f:
                self.accounts = cPickle.load(f)

    def _save(self):
        print self.filename
        with open(self.filename, 'wb') as f:
            cPickle.dump(self.accounts, f)
            f.write('ok')

    def add_account(self, username, password, api):
        account = {'username': username,
                   'password': password,
                   'api': api,
                  }
        self.accounts['accounts'].append(account)
        self._save()

    def get_accounts(self):
        return self.accounts['accounts']

    def get_default(self):
        return self.accounts['default']

    def set_default(self, val):
        self.accounts['default'] = val

    def unset_default(self):
        self.accounts['default'] = None

